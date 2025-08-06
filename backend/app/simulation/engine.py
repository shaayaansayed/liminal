from datetime import datetime
from app.simulation.conversation import conversation_manager
from app.services.openai_service import OpenAIService
from app.simulation.agents import ALL_AGENTS, SimulatedAgent

# Create service instance
openai_service = OpenAIService()

# Module-level state for turn-taking
turn_index = 0


async def run_simulation_turn():
    """
    Orchestrates a single conversational turn in the simulation.
    
    Returns:
        tuple: (agent, text) - The agent who spoke and their message text.
               Returns (None, None) if no message was generated.
    """
    # Step 1: Select Speaker
    next_speaker = select_next_speaker()
    
    # Step 2: Construct Prompt
    # Get the conversation history as a formatted string
    conversation_history = conversation_manager.get_formatted_history()
    
    # Build the prompt using an f-string template
    llm_prompt = f"""You are {next_speaker['name']} and you are participating in a group therapy session. Your role is: {next_speaker['role']}. Here is the current conversation history:

<conversation_history>
{conversation_history}
</conversation_history>

It's your turn to speak. Generate your message. IMPORTANT: Keep your response concise, to a maximum of 3 sentences."""
    
    # Step 3: Generate Response
    response = await openai_service.generate_response(
        prompt=llm_prompt,
        temperature=next_speaker['temperature']
    )
    
    # Step 4: Validate & Update State
    if response:
        conversation_manager.add_message(
            participant_name=next_speaker['name'],
            text=response
        )
        
        # Return the agent and their message
        return next_speaker, response
    
    return None, None


def select_next_speaker() -> SimulatedAgent:
    """
    Gets the next agent to speak based on turn order.
    
    Returns:
        The SimulatedAgent object for the next speaker
    """
    global turn_index
    
    # Get the current agent
    current_agent = ALL_AGENTS[turn_index]
    
    # Increment turn index with wraparound
    turn_index = (turn_index + 1) % len(ALL_AGENTS)
    
    return current_agent