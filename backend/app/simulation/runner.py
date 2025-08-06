# backend/app/simulation/runner.py
import asyncio
import logging
from datetime import datetime, timezone
from typing import Dict

# Internal Application Imports
from app.api.websockets import manager
from app.services.recall_service import (
    create_scribe_bot,
    create_speaker_bot,
    send_audio_to_bot,
    register_event_callback,
    unregister_event_callback
)
from app.services.conversation_event_service import conversation_event_service
from app.services.openai_service import OpenAIService
from app.simulation import engine
from app.simulation.agents import ALL_AGENTS
from app.simulation.zoom_turnflow import MEETING, TurnPhase, turnflow_monitor
from app.indicators.observability import indicator_logger

# Create service instance
openai_service = OpenAIService()

logger = logging.getLogger(__name__)


async def run_text_simulation_loop(turn_provider=None):
    """
    Main simulation loop for text-only mode.
    The loop now uses the ConversationEventService to persist and broadcast.
    
    Args:
        turn_provider: Callable that returns (agent, text) tuple. 
                      If None, defaults to engine.run_simulation_turn
    """
    # Default to the live engine if no provider specified
    if turn_provider is None:
        turn_provider = engine.run_simulation_turn
        
    logger.info("Text simulation loop started")
    await asyncio.sleep(5)
    
    try:
        while True:
            await asyncio.sleep(3)
            
            # Step 1: Get the next turn from the provider
            agent, text = await turn_provider()
            
            if agent and text:
                # Step 2: The event service handles PERSISTENCE and BROADCASTING
                await conversation_event_service.handle_simulated_utterance(agent, text)
                logger.info(f"Simulation message processed from {agent['name']}")
            else:
                # No more turns available (could be end of demo or engine decision)
                logger.info("No message generated in simulation turn - simulation may be complete")
                # For demos, this signals the end. For live simulations, it continues.
                if turn_provider != engine.run_simulation_turn:
                    break
                
    except asyncio.CancelledError:
        logger.info("Text simulation loop cancelled.")
        raise
    except Exception as e:
        logger.error(f"Text simulation loop error: {str(e)}", exc_info=True)
        # Clean shutdown instead of automatic restart
        logger.info("Text simulation loop terminated due to error")
    finally:
        logger.info("Text simulation loop finished.")


