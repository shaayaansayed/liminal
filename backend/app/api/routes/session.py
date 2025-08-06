"""
Session management endpoints.
"""
import asyncio
import json
import logging
import os
from datetime import datetime
from typing import Literal, Optional, List, Dict

from fastapi import APIRouter
from pydantic import BaseModel

from app.api.websockets import manager
from app.services.recall_service import create_bot
from app.simulation import runner, engine
from app.simulation.conversation import conversation_manager
from app.simulation.demo_provider import DemoTurnProvider
from app.core.transcript import transcript_store
from app.indicators.service import IndicatorService
from app.indicators.observability import indicator_logger

# Module-level variables to hold background task references
indicator_task: Optional[asyncio.Task] = None
simulation_task: Optional[asyncio.Task] = None

logging.basicConfig(level=logging.INFO, format='%(levelname)s:     %(name)s - %(message)s')
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api", tags=["session"])


# Request models
class SessionConfig(BaseModel):
    sessionType: Literal['real', 'simulation']
    isTextBased: bool
    meetingUrl: Optional[str] = None
    demoId: Optional[str] = None


@router.post("/session")
async def start_session(config: SessionConfig):
    """
    Unified endpoint for starting any type of session with on-demand orchestration.
    """
    global indicator_task, simulation_task
    
    # Start a new observability session
    session_id = indicator_logger.start_session()
    
    # Cancel any existing indicator task before starting a new session
    if indicator_task and not indicator_task.done():
        logger.info("Cancelling existing indicator service task.")
        indicator_task.cancel()
        indicator_task = None
    
    if not config.isTextBased and not config.meetingUrl:
        return {"error": "meetingUrl is required for non-text-based sessions"}
    
    if config.sessionType == "real":
        # Real session: create monitoring bot (reactive mode)
        logger.info(f"Starting real session with URL: {config.meetingUrl}")
        result = await create_bot(config.meetingUrl)
        
        # Start indicator service for real sessions
        indicator_service = IndicatorService(manager, session_id)
        indicator_task = asyncio.create_task(indicator_service.start_periodic_checks())
        logger.info("Indicator service started for real session")
        
        return result
    
    elif config.sessionType == "simulation":
        # Determine which turn provider to use
        if config.demoId:
            # Create a demo turn provider
            logger.info(f"Creating demo turn provider for demoId: {config.demoId}")
            demo_provider = DemoTurnProvider(config.demoId)
            turn_provider = demo_provider.get_next_turn
        else:
            # Use the live engine
            logger.info("Using live engine for simulation")
            turn_provider = engine.run_simulation_turn
        
        # Now route to the appropriate runner with the turn provider
        if config.isTextBased:
            # Text-based simulation: start background loop
            logger.info(f"Starting text-based simulation session{' (demo)' if config.demoId else ''}")
            
            # Create background task for text simulation with the turn provider
            simulation_task = asyncio.create_task(runner.run_text_simulation_loop(turn_provider=turn_provider))
            
            # Start indicator service for text simulation
            indicator_service = IndicatorService(manager, session_id)
            indicator_task = asyncio.create_task(indicator_service.start_periodic_checks())
            logger.info("Indicator service started for text simulation")
            
            return {
                "status": "success",
                "message": f"{'Demo' if config.demoId else 'Text-based'} simulation started",
                "session_type": "demo-simulation" if config.demoId else "text-simulation",
                "id": f"{'demo' if config.demoId else 'text'}-sim-{datetime.now().timestamp()}"
            }
        else:
            # Zoom-based simulation: start background audio loop
            logger.info(f"Starting Zoom-based simulation for URL: {config.meetingUrl}{' (demo)' if config.demoId else ''}")
            
            # Create background task for Zoom simulation with the turn provider
            simulation_task = asyncio.create_task(runner.run_zoom_simulation_loop(config.meetingUrl, turn_provider=turn_provider))
            
            # Start indicator service for Zoom simulation
            indicator_service = IndicatorService(manager, session_id)
            indicator_task = asyncio.create_task(indicator_service.start_periodic_checks())
            logger.info("Indicator service started for Zoom simulation")
            
            return {
                "status": "success",
                "message": f"Zoom-based {'demo' if config.demoId else ''} simulation started",
                "meeting_url": config.meetingUrl,
                "session_type": "demo-simulation" if config.demoId else "zoom-simulation",
                "id": f"{'demo' if config.demoId else 'zoom'}-sim-{datetime.now().timestamp()}"
            }


@router.post("/reset-session")
async def reset_session():
    """Reset the current session."""
    global indicator_task, simulation_task
    
    # Save observability logs before resetting
    indicator_logger.end_session_and_save()
    
    tasks_to_cancel = []

    # Cancel the indicator service task
    if indicator_task and not indicator_task.done():
        logger.info("Cancelling indicator service task.")
        indicator_task.cancel()
        tasks_to_cancel.append(indicator_task)

    # Cancel the simulation runner task
    if simulation_task and not simulation_task.done():
        logger.info("Cancelling simulation runner task.")
        simulation_task.cancel()
        tasks_to_cancel.append(simulation_task)

    # Wait for all tasks to acknowledge cancellation
    if tasks_to_cancel:
        await asyncio.gather(*tasks_to_cancel, return_exceptions=True)

    # Nullify references to ensure idempotency
    indicator_task = None
    simulation_task = None

    # Clear in-memory state stores
    transcript_store.clear()
    conversation_manager.clear()
    
    # Reset simulation-specific state (e.g., turn counter in engine)
    from app.simulation import engine
    engine.turn_index = 0
    
    # Notify frontend to clear its state
    await manager.broadcast({"type": "clear_alerts"})
    await manager.broadcast({"type": "transcript_cleared"})
    
    logger.info("Session reset complete.")
    return {"status": "session reset"}


@router.get("/demos")
async def list_demos() -> List[Dict[str, str]]:
    """
    List all available demo scenarios.
    Returns a list of demo objects with id and name.
    """
    demos = []
    
    # Get the demos directory path
    demos_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
        'simulation', 'demos'
    )
    
    try:
        # Scan for JSON files in the demos directory
        if os.path.exists(demos_dir):
            for filename in os.listdir(demos_dir):
                if filename.endswith('.json'):
                    # Extract demo ID from filename
                    demo_id = filename[:-5]  # Remove .json extension
                    
                    # Try to read the demo name from the file
                    demo_path = os.path.join(demos_dir, filename)
                    try:
                        with open(demo_path, 'r') as f:
                            demo_data = json.load(f)
                            demo_name = demo_data.get('name', f'Demo: {demo_id}')
                            
                            demos.append({
                                "id": demo_id,
                                "name": demo_name
                            })
                    except (json.JSONDecodeError, IOError) as e:
                        logger.warning(f"Failed to read demo file {filename}: {str(e)}")
                        # Still include the demo with a fallback name
                        demos.append({
                            "id": demo_id,
                            "name": f"Demo: {demo_id}"
                        })
        
        # Sort demos by name for consistent ordering
        demos.sort(key=lambda x: x['name'])
        
    except OSError as e:
        logger.error(f"Failed to list demos directory: {str(e)}")
        # Return empty list on error
        
    return demos