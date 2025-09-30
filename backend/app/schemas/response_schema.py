from pydantic import BaseModel
from typing import Any, Optional, Dict
from datetime import datetime
import uuid


class HealthResponse(BaseModel):
    status: str
    timestamp: datetime
    version: str
    environment: str
    uptime: float


class MetaResponse(BaseModel):
    timestamp: datetime
    version: str = "1.0.0"
    request_id: str


class ErrorDetailResponse(BaseModel):
    code: str
    message: str
    details: Optional[Dict[str, Any]] = None


class ErrorResponse(BaseModel):
    error: ErrorDetailResponse
    meta: MetaResponse


class SuccessResponse(BaseModel):
    data: Any
    meta: MetaResponse


def create_success_response(data: Any, request_id: Optional[str] = None) -> SuccessResponse:
    """Create a standardized success response."""
    return SuccessResponse(
        data=data,
        meta=MetaResponse(
            timestamp=datetime.utcnow(),
            request_id=request_id or str(uuid.uuid4())
        )
    )


def create_error_response(
    code: str, 
    message: str, 
    details: Optional[Dict[str, Any]] = None,
    request_id: Optional[str] = None
) -> ErrorResponse:
    """Create a standardized error response."""
    return ErrorResponse(
        error=ErrorDetailResponse(
            code=code,
            message=message,
            details=details
        ),
        meta=MetaResponse(
            timestamp=datetime.utcnow(),
            request_id=request_id or str(uuid.uuid4())
        )
    )
