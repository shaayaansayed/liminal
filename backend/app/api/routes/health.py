"""
Health check endpoints.
"""
from datetime import datetime
from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/health")
async def health_check():
    """Check if the service is healthy."""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}