from fastapi import APIRouter
from app.api.endpoints import auth, oauth, health, courses, students, dashboard, search, notifications

# Create main API router
api_router = APIRouter()

# Include endpoint routers
api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(oauth.router, prefix="/oauth", tags=["oauth"])
api_router.include_router(courses.router, tags=["courses"])
api_router.include_router(students.router, tags=["students"])
api_router.include_router(dashboard.router, tags=["metrics"])
api_router.include_router(search.router, tags=["search"])
api_router.include_router(notifications.router, tags=["notifications"])
