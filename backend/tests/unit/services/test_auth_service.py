import pytest
from app.services.auth_service import auth_service
from app.services.mock_service import mock_service
from app.core.exceptions import AuthenticationError


class TestAuthService:
    """Test cases for AuthService."""
    
    def test_authenticate_user_valid_credentials(self):
        """Test authentication with valid credentials."""
        user = auth_service.authenticate_user("admin@educational.dashboard", "admin123")
        assert user is not None
        assert user.email == "admin@educational.dashboard"
        assert user.role.value == "administrator"
    
    def test_authenticate_user_invalid_credentials(self):
        """Test authentication with invalid credentials."""
        user = auth_service.authenticate_user("admin@educational.dashboard", "wrongpassword")
        assert user is None
    
    def test_authenticate_user_nonexistent_user(self):
        """Test authentication with nonexistent user."""
        user = auth_service.authenticate_user("nonexistent@example.com", "password")
        assert user is None
    
    def test_create_token(self):
        """Test token creation."""
        user = mock_service.get_user_by_email("admin@educational.dashboard")
        assert user is not None
        
        token_data = auth_service.create_token(user)
        assert "access_token" in token_data
        assert token_data["token_type"] == "bearer"
        assert "expires_in" in token_data
        assert "user" in token_data
        assert token_data["user"]["email"] == user.email
    
    def test_get_user_from_token_valid(self):
        """Test getting user from valid token."""
        user = mock_service.get_user_by_email("admin@educational.dashboard")
        assert user is not None
        
        token_data = auth_service.create_token(user)
        token = token_data["access_token"]
        
        retrieved_user = auth_service.get_user_from_token(token)
        assert retrieved_user is not None
        assert retrieved_user.id == user.id
        assert retrieved_user.email == user.email
    
    def test_get_user_from_token_invalid(self):
        """Test getting user from invalid token."""
        user = auth_service.get_user_from_token("invalid_token")
        assert user is None
    
    def test_get_user_profile(self):
        """Test getting user profile."""
        user = mock_service.get_user_by_email("admin@educational.dashboard")
        assert user is not None
        
        profile = auth_service.get_user_profile(user.id)
        assert profile is not None
        assert profile.id == user.id
        assert profile.email == user.email
        assert profile.role == user.role
