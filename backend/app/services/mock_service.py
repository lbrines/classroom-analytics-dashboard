"""Mock service for development and testing."""

import json
from pathlib import Path
from typing import List, Dict, Optional, Any
from app.models.user import User, UserRole


class MockService:
    """Mock service for handling mock data."""
    
    def __init__(self):
        """Initialize mock service."""
        self.mock_data_path = Path(__file__).parent.parent / "data" / "mock_users.json"
    
    def load_mock_users(self) -> List[Dict[str, Any]]:
        """Load mock users from JSON file."""
        try:
            with open(self.mock_data_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data.get("users", [])
        except (FileNotFoundError, json.JSONDecodeError) as e:
            # Return empty list if file doesn't exist or is invalid
            return []
    
    def get_user_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        """Get user by email."""
        users = self.load_mock_users()
        for user in users:
            if user.get("email") == email:
                return user
        return None
    
    def get_user_by_id(self, user_id: str) -> Optional[Dict[str, Any]]:
        """Get user by ID."""
        users = self.load_mock_users()
        for user in users:
            if user.get("id") == user_id:
                return user
        return None
    
    def verify_user_credentials(self, email: str, password: str) -> Optional[Dict[str, Any]]:
        """Verify user credentials."""
        user = self.get_user_by_email(email)
        if user and user.get("password") == password and user.get("active", False):
            return user
        return None
    
    def get_all_users(self) -> List[Dict[str, Any]]:
        """Get all users."""
        return self.load_mock_users()
    
    def get_users_by_role(self, role: str) -> List[Dict[str, Any]]:
        """Get users by role."""
        users = self.load_mock_users()
        return [user for user in users if user.get("role") == role]
