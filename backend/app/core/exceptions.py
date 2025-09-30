"""Custom exceptions for the application."""

from typing import Any, Dict, Optional


class BaseAPIException(Exception):
    """Base exception for API errors."""
    
    def __init__(
        self,
        code: str,
        message: str,
        user_message: str,
        details: Optional[Dict[str, Any]] = None,
        status_code: int = 500
    ):
        self.code = code
        self.message = message
        self.user_message = user_message
        self.details = details or {}
        self.status_code = status_code
        super().__init__(self.message)


class AuthenticationError(BaseAPIException):
    """Authentication related errors."""
    
    def __init__(
        self,
        message: str = "Authentication failed",
        user_message: str = "Invalid credentials",
        details: Optional[Dict[str, Any]] = None
    ):
        super().__init__(
            code="AUTH_ERROR",
            message=message,
            user_message=user_message,
            details=details,
            status_code=401
        )


class AuthorizationError(BaseAPIException):
    """Authorization related errors."""
    
    def __init__(
        self,
        message: str = "Authorization failed",
        user_message: str = "You don't have permission to access this resource",
        details: Optional[Dict[str, Any]] = None
    ):
        super().__init__(
            code="AUTHORIZATION_ERROR",
            message=message,
            user_message=user_message,
            details=details,
            status_code=403
        )


class ValidationError(BaseAPIException):
    """Validation related errors."""
    
    def __init__(
        self,
        message: str = "Validation failed",
        user_message: str = "Please check your input and try again",
        details: Optional[Dict[str, Any]] = None
    ):
        super().__init__(
            code="VALIDATION_ERROR",
            message=message,
            user_message=user_message,
            details=details,
            status_code=422
        )


class NotFoundError(BaseAPIException):
    """Resource not found errors."""
    
    def __init__(
        self,
        message: str = "Resource not found",
        user_message: str = "The requested resource was not found",
        details: Optional[Dict[str, Any]] = None
    ):
        super().__init__(
            code="NOT_FOUND",
            message=message,
            user_message=user_message,
            details=details,
            status_code=404
        )


class OAuthError(BaseAPIException):
    """OAuth related errors."""
    
    def __init__(
        self,
        message: str = "OAuth error",
        user_message: str = "Authentication with external provider failed",
        details: Optional[Dict[str, Any]] = None
    ):
        super().__init__(
            code="OAUTH_ERROR",
            message=message,
            user_message=user_message,
            details=details,
            status_code=400
        )
