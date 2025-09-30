import json
import os
from typing import List, Optional, Dict, Any
from app.models.user import User, UserInDB, UserRole
from app.models.oauth_token import OAuthToken, OAuthTokenInDB
from app.core.security import get_password_hash


class MockService:
    """Service for managing mock data."""
    
    def __init__(self):
        self.data_file = os.path.join(os.path.dirname(__file__), "..", "data", "mock_users.json")
        self._data = None
    
    def _load_data(self) -> Dict[str, Any]:
        """Load mock data from JSON file."""
        if self._data is None:
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    self._data = json.load(f)
            except FileNotFoundError:
                self._data = {"users": [], "oauth_tokens": []}
        return self._data
    
    def get_user_by_email(self, email: str) -> Optional[UserInDB]:
        """Get user by email."""
        data = self._load_data()
        for user_data in data.get("users", []):
            if user_data["email"] == email:
                return UserInDB(
                    id=user_data["id"],
                    email=user_data["email"],
                    name=user_data["name"],
                    role=UserRole(user_data["role"]),
                    active=user_data["active"],
                    password_hash=get_password_hash(user_data["password"]),
                    created_at=user_data["created_at"],
                    updated_at=user_data["updated_at"]
                )
        return None
    
    def get_user_by_id(self, user_id: str) -> Optional[UserInDB]:
        """Get user by ID."""
        data = self._load_data()
        for user_data in data.get("users", []):
            if user_data["id"] == user_id:
                return UserInDB(
                    id=user_data["id"],
                    email=user_data["email"],
                    name=user_data["name"],
                    role=UserRole(user_data["role"]),
                    active=user_data["active"],
                    password_hash=get_password_hash(user_data["password"]),
                    created_at=user_data["created_at"],
                    updated_at=user_data["updated_at"]
                )
        return None
    
    def get_all_users(self) -> List[UserInDB]:
        """Get all users."""
        data = self._load_data()
        users = []
        for user_data in data.get("users", []):
            users.append(UserInDB(
                id=user_data["id"],
                email=user_data["email"],
                name=user_data["name"],
                role=UserRole(user_data["role"]),
                active=user_data["active"],
                password_hash=get_password_hash(user_data["password"]),
                created_at=user_data["created_at"],
                updated_at=user_data["updated_at"]
            ))
        return users
    
    def get_users_by_role(self, role: UserRole) -> List[UserInDB]:
        """Get users by role."""
        all_users = self.get_all_users()
        return [user for user in all_users if user.role == role]
    
    def get_oauth_token_by_user(self, user_id: str, provider: str = "google") -> Optional[OAuthTokenInDB]:
        """Get OAuth token by user ID and provider."""
        data = self._load_data()
        for token_data in data.get("oauth_tokens", []):
            if token_data["user_id"] == user_id and token_data["provider"] == provider:
                return OAuthTokenInDB(
                    id=token_data["id"],
                    user_id=token_data["user_id"],
                    provider=token_data["provider"],
                    access_token=token_data["access_token"],
                    refresh_token=token_data.get("refresh_token"),
                    expires_at=token_data["expires_at"],
                    scope=token_data["scope"],
                    created_at=token_data["created_at"],
                    updated_at=token_data["updated_at"]
                )
        return None
    
    def save_oauth_token(self, token_data: Dict[str, Any]) -> OAuthTokenInDB:
        """Save OAuth token (mock implementation - just returns the data)."""
        # In a real implementation, this would save to database
        return OAuthTokenInDB(
            id=token_data.get("id", "mock-oauth-token"),
            user_id=token_data["user_id"],
            provider=token_data["provider"],
            access_token=token_data["access_token"],
            refresh_token=token_data.get("refresh_token"),
            expires_at=token_data["expires_at"],
            scope=token_data["scope"],
            created_at=token_data.get("created_at", "2025-09-30T10:00:00Z"),
            updated_at=token_data.get("updated_at", "2025-09-30T10:00:00Z")
        )
    
    def delete_oauth_token(self, user_id: str, provider: str = "google") -> bool:
        """Delete OAuth token (mock implementation)."""
        # In a real implementation, this would delete from database
        return True


# Global instance
mock_service = MockService()