async def run_zoom_simulation_loop(meeting_url: str, turn_provider=None):
    """
    Simulation loop for Zoom-based mode with audio.
    It is now fully self-contained, managing its own state and callbacks.
    
    Args:
        meeting_url: The Zoom meeting URL to join
        turn_provider: Callable that returns (agent, text) tuple. 
                      If None, defaults to engine.run_simulation_turn
    """
    # Default to the live engine if no provider specified
    if turn_provider is None:
        turn_provider = engine.run_simulation_turn
        
    logger.info(f"Zoom simulation loop starting for URL: {meeting_url}")
    
    # --- 1. Create a Scribe Bot to listen for events ---
    logger.info("Creating Scribe Bot to monitor joins...")
    scribe_res = await create_scribe_bot(meeting_url)
    if scribe_res.get("error"):
        logger.error(f"Fatal: Could not create Scribe Bot. Ending simulation. Details: {scribe_res}")
        return
    logger.info(" Scribe Bot created successfully.")
    
    # --- 2. Define Local State and Callbacks ---
    
    # This dictionary is now LOCAL to this function, not a global.
    bots_to_join_events: Dict[str, asyncio.Event] = {}
    
    def _on_transcript_event(payload: dict):
        """This function will be called by the recall_service for transcript events."""
        logger.debug("Zoom simulation turn-flow callback triggered.")
        MEETING.last_ts = datetime.now(timezone.utc)
        if MEETING.phase is TurnPhase.PLAYING:
            MEETING.phase = TurnPhase.TRANSCRIBING
            
    def _on_participant_join(payload: dict):
        """Callback to handle participant join events for this specific simulation."""
        data = payload.get("data", {}).get("data", {})
        participant = data.get("participant", {})
        participant_name = participant.get("name")
        
        # Check against our LOCAL dictionary
        if participant_name in bots_to_join_events:
            join_event = bots_to_join_events.get(participant_name)
            if join_event:
                logger.info(f" Simulation bot '{participant_name}' joined. Setting event.")
                join_event.set() # Signal that this specific bot has joined!

        # This is also a good place for the generic UI broadcast
        asyncio.create_task(
            manager.broadcast({
                "type": "participant_event",
                "event": "join",
                "participant": participant.get("name", "Unknown"),
                "participant_id": participant.get("id"),
            })
        )
    
    # --- 3. Register Callbacks ---
    register_event_callback("transcript.data", _on_transcript_event)
    register_event_callback("transcript.partial_data", _on_transcript_event)
    register_event_callback("participant_events.join", _on_participant_join)
    
    # Start the monitor task only for this loop
    monitor_task = asyncio.create_task(turnflow_monitor())
    
    try:
        # --- 4. Create Speaker Bots using LOCAL state ---
        speaker_bots = []
        tasks_to_wait_for = []

        for agent in ALL_AGENTS:
            bot_name = f"Sim-{agent['name']}"
            
            # Create an asyncio Event that the webhook will trigger
            join_event = asyncio.Event()
            # Populate the LOCAL dictionary
            bots_to_join_events[bot_name] = join_event
            tasks_to_wait_for.append(join_event.wait())
            
            logger.info(f"Creating speaker bot: {bot_name}")
            try:
                response = await create_speaker_bot(meeting_url, bot_name)
                bot_id = response.get("id")
                if bot_id:
                    speaker_bots.append({
                        "id": bot_id,
                        "agent": agent
                    })
                    logger.info(f"Speaker bot '{bot_name}' is being created with ID: {bot_id}")
                else:
                    logger.error(f"Failed to create speaker bot: {bot_name}. Details: {response}")
                    # If creation fails, remove the corresponding wait task
                    tasks_to_wait_for.pop()
                    bots_to_join_events.pop(bot_name, None)

            except Exception as e:
                logger.error(f"Exception creating speaker bot {bot_name}: {str(e)}")
                tasks_to_wait_for.pop()
                bots_to_join_events.pop(bot_name, None)

        if not speaker_bots:
            logger.error("No speaker bots were created. Ending Zoom simulation.")
            return

        # --- 5. Wait for all Speaker Bots to join the meeting ---
        logger.info(f"Waiting for {len(tasks_to_wait_for)} speaker bot(s) to join...")
        await asyncio.wait_for(asyncio.gather(*tasks_to_wait_for), timeout=180.0)
        logger.info(" All speaker bots have joined the meeting. Starting conversation.")

        # --- 6. Run the main conversation loop ---
        agent_to_bot_id = {bot['agent']['name']: bot['id'] for bot in speaker_bots}
        while True:
            # Wait until the room has been quiet long enough
            while MEETING.phase is not TurnPhase.READY:
                await asyncio.sleep(0.05)
            
            logger.info("Room is READY. Proceeding with next turn.")

            # Get the turn result from the turn provider
            agent, text = await turn_provider()
            
            if agent and text:
                # NOTE: We don't broadcast here - the actual transcription will come through webhooks
                # This prevents duplicate messages in the UI
                
                # Pass the agent's voice to generate_speech
                audio_data = await openai_service.generate_speech(text, voice=agent['voice'])
                bot_id = agent_to_bot_id.get(agent['name'])
                
                if audio_data and bot_id:
                    speak_response = await send_audio_to_bot(bot_id, audio_data)
                    if speak_response and speak_response.get("error"):
                        logger.error(f"Failed to send audio for {agent['name']}: {speak_response.get('error')} - {speak_response.get('details', '')}")
                    else:
                        logger.info(f"Audio sent to bot {agent['name']}. Phase -> PLAYING")
                        MEETING.phase = TurnPhase.PLAYING
                else:
                    logger.warning(f"Could not send audio for {agent['name']}. Missing audio data or bot ID.")
            else:
                # No more turns available (could be end of demo)
                logger.info("No message generated in simulation turn - simulation may be complete")
                # For demos, this signals the end. For live simulations, it continues.
                if turn_provider != engine.run_simulation_turn:
                    logger.info("Demo finished - ending Zoom simulation")
                    break
    except Exception as e:
        logger.error(f"Zoom simulation loop error: {str(e)}")
    finally:
        # --- 7. CRITICAL: Cleanup ---
        logger.info("Cleaning up Zoom simulation loop resources.")
        monitor_task.cancel()  # avoid task leak if loop exits
        # Unregister all callbacks to prevent leaks
        unregister_event_callback("transcript.data", _on_transcript_event)
        unregister_event_callback("transcript.partial_data", _on_transcript_event)
        unregister_event_callback("participant_events.join", _on_participant_join)
        
        logger.info("Zoom simulation finished.")