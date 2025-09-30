"""Response helper utilities."""

from datetime import datetime
from typing import Any, Optional, Dict
from app.models.response import SuccessResponse, ErrorResponse, ResponseMeta, ErrorDetail


class ResponseHelper:
    """Helper class for creating standardized API responses."""
    
    def create_success_response(
        self, 
        data: Any, 
        request_id: Optional[str] = None
    ) -> SuccessResponse:
        """Create a success response."""
        meta = self.create_meta(request_id)
        return SuccessResponse(data=data, meta=meta)
    
    def create_error_response(
        self,
        code: str,
        message: str,
        user_message: str,
        details: Optional[Dict[str, Any]] = None,
        request_id: Optional[str] = None
    ) -> ErrorResponse:
        """Create an error response."""
        meta = self.create_meta(request_id)
        error = ErrorDetail(
            code=code,
            message=message,
            user_message=user_message,
            details=details
        )
        return ErrorResponse(error=error, meta=meta)
    
    def create_meta(self, request_id: Optional[str] = None) -> ResponseMeta:
        """Create response metadata."""
        return ResponseMeta(
            timestamp=datetime.utcnow().isoformat(),
            version="1.0.0",
            request_id=request_id
        )
