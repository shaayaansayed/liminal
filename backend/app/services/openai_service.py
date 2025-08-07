"""
OpenAI Service Module
Handles all interactions with OpenAI APIs including LLM chat completions and TTS.
"""
import base64
import logging
from typing import Optional

import openai
from openai import AsyncOpenAI

from app.core.config import OPENAI_API_KEY

logger = logging.getLogger(__name__)


class OpenAIService:
    """Service class for all OpenAI API interactions."""
    
    def __init__(self):
        if not OPENAI_API_KEY:
            logger.warning("OPENAI_API_KEY is not set")
        self.client = AsyncOpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None
    
    async def generate_response(self, prompt: str, temperature: float = 0.7) -> str:
        """
        Generate a response from the LLM using the provided prompt.
        
        Args:
            prompt: The prompt string to send to the LLM
            temperature: Temperature parameter for the LLM (0.0 to 1.0)
        
        Returns:
            str: The generated response text, or empty string on failure
        """
        if not self.client:
            logger.error("OpenAI client not initialized")
            return ""
            
        try:
            # Wrap the prompt in the required message structure
            messages = [
                {'role': 'user', 'content': prompt}
            ]
            
            # Make the API call
            response = await self.client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                temperature=temperature
            )
            
            # Extract and return the response content
            return response.choices[0].message.content
            
        except openai.APIError as e:
            logger.error(f"OpenAI API error: {e}")
            return ""
        
        except openai.RateLimitError as e:
            logger.error(f"OpenAI rate limit error: {e}")
            return ""
        
        except Exception as e:
            logger.error(f"Unexpected error in generate_response: {e}")
            return ""
    
    async def generate_speech(self, text: str, voice: str = "alloy") -> Optional[str]:
        """
        Generates speech from text using OpenAI's TTS API and returns it as a base64 string.
        
        Args:
            text: The text to convert to speech
            voice: The TTS voice to use (e.g., "alloy", "nova", "fable")
            
        Returns:
            Base64-encoded MP3 audio string, or None if generation failed
        """
        if not self.client:
            logger.error("OpenAI client not initialized")
            return None

        try:
            response = await self.client.audio.speech.create(
                model="tts-1",
                voice=voice,
                input=text,
                response_format="mp3"
            )
            
            # Read the binary audio content and encode it in base64
            audio_content = await response.aread()
            base64_audio = base64.b64encode(audio_content).decode('utf-8')
            
            return base64_audio
        except Exception as e:
            logger.error(f"Error generating speech: {e}")
            return None

    async def generate_speech_stream(self, text: str, voice: str = "alloy"):
        """
        Generates speech from text using OpenAI's TTS API and yields audio chunks.
        
        Args:
            text: The text to convert to speech
            voice: The TTS voice to use (e.g., "alloy", "nova", "fable")
            
        Yields:
            bytes: Raw PCM audio chunks for streaming
        """
        if not self.client:
            logger.error("OpenAI client not initialized")
            return

        try:
            # Use PCM format for lower latency streaming
            response = await self.client.audio.speech.create(
                model="tts-1",
                voice=voice,
                input=text,
                response_format="pcm"  # 16-bit PCM at 24kHz
            )
            
            async for chunk in await response.aiter_bytes():
                yield chunk
                
        except Exception as e:
            logger.error(f"Error generating speech stream: {e}")


# Create a singleton instance
openai_service = OpenAIService()


# Backward compatibility functions
async def generate_response(prompt: str, temperature: float = 0.7) -> str:
    """Backward compatibility wrapper for generate_response."""
    return await openai_service.generate_response(prompt, temperature)


async def generate_speech(text: str, voice: str = "alloy") -> Optional[str]:
    """Backward compatibility wrapper for generate_speech."""
    return await openai_service.generate_speech(text, voice)