"""
Demo Turn Provider for pre-scripted conversation scenarios.
This module provides a turn-by-turn interface to demo scripts,
compatible with both text and zoom simulation runners.
"""
import asyncio
import json
import logging
import os
from typing import Optional, Tuple, List, Dict, Any
from app.simulation.agents import SimulatedAgent, ALL_AGENTS

logger = logging.getLogger(__name__)


class DemoTurnProvider:
    """Provides conversation turns from a pre-written demo script."""
    
    def __init__(self, demo_id: str):
        self.demo_id = demo_id
        self.script: List[Dict[str, Any]] = []
        self.current_index = 0
        self.agent_map: Dict[str, SimulatedAgent] = {agent['name']: agent for agent in ALL_AGENTS}
        self._load_script()
    
    def _load_script(self) -> None:
        """Load the demo script from JSON file."""
        try:
            # Construct path relative to this file's location
            script_path = os.path.join(
                os.path.dirname(__file__), 'demos', f'{self.demo_id}.json'
            )
            with open(script_path, 'r') as f:
                demo_data = json.load(f)
            self.script = demo_data.get("script", [])
            logger.info(f"Loaded demo script: {demo_data.get('name')} with {len(self.script)} turns")
        except FileNotFoundError:
            logger.error(f"Demo script not found: {self.demo_id}.json")
            self.script = []
        except json.JSONDecodeError:
            logger.error(f"Failed to parse demo script: {self.demo_id}.json")
            self.script = []
    
    async def get_next_turn(self) -> Tuple[Optional[SimulatedAgent], Optional[str]]:
        """
        Get the next turn from the demo script.
        Returns (agent, text) tuple, or (None, None) if script is finished.
        This method signature matches engine.run_simulation_turn() for compatibility.
        """
        # Check if we've reached the end of the script
        if self.current_index >= len(self.script):
            logger.info(f"Demo '{self.demo_id}' finished - all turns completed")
            return None, None
        
        # Get the current utterance
        utterance = self.script[self.current_index]
        self.current_index += 1
        
        # Extract turn data
        delay = utterance.get("delay_seconds", 3.0)
        participant_name = utterance.get("participant_name")
        text = utterance.get("text")
        
        # Wait for the specified delay
        await asyncio.sleep(delay)
        
        # Validate utterance data
        if not participant_name or not text:
            logger.warning(f"Invalid utterance at index {self.current_index - 1}: missing participant_name or text")
            # Recursively try the next turn
            return await self.get_next_turn()
        
        # Find the corresponding agent
        agent = self.agent_map.get(participant_name)
        if not agent:
            logger.warning(f"Agent '{participant_name}' not found in ALL_AGENTS. Skipping utterance.")
            # Recursively try the next turn
            return await self.get_next_turn()
        
        logger.info(f"Demo turn {self.current_index}/{len(self.script)}: {agent['name']} speaking")
        return agent, text
    
    def reset(self) -> None:
        """Reset the provider to start from the beginning of the script."""
        self.current_index = 0
        logger.info(f"Demo provider reset for '{self.demo_id}'")