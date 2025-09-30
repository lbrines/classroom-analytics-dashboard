"""Response models for API envelope."""

from typing import Any, Dict, Optional
from pydantic import BaseModel
from datetime import datetime


class ResponseMeta(BaseModel):
    """Response metadata."""
    timestamp: str
    version: str = "1.0.0"
    request_id: Optional[str] = None


class ErrorDetail(BaseModel):
    """Error detail model."""
    code: str
    message: str
    user_message: str
    details: Optional[Dict[str, Any]] = None


class APIResponse(BaseModel):
    """Standard API response envelope."""
    data: Optional[Any] = None
    meta: ResponseMeta
    error: Optional[ErrorDetail] = None


class SuccessResponse(BaseModel):
    """Success response model."""
    data: Any
    meta: ResponseMeta


class ErrorResponse(BaseModel):
    """Error response model."""
    error: ErrorDetail
    meta: ResponseMeta
