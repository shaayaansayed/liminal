from typing import List, Dict


class ConversationManager:
    """Manages the message history for conversations."""
    
    def __init__(self):
        self.history: List[Dict[str, str]] = []
    
    def add_message(self, participant_name: str, text: str) -> None:
        """
        Appends a new message to the conversation history.
        
        Args:
            participant_name: Name of the participant sending the message
            text: The message content
        """
        message = {
            'role': 'assistant',
            'name': participant_name,
            'content': text
        }
        self.history.append(message)
    
    def get_formatted_history(self, last_n: int = 15) -> str:
        """
        Returns the last n messages from the conversation history as a formatted string.
        
        Args:
            last_n: Number of recent messages to return (default: 15)
            
        Returns:
            A formatted string of the conversation history
        """
        recent_messages = self.history[-last_n:] if self.history else []
        
        # Format each message as "Name: Content"
        formatted_messages = []
        for message in recent_messages:
            name = message.get('name', 'Unknown')
            content = message['content']
            formatted_messages.append(f"{name}: {content}")
        
        # Join all messages with newlines
        return '\n'.join(formatted_messages)
    
    def clear(self) -> None:
        """Resets the conversation history."""
        self.history = []


# Create singleton instance
conversation_manager = ConversationManager()