"""Main FastAPI application."""

from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.api.router import api_router
from app.core.config import settings
from app.core.exceptions import BaseAPIException
from app.utils.response_helper import ResponseHelper
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Educational Dashboard API",
    description="API for Educational Dashboard Management System",
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

# Include API routes
app.include_router(api_router)

# Initialize response helper
response_helper = ResponseHelper()


@app.exception_handler(BaseAPIException)
async def api_exception_handler(request: Request, exc: BaseAPIException):
    """Handle custom API exceptions."""
    logger.error(f"API Exception: {exc.code} - {exc.message}")
    
    error_response = response_helper.create_error_response(
        code=exc.code,
        message=exc.message,
        user_message=exc.user_message,
        details=exc.details,
        request_id=getattr(request.state, 'request_id', None)
    )
    
    return JSONResponse(
        status_code=exc.status_code,
        content=error_response.model_dump()
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """Handle HTTP exceptions."""
    logger.error(f"HTTP Exception: {exc.status_code} - {exc.detail}")
    
    error_response = response_helper.create_error_response(
        code=f"HTTP_{exc.status_code}",
        message=str(exc.detail),
        user_message="An error occurred while processing your request",
        details={},
        request_id=getattr(request.state, 'request_id', None)
    )
    
    return JSONResponse(
        status_code=exc.status_code,
        content=error_response.model_dump()
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    """Handle general exceptions."""
    logger.error(f"General Exception: {str(exc)}", exc_info=True)
    
    error_response = response_helper.create_error_response(
        code="INTERNAL_SERVER_ERROR",
        message="An internal server error occurred",
        user_message="Something went wrong. Please try again later.",
        details={},
        request_id=getattr(request.state, 'request_id', None)
    )
    
    return JSONResponse(
        status_code=500,
        content=error_response.model_dump()
    )


@app.get("/")
async def root():
    """Root endpoint."""
    response = response_helper.create_success_response({
        "message": "Educational Dashboard API",
        "version": "1.0.0",
        "status": "running"
    })
    return response.model_dump()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=settings.port,
        reload=True if settings.environment == "development" else False
    )
