from pydantic import BaseModel
from typing import Optional, Any, Dict
from datetime import datetime
import uuid


class Meta(BaseModel):
    timestamp: datetime
    version: str = "1.0.0"
    request_id: str


class ErrorDetail(BaseModel):
    code: str
    message: str
    details: Optional[Dict[str, Any]] = None


class ErrorResponse(BaseModel):
    error: ErrorDetail
    meta: Meta


class SuccessResponse(BaseModel):
    data: Any
    meta: Meta


def create_success_response(data: Any, request_id: Optional[str] = None) -> SuccessResponse:
    """Create a standardized success response."""
    return SuccessResponse(
        data=data,
        meta=Meta(
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
        error=ErrorDetail(
            code=code,
            message=message,
            details=details
        ),
        meta=Meta(
            timestamp=datetime.utcnow(),
            request_id=request_id or str(uuid.uuid4())
        )
    )
