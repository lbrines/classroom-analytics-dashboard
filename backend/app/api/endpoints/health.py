"""Health check endpoint."""

from datetime import datetime
from fastapi import APIRouter
from app.utils.response_helper import ResponseHelper

router = APIRouter()
response_helper = ResponseHelper()


@router.get("/")
async def health_check():
    """Health check endpoint."""
    data = {
        "status": "healthy",
        "message": "Service is running",
        "timestamp": datetime.utcnow().isoformat()
    }
    
    response = response_helper.create_success_response(data)
    return response.model_dump()
