import httpx
import logging
import asyncio
import json
import os
from datetime import datetime, timezone
from collections import defaultdict
from typing import Callable, List

from app.core.config import RECALL_API_KEY, RECALL_REGION, RECALL_WEBHOOK_URL
from app.core.transcript import transcript_store
from app.api.websockets import manager
from app.services.conversation_event_service import conversation_event_service

logger = logging.getLogger(__name__)

# --- Callback Registry ---
# A dictionary to store lists of callback functions for each event type.
# e.g., {"transcript.data": [callback1, callback2]}
_event_callbacks: defaultdict[str, List[Callable]] = defaultdict(list)

def register_event_callback(event_type: str, callback: Callable):
    """Registers a function to be called when a specific event occurs."""
    logger.info(f"Registering callback for event type: {event_type}")
    _event_callbacks[event_type].append(callback)

def unregister_event_callback(event_type: str, callback: Callable):
    """Unregisters a specific callback function."""
    logger.info(f"Unregistering callback for event type: {event_type}")
    try:
        _event_callbacks[event_type].remove(callback)
    except ValueError:
        logger.warning(f"Attempted to unregister a callback that was not found for event: {event_type}")

# A base64 encoded silent MP3 file (required for audio output capability)
SILENT_MP3_B64 = "SUQzBAAAAAAB9AJhAAAAAAAAAAAAAAAAY29tbWVudABCaXRyYXRlVGFn"


async def create_bot(meeting_url: str):
    if not all([RECALL_API_KEY, RECALL_WEBHOOK_URL]):
        return {"error": "Missing required environment variables"}

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"https://{RECALL_REGION}.recall.ai/api/v1/bot/",
            headers={
                "Authorization": f"Token {RECALL_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "meeting_url": meeting_url,
                "bot_name": "Test Bot",
                # Add automatic_audio_output to enable audio playback
                "automatic_audio_output": {
                    "in_call_recording": {
                        "data": {
                            "kind": "mp3",
                            "b64_data": SILENT_MP3_B64,
                        }
                    }
                },
                "recording_config": {
                    "realtime_endpoints": [
                        {
                            "type": "webhook",
                            "url": RECALL_WEBHOOK_URL,
                            "events": [
                                "participant_events.join",
                                "participant_events.leave",
                                "transcript.data",
                                "transcript.partial_data",
                            ],
                        }
                    ],
                    "transcript": {
                        "provider": {"deepgram_streaming": {"diarize": "true"}}
                    },
                    "video_mixed_mp4": {},
                    "participant_events": {},
                    "meeting_metadata": {},
                },
            },
        )

        if response.status_code >= 400:
            logger.error(f"Recall API error creating bot: {response.status_code} - {response.text}")
            return {"error": f"Recall API error: {response.status_code}", "details": response.text}

        return response.json()


async def create_scribe_bot(meeting_url: str):
    """Creates a bot that only listens and sends webhooks."""
    if not all([RECALL_API_KEY, RECALL_WEBHOOK_URL]):
        return {"error": "Missing required environment variables"}

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"https://{RECALL_REGION}.recall.ai/api/v1/bot/",
            headers={"Authorization": f"Token {RECALL_API_KEY}", "Content-Type": "application/json"},
            json={
                "meeting_url": meeting_url,
                "bot_name": "Scribe Bot",
                "recording_config": {
                    "realtime_endpoints": [{
                        "type": "webhook",
                        "url": RECALL_WEBHOOK_URL,
                        "events": [
                            "participant_events.join", 
                            "transcript.data", 
                            "transcript.partial_data"
                        ],
                    }],
                    "transcript": {
                        "provider": {"deepgram_streaming": {"diarize": "true"}}
                    },
                },
            },
        )
        if response.status_code >= 400:
            logger.error(f"Recall API error creating scribe bot: {response.status_code} - {response.text}")
            return {"error": f"Recall API error: {response.status_code}", "details": response.text}
        return response.json()


async def create_speaker_bot(meeting_url: str, bot_name: str):
    """Creates a bot that can speak but does not send webhooks."""
    if not RECALL_API_KEY:
        return {"error": "Missing RECALL_API_KEY"}

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"https://{RECALL_REGION}.recall.ai/api/v1/bot/",
            headers={"Authorization": f"Token {RECALL_API_KEY}", "Content-Type": "application/json"},
            json={
                "meeting_url": meeting_url,
                "bot_name": bot_name,
                "automatic_audio_output": {
                    "in_call_recording": {"data": {"kind": "mp3", "b64_data": SILENT_MP3_B64}}
                },
            },
        )
        if response.status_code >= 400:
            logger.error(f"Recall API error creating speaker bot: {response.status_code} - {response.text}")
            return {"error": f"Recall API error: {response.status_code}", "details": response.text}
        return response.json()


async def send_audio_to_bot(bot_id: str, audio_data: str):
    """
    Sends base64-encoded MP3 audio data to a specific Recall bot to be played in the meeting.
    
    Args:
        bot_id: The ID of the bot to send audio to
        audio_data: Base64-encoded MP3 audio data
        
    Returns:
        Response from the Recall API or error dict
    """
    if not all([RECALL_API_KEY, bot_id, audio_data]):
        return {"error": "Missing bot_id, API key, or audio data"}

    url = f"https://{RECALL_REGION}.recall.ai/api/v1/bot/{bot_id}/output_audio/"
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            url,
            headers={
                "Authorization": f"Token {RECALL_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "b64_data": audio_data,
                "kind": "mp3"
            },
            timeout=30.0  # It might take a moment to stream audio
        )

        # Save audio file locally for inspection
        # save_dir = "speak_responses"
        # os.makedirs(save_dir, exist_ok=True)
        # timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
        # filename = f"audio_{timestamp}.mp3"
        # filepath = os.path.join(save_dir, filename)
        
        # # Decode base64 audio data and save as MP3 file
        # import base64
        # audio_bytes = base64.b64decode(audio_data)
        # with open(filepath, "wb") as f:
        #     f.write(audio_bytes)
        
        # logger.info(f"Saved audio file to {filepath}")

        if response.status_code >= 400:
            logger.error(f"Recall API error sending audio: {response.status_code} - {response.text}")
            return {"error": f"Recall API error sending audio: {response.status_code}", "details": response.text}
        
        return response.json()


def process_webhook(payload: dict):
    """
    Process webhook events from Recall.ai.
    This function is now a pure dispatcher.
    """
    event = payload.get("event")
    
    # Save payload to a file for inspection (good for debugging)
    # save_dir = "webhook_payloads"
    # os.makedirs(save_dir, exist_ok=True)
    # timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
    # filename = f"payload_{timestamp}.json"
    # filepath = os.path.join(save_dir, filename)
    # with open(filepath, "w") as f:
    #     json.dump(payload, f, indent=2)
    
    # --- 1. Dispatch to registered callbacks ---
    # The 'participant_events.join' logic will be handled here now
    if event in _event_callbacks:
        for callback in _event_callbacks[event]:
            try:
                callback(payload)
            except Exception as e:
                logger.error(f"Error executing callback for event {event}: {e}", exc_info=True)
    
    # --- 2. Dispatch to the main ConversationEventService ---
    if event in ["transcript.data", "transcript.partial_data"]:
        asyncio.create_task(
            conversation_event_service.handle_recall_transcript_data(payload)
        )
    
    # NOTE: The explicit 'participant_events.join' and 'leave' blocks are now gone.
    # They can be handled by callbacks if specific logic is needed.
