"""
Webhook endpoints for external services.
"""
from fastapi import APIRouter, Request

from app.services.recall_service import process_webhook

router = APIRouter(tags=["webhooks"])


@router.post("/webhooks/recall")
async def handle_recall_webhook(request: Request):
    """Handle webhooks from Recall.ai service."""
    try:
        payload = await request.json()
        process_webhook(payload)
        return {"status": "success"}
    except Exception as e:
        # Log the error so it's visible in backend logs
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Failed to process webhook: {str(e)}", exc_info=True)
        return {"error": f"Failed to process webhook: {str(e)}"}