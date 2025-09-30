"""API router configuration."""

from fastapi import APIRouter
from app.api.endpoints import auth, health

api_router = APIRouter()

# Include endpoint routers
api_router.include_router(health.router, prefix="/api/v1/health", tags=["health"])
api_router.include_router(auth.router, prefix="/api/v1/auth", tags=["authentication"])
