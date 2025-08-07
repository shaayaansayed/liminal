"""
Main FastAPI application module.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.core.config import CORS_ORIGINS
from app.api.routes import session, webhooks, health, transcript
from app.api import websockets

# Create FastAPI app
app = FastAPI(
    title="Liminal Backend API",
    description="Behavioral Health Copilot Backend Service",
    version="1.0.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(health.router)
app.include_router(session.router)
app.include_router(webhooks.router)
app.include_router(transcript.router)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Add WebSocket endpoints
app.add_api_websocket_route("/ws/alerts", websockets.websocket_endpoint)
app.add_api_websocket_route("/ws/puppet/{token}", websockets.puppet_websocket_endpoint)