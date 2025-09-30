from datetime import datetime, timedelta
from typing import Optional, Dict, Any
from app.core.security import verify_password, create_access_token, parse_expiration_time
from app.core.config import settings
from app.services.mock_service import mock_service
from app.models.user import UserInDB, User
from app.core.exceptions import AuthenticationError


class AuthService:
    """Service for handling authentication operations."""
    
    def authenticate_user(self, email: str, password: str) -> Optional[UserInDB]:
        """Authenticate a user with email and password."""
        user = mock_service.get_user_by_email(email)
        if not user:
            return None
        
        if not user.active:
            raise AuthenticationError("User account is disabled")
        
        if not verify_password(password, user.password_hash):
            return None
        
        return user
    
    def create_token(self, user: UserInDB) -> Dict[str, Any]:
        """Create access token for user."""
        expires_delta = parse_expiration_time(settings.jwt_expires_in)
        access_token = create_access_token(
            data={"sub": user.id, "email": user.email, "role": user.role.value},
            expires_delta=expires_delta
        )
        
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "expires_in": int(expires_delta.total_seconds()),
            "user": {
                "id": user.id,
                "email": user.email,
                "name": user.name,
                "role": user.role.value,
                "active": user.active
            }
        }
    
    def get_user_from_token(self, token: str) -> Optional[UserInDB]:
        """Get user from JWT token."""
        from app.core.security import verify_token
        
        payload = verify_token(token)
        if not payload:
            return None
        
        user_id = payload.get("sub")
        if not user_id:
            return None
        
        return mock_service.get_user_by_id(user_id)
    
    def refresh_token(self, token: str) -> Optional[Dict[str, Any]]:
        """Refresh access token."""
        user = self.get_user_from_token(token)
        if not user:
            return None
        
        return self.create_token(user)
    
    def logout_user(self, token: str) -> bool:
        """Logout user (invalidate token)."""
        # In a real implementation, this would add token to blacklist
        # For now, we just verify the token exists
        user = self.get_user_from_token(token)
        return user is not None
    
    def get_user_profile(self, user_id: str) -> Optional[User]:
        """Get user profile by ID."""
        user_in_db = mock_service.get_user_by_id(user_id)
        if not user_in_db:
            return None
        
        return User(
            id=user_in_db.id,
            email=user_in_db.email,
            name=user_in_db.name,
            role=user_in_db.role,
            active=user_in_db.active,
            created_at=user_in_db.created_at,
            updated_at=user_in_db.updated_at
        )


# Global instance
auth_service = AuthService()
