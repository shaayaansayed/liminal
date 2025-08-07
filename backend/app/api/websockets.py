import json
import logging
import asyncio
from typing import Dict
from fastapi import WebSocket, WebSocketDisconnect

logger = logging.getLogger(__name__)

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)

    async def broadcast(self, data: dict):
        message = json.dumps(data)
        for connection in self.active_connections[:]:
            try:
                await connection.send_text(message)
            except:
                self.disconnect(connection)

manager = ConnectionManager()


# --- NEW PUPPET CONNECTION MANAGER ---
class PuppetConnectionManager:
    def __init__(self):
        # This dictionary holds active connections, mapping unique token to WebSocket
        self.active_puppets: Dict[str, WebSocket] = {}
        # Dictionary to track connection events for synchronization
        self.connection_events: Dict[str, asyncio.Event] = {}

    def set_event_dict(self, event_dict: Dict[str, asyncio.Event]):
        """Set the event dictionary for synchronization with the runner."""
        self.connection_events = event_dict

    async def connect(self, websocket: WebSocket, token: str):
        await websocket.accept()
        self.active_puppets[token] = websocket
        logger.info(f"Puppet connected with token: {token}")
        
        # Signal that this puppet has connected
        if token in self.connection_events:
            self.connection_events[token].set()
            logger.info(f"Signaled connection event for token: {token}")

    def disconnect(self, token: str):
        if token in self.active_puppets:
            del self.active_puppets[token]
            logger.info(f"Puppet disconnected with token: {token}")

    async def send_audio(self, token: str, audio_chunk: bytes):
        websocket = self.active_puppets.get(token)
        if websocket:
            try:
                # Send raw bytes for audio streaming
                await websocket.send_bytes(audio_chunk)
            except WebSocketDisconnect:
                self.disconnect(token)
            except Exception as e:
                logger.error(f"Error sending audio to puppet {token}: {e}")
                self.disconnect(token)

    async def send_message(self, token: str, message: dict):
        websocket = self.active_puppets.get(token)
        if websocket:
            try:
                await websocket.send_text(json.dumps(message))
            except WebSocketDisconnect:
                self.disconnect(token)
            except Exception as e:
                logger.error(f"Error sending message to puppet {token}: {e}")
                self.disconnect(token)


# Create a singleton instance for the entire application
puppet_manager = PuppetConnectionManager()


async def puppet_websocket_endpoint(websocket: WebSocket, token: str):
    """WebSocket endpoint for audio puppets."""
    await puppet_manager.connect(websocket, token)
    try:
        while True:
            # Keep connection alive, listen for any messages (e.g., ping/pong)
            message = await websocket.receive_text()
            # Handle ping messages to keep connection alive
            try:
                data = json.loads(message)
                if data.get('type') == 'ping':
                    await puppet_manager.send_message(token, {'type': 'pong'})
            except json.JSONDecodeError:
                pass
    except WebSocketDisconnect:
        puppet_manager.disconnect(token)


async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint for real-time alerts."""
    await manager.connect(websocket)
    try:
        while True:
            # Keep connection alive
            await websocket.receive_text()
    except:
        manager.disconnect(websocket)