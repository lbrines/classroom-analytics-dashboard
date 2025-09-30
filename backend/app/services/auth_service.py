"""Authentication service."""

from datetime import timedelta
from typing import Dict, Any, Optional
from app.services.mock_service import MockService
from app.core.security import verify_password, create_access_token, verify_token
from app.core.exceptions import AuthenticationError
from app.models.user import TokenData


class AuthService:
    """Service for handling authentication."""
    
    def __init__(self, mock_service: MockService):
        """Initialize auth service."""
        self.mock_service = mock_service
    
    def authenticate_user(self, email: str, password: str) -> Dict[str, Any]:
        """Authenticate user with email and password."""
        user = self.mock_service.verify_user_credentials(email, password)
        if not user:
            raise AuthenticationError(
                message="Invalid credentials",
                user_message="Invalid credentials",
                details={"email": "Invalid email or password"}
            )
        return user
    
    def create_access_token(self, user_data: Dict[str, Any]) -> str:
        """Create access token for user."""
        data = {
            "sub": user_data["id"],
            "email": user_data["email"],
            "role": user_data["role"]
        }
        return create_access_token(data)
    
    def verify_token(self, token: str) -> Optional[TokenData]:
        """Verify JWT token."""
        return verify_token(token)
    
    def get_current_user(self, token: str) -> Dict[str, Any]:
        """Get current user from token."""
        token_data = self.verify_token(token)
        if not token_data or not token_data.user_id:
            raise AuthenticationError(
                message="Invalid token",
                user_message="Invalid token"
            )
        
        user = self.mock_service.get_user_by_id(token_data.user_id)
        if not user:
            raise AuthenticationError(
                message="User not found",
                user_message="User not found"
            )
        
        return user
