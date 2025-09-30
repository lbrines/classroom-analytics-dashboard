from fastapi import HTTPException, status
from typing import Optional, Dict, Any


class EducationalDashboardException(Exception):
    """Base exception for Educational Dashboard."""
    
    def __init__(self, message: str, code: str = "GENERIC_ERROR", details: Optional[Dict[str, Any]] = None):
        self.message = message
        self.code = code
        self.details = details or {}
        super().__init__(self.message)


class AuthenticationError(EducationalDashboardException):
    """Authentication related errors."""
    
    def __init__(self, message: str = "Authentication failed", details: Optional[Dict[str, Any]] = None):
        super().__init__(message, "AUTH_ERROR", details)


class AuthorizationError(EducationalDashboardException):
    """Authorization related errors."""
    
    def __init__(self, message: str = "Access denied", details: Optional[Dict[str, Any]] = None):
        super().__init__(message, "AUTHZ_ERROR", details)


class ValidationError(EducationalDashboardException):
    """Validation related errors."""
    
    def __init__(self, message: str = "Validation failed", details: Optional[Dict[str, Any]] = None):
        super().__init__(message, "VALIDATION_ERROR", details)


class NotFoundError(EducationalDashboardException):
    """Resource not found errors."""
    
    def __init__(self, message: str = "Resource not found", details: Optional[Dict[str, Any]] = None):
        super().__init__(message, "NOT_FOUND", details)


def create_http_exception(exception: EducationalDashboardException) -> HTTPException:
    """Convert custom exception to HTTPException."""
    status_code_map = {
        "AUTH_ERROR": status.HTTP_401_UNAUTHORIZED,
        "AUTHZ_ERROR": status.HTTP_403_FORBIDDEN,
        "VALIDATION_ERROR": status.HTTP_422_UNPROCESSABLE_ENTITY,
        "NOT_FOUND": status.HTTP_404_NOT_FOUND,
    }
    
    status_code = status_code_map.get(exception.code, status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return HTTPException(
        status_code=status_code,
        detail={
            "error": {
                "code": exception.code,
                "message": exception.message,
                "details": exception.details
            }
        }
    )
