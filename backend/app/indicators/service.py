# backend/app/indicators/service.py
import asyncio
import logging
import time
from datetime import datetime, timezone
from typing import Dict, Tuple

from app.api.websockets import manager as websocket_manager
from app.core.transcript import transcript_store
from app.services.openai_service import OpenAIService
from app.indicators.definitions import ALL_INDICATORS
from app.indicators.observability import indicator_logger, IndicatorEvaluationLog

logger = logging.getLogger(__name__)

class IndicatorService:
    def __init__(self, ws_manager, session_id: str = ""):
        self.ws_manager = ws_manager
        self.session_id = session_id
        self.openai_service = OpenAIService()
        # Track last triggered times to avoid re-triggering too frequently
        self.last_triggered: Dict[str, float] = {}
        self.min_retrigger_interval = 60  # Minimum seconds before re-triggering same indicator

    def _parse_llm_response(self, response: str) -> Tuple[bool, str]:
        """
        Parses the 'yes/no, rationale' format from the LLM.
        
        Returns:
            Tuple of (should_trigger, justification_text)
        """
        try:
            # Clean up the response
            response = response.strip().lower()
            
            # Check if it starts with yes or no
            if response.startswith("yes"):
                # Extract rationale after comma
                parts = response.split(",", 1)
                rationale = parts[1].strip() if len(parts) > 1 else "condition detected"
                return True, rationale
            elif response.startswith("no"):
                # Extract rationale after comma
                parts = response.split(",", 1)
                rationale = parts[1].strip() if len(parts) > 1 else "condition not met"
                return False, rationale
            else:
                # If response doesn't follow format, log and don't trigger
                logger.warning(f"Unexpected LLM response format: {response}")
                return False, "unable to parse response"
        except Exception as e:
            logger.error(f"Error parsing LLM response: {e}")
            return False, "error parsing response"

    async def _check_all_indicators(self):
        """Runs one cycle of checking all defined indicators."""
        current_time = time.time()
        
        for indicator in ALL_INDICATORS:
            try:
                # Check if we've triggered this indicator too recently
                last_trigger_time = self.last_triggered.get(indicator["id"], 0)
                if current_time - last_trigger_time < self.min_retrigger_interval:
                    continue
                
                # Get the transcript for the specified window
                transcript_text = transcript_store.get_formatted_transcript_for_window(
                    seconds=indicator["window_seconds"]
                )
                
                if not transcript_text:  # Not enough data yet
                    continue
                
                # Format the prompt with the transcript
                prompt = indicator["prompt_template"].format(
                    transcript_text=transcript_text,
                    window_seconds=indicator["window_seconds"]
                )
                
                # Time the LLM call
                start_time = time.time()
                
                # Call LLM with low temperature for consistent responses
                llm_response = await self.openai_service.generate_response(
                    prompt=prompt, 
                    temperature=0.2
                )
                
                # Calculate LLM call duration
                llm_duration_ms = int((time.time() - start_time) * 1000)
                
                if not llm_response:
                    continue
                
                # Parse the response
                should_trigger, justification = self._parse_llm_response(llm_response)
                
                # Determine if alert was actually triggered (respecting cooldown)
                alert_triggered = False
                if should_trigger:
                    # Update last triggered time
                    self.last_triggered[indicator["id"]] = current_time
                    alert_triggered = True
                    
                    # Broadcast the indicator trigger
                    payload = {
                        "type": "indicator_triggered",
                        "data": {
                            "id": indicator["id"],
                            "name": indicator["name"],
                            "justification": justification,
                            "timestamp": current_time
                        }
                    }
                    await self.ws_manager.broadcast(payload)
                    logger.info(f"Indicator triggered: {indicator['name']} - {justification}")
                
                # Create log entry for observability
                log_entry = IndicatorEvaluationLog(
                    session_id=self.session_id,
                    check_timestamp_utc=datetime.now(timezone.utc).isoformat(),
                    indicator_id=indicator["id"],
                    indicator_name=indicator["name"],
                    transcript_window_seconds=indicator["window_seconds"],
                    transcript_snippet=transcript_text,
                    llm_prompt=prompt,
                    llm_response_raw=llm_response,
                    llm_call_duration_ms=llm_duration_ms,
                    parsed_decision=should_trigger,
                    parsed_rationale=justification,
                    triggered_alert=alert_triggered
                )
                
                # Log the evaluation
                indicator_logger.log_evaluation(log_entry)
                    
            except Exception as e:
                logger.error(f"Error checking indicator {indicator['id']}: {e}", exc_info=True)

    async def start_periodic_checks(self, interval_seconds: int = 15):
        """
        The main background loop that runs for the duration of a session.
        
        Args:
            interval_seconds: How often to check indicators (default: 15 seconds)
        """
        logger.info(f"Indicator service started. Checking every {interval_seconds} seconds.")
        
        try:
            while True:
                try:
                    await self._check_all_indicators()
                except Exception as e:
                    logger.error(f"Error in indicator check loop: {e}", exc_info=True)
                
                await asyncio.sleep(interval_seconds)
                
        except asyncio.CancelledError:
            logger.info("Indicator service stopped.")
            raise