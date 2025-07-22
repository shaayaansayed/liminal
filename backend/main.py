import asyncio
import json
import logging
import os
from datetime import datetime, timedelta
from typing import Dict, List

import dotenv
import httpx
from fastapi import FastAPI, HTTPException, Request, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

dotenv.load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

participant_speaking_times: Dict[str, Dict] = {}


class ConnectionManager:
    """Manages WebSocket connections for real-time alerts"""

    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def send_message(self, message: str):
        """Send message to all connected clients"""
        for connection in self.active_connections[:]:
            try:
                await connection.send_text(message)
            except Exception:
                # Connection is broken, explicitly disconnect it
                self.disconnect(connection)


manager = ConnectionManager()


async def check_participant_silence():
    """Check all participants for 60+ second silence and send WebSocket alerts"""
    current_time = datetime.now()
    silence_threshold = timedelta(seconds=60)

    for participant_id, participant_data in participant_speaking_times.items():
        last_spoke = participant_data["timestamp"]
        participant_name = participant_data["name"]
        time_since_spoke = current_time - last_spoke

        if time_since_spoke >= silence_threshold:
            silent_duration = int(time_since_spoke.total_seconds())

            # Create silence alert message
            alert_message = {
                "type": "silence_alert",
                "participant": participant_name,
                "participant_id": participant_id,
                "silent_duration": silent_duration,
                "timestamp": current_time.isoformat(),
            }

            logger.warning(
                f"🔇 SILENCE DETECTED: {participant_name} ({participant_id}) hasn't spoken for {silent_duration} seconds"
            )

            # Send alert via WebSocket
            await manager.send_message(json.dumps(alert_message))


async def silence_monitoring_task():
    """Background task that runs every 10 seconds to check for participant silence"""
    while True:
        try:
            await check_participant_silence()
            await asyncio.sleep(10)  # Check every 10 seconds
        except Exception as e:
            logger.error(f"Error in silence monitoring task: {e}")
            await asyncio.sleep(10)  # Continue even if there's an error


app = FastAPI(
    title="Simple Backend API",
    description="A simple FastAPI backend deployed on ECS",
    version="1.0.0",
)

RECALL_API_KEY = os.getenv("RECALL_API_KEY")
RECALL_REGION = os.getenv("RECALL_REGION", "us-west-2")
RECALL_WEBHOOK_URL = os.getenv("RECALL_WEBHOOK_URL")

# Add CORS middleware to allow frontend calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # React dev server
        "http://localhost:5173",
        "*",
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    """Start background tasks when the app starts"""
    logger.info("🚀 Starting silence monitoring background task")
    asyncio.create_task(silence_monitoring_task())


@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}


@app.post("/api/create-bot")
async def create_bot(request: dict):
    meeting_url = request.get("meeting_url")

    if not meeting_url:
        return {"error": "meeting_url is required"}

    if not RECALL_API_KEY:
        return {"error": "RECALL_API_KEY environment variable not set"}

    if not RECALL_WEBHOOK_URL:
        return {"error": "RECALL_WEBHOOK_URL environment variable not set"}

    # Correct payload structure based on API documentation
    bot_payload = {
        "meeting_url": meeting_url,
        "bot_name": "Test Bot",
        "recording_config": {
            # Realtime endpoints go at the top level of recording_config
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
            # Configure transcript with a provider for real-time transcription
            "transcript": {"provider": {"deepgram_streaming": {"diarize": "true"}}},
            # Enable basic recording features
            "video_mixed_mp4": {},
            "participant_events": {},
            "meeting_metadata": {},
        },
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"https://{RECALL_REGION}.recall.ai/api/v1/bot/",
                headers={
                    "Authorization": f"Token {RECALL_API_KEY}",
                    "Content-Type": "application/json",
                },
                json=bot_payload,
            )

            if response.status_code >= 400:
                return {"error": f"Recall API error: {response.status_code}"}

            return response.json()

    except Exception as e:
        logger.error(f"Bot creation failed: {e}")
        return {"error": "Failed to connect to Recall API"}


def update_participant_speaking_time(
    participant_id: str, participant_name: str = "Unknown"
):
    """Update the last spoken timestamp and name for a participant"""
    current_time = datetime.now()
    participant_speaking_times[participant_id] = {
        "timestamp": current_time,
        "name": participant_name,
    }


@app.post("/webhooks/recall")
async def handle_recall_webhook(request: Request):
    """Handle incoming webhooks from Recall API - Track participant speaking times"""
    try:
        body = await request.body()
        payload = json.loads(body)
        event_type = payload.get("event")

        # Handle both transcript.data and transcript.partial_data events
        if event_type in ["transcript.data", "transcript.partial_data"]:
            transcript_data = payload.get("data", {}).get("data", {})
            words = transcript_data.get("words", [])
            participant = transcript_data.get("participant", {})

            if words and participant.get("id"):
                update_participant_speaking_time(
                    participant["id"], participant.get("name", "Unknown")
                )

        return {"status": "success"}

    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON")
    except Exception as e:
        logger.error(f"Error processing webhook: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@app.websocket("/ws/alerts")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for real-time alerts"""
    await manager.connect(websocket)

    try:
        while True:
            # Keep the connection alive
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)
