"""
Transcript management endpoints.
"""
from fastapi import APIRouter

from app.core.transcript import transcript_store

router = APIRouter(prefix="/api", tags=["transcript"])


@router.get("/transcript")
async def get_transcript(format: str = "json", last_seconds: float = None):
    """Get the current transcript
    
    Args:
        format: "json" for structured data or "text" for formatted text
        last_seconds: If provided, only return transcript from last N seconds
    """
    if last_seconds:
        transcript_data = transcript_store.get_last_n_seconds(last_seconds)
    else:
        transcript_data = transcript_store.get_full_transcript()
    
    if format == "text":
        return {
            "transcript": transcript_store.get_formatted_transcript(),
            "segment_count": len(transcript_data),
        }
    else:
        return {"transcript": transcript_data, "segment_count": len(transcript_data)}


@router.get("/transcript/latest")
async def get_latest_transcript(seconds: float = 30):
    """Get transcript from the last N seconds (default: 30)"""
    transcript_data = transcript_store.get_last_n_seconds(seconds)
    return {
        "transcript": transcript_data,
        "seconds": seconds,
        "segment_count": len(transcript_data),
    }