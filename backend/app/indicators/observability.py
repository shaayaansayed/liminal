"""
Observability module for the Indicator Service.
Provides structured logging of indicator evaluations for debugging and analysis.
"""
import json
import os
from datetime import datetime, timezone
from typing import List, Optional
from pydantic import BaseModel
import logging
from app.core.config import settings

logger = logging.getLogger(__name__)

class IndicatorEvaluationLog(BaseModel):
    """Data model for a single indicator evaluation log entry."""
    session_id: str
    check_timestamp_utc: str
    indicator_id: str
    indicator_name: str
    transcript_window_seconds: int
    transcript_snippet: str
    llm_prompt: str
    llm_response_raw: str
    llm_call_duration_ms: int
    parsed_decision: bool
    parsed_rationale: str
    triggered_alert: bool


class IndicatorLogger:
    """
    Manages observability logging for the indicator service.
    Operates as a singleton to centralize all logging concerns.
    """
    
    def __init__(self):
        """Initialize the logger with configuration from environment."""
        self.enabled = settings.INDICATOR_OBSERVABILITY_ENABLED
        self.log_path = settings.INDICATOR_LOG_PATH
        self.logs: List[IndicatorEvaluationLog] = []
        self.session_id: Optional[str] = None
        
        if self.enabled:
            logger.info(f"Indicator observability enabled. Logs will be saved to: {self.log_path}")
        else:
            logger.info("Indicator observability disabled.")
    
    def start_session(self) -> str:
        """
        Start a new logging session.
        Returns the generated session ID.
        """
        if not self.enabled:
            return ""
            
        # Generate unique session ID with timestamp
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        self.session_id = f"session_{timestamp}"
        
        # Clear any previous logs
        self.logs = []
        
        return self.session_id
    
    def log_evaluation(self, log_entry: IndicatorEvaluationLog) -> None:
        """
        Add an evaluation log entry to the current session.
        
        Args:
            log_entry: The structured log data to record
        """
        if not self.enabled:
            return
            
        self.logs.append(log_entry)
    
    def end_session_and_save(self) -> None:
        """
        End the current session and save all logs to a JSON file.
        """
        if not self.enabled or not self.logs:
            return
        
        # Create log directory if it doesn't exist
        os.makedirs(self.log_path, exist_ok=True)
        
        # Generate filename with session ID and timestamp
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%S")
        filename = f"{self.session_id}_{timestamp}_log.json"
        filepath = os.path.join(self.log_path, filename)
        
        # Convert logs to dictionaries for JSON serialization
        log_data = {
            "session_id": self.session_id,
            "total_evaluations": len(self.logs),
            "session_end_time": datetime.now(timezone.utc).isoformat(),
            "evaluations": [log.dict() for log in self.logs]
        }
        
        # Write to file
        with open(filepath, 'w') as f:
            json.dump(log_data, f, indent=2)
        
        print(f"Indicator logs saved to: {filepath}")
        
        # Clear logs after saving
        self.logs = []
        self.session_id = None


# Singleton instance
indicator_logger = IndicatorLogger()