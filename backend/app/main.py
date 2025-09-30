from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import time
import uuid
from app.api.router import api_router
from app.core.config import settings
from app.core.exceptions import EducationalDashboardException, create_http_exception

# Create FastAPI application
app = FastAPI(
    title="Educational Dashboard API",
    description="Backend API for Educational Dashboard - Stage 1",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.cors_origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add request ID middleware
@app.middleware("http")
async def add_request_id(request: Request, call_next):
    request_id = str(uuid.uuid4())
    request.state.request_id = request_id
    
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    
    response.headers["X-Process-Time"] = str(process_time)
    response.headers["X-Request-ID"] = request_id
    
    return response

# Global exception handler
@app.exception_handler(EducationalDashboardException)
async def custom_exception_handler(request: Request, exc: EducationalDashboardException):
    return JSONResponse(
        status_code=400,
        content={
            "error": {
                "code": exc.code,
                "message": exc.message,
                "details": exc.details
            },
            "meta": {
                "timestamp": time.time(),
                "version": "1.0.0",
                "request_id": getattr(request.state, "request_id", str(uuid.uuid4()))
            }
        }
    )

# Include API router
app.include_router(api_router, prefix="/api/v1")

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Educational Dashboard API",
        "version": "1.0.0",
        "status": "running",
        "docs": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=settings.port,
        reload=True if settings.environment == "development" else False
    )
