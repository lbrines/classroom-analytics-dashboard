import time
from fastapi import APIRouter
from app.schemas.response_schema import create_success_response
from app.core.config import settings

router = APIRouter()

# Store start time for uptime calculation
start_time = time.time()


@router.get("/health")
async def health_check():
    """Health check endpoint."""
    uptime = time.time() - start_time
    
    health_data = {
        "status": "healthy",
        "timestamp": time.time(),
        "version": "1.0.0",
        "environment": settings.environment,
        "uptime": round(uptime, 2)
    }
    
    return create_success_response(health_data).model_dump()
