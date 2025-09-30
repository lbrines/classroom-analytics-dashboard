from typing import Any, Optional, Dict
from datetime import datetime
import uuid
from app.schemas.response_schema import create_success_response, create_error_response


def success_response(data: Any, request_id: Optional[str] = None) -> Dict[str, Any]:
    """Create a standardized success response."""
    return create_success_response(data, request_id).dict()


def error_response(
    code: str, 
    message: str, 
    details: Optional[Dict[str, Any]] = None,
    request_id: Optional[str] = None
) -> Dict[str, Any]:
    """Create a standardized error response."""
    return create_error_response(code, message, details, request_id).dict()


def validation_error_response(
    message: str = "Validation failed",
    details: Optional[Dict[str, Any]] = None,
    request_id: Optional[str] = None
) -> Dict[str, Any]:
    """Create a validation error response."""
    return error_response("VALIDATION_ERROR", message, details, request_id)


def not_found_error_response(
    message: str = "Resource not found",
    details: Optional[Dict[str, Any]] = None,
    request_id: Optional[str] = None
) -> Dict[str, Any]:
    """Create a not found error response."""
    return error_response("NOT_FOUND", message, details, request_id)


def authentication_error_response(
    message: str = "Authentication failed",
    details: Optional[Dict[str, Any]] = None,
    request_id: Optional[str] = None
) -> Dict[str, Any]:
    """Create an authentication error response."""
    return error_response("AUTH_ERROR", message, details, request_id)


def authorization_error_response(
    message: str = "Access denied",
    details: Optional[Dict[str, Any]] = None,
    request_id: Optional[str] = None
) -> Dict[str, Any]:
    """Create an authorization error response."""
    return error_response("AUTHZ_ERROR", message, details, request_id)
