"""Tests for auth service."""

import pytest
from datetime import timedelta
from app.services.auth_service import AuthService
from app.services.mock_service import MockService
from app.core.exceptions import AuthenticationError


class TestAuthService:
    """Test cases for AuthService."""
    
    @pytest.fixture
    def mock_service(self):
        """Create MockService instance for testing."""
        return MockService()
    
    @pytest.fixture
    def auth_service(self, mock_service):
        """Create AuthService instance for testing."""
        return AuthService(mock_service)
    
    def test_authenticate_user_success(self, auth_service):
        """Test successful user authentication."""
        # Arrange
        email = "admin@educational.dashboard"
        password = "admin123"
        
        # Act
        result = auth_service.authenticate_user(email, password)
        
        # Assert
        assert result is not None
        assert result["email"] == email
        assert result["role"] == "admin"
    
    def test_authenticate_user_invalid_credentials(self, auth_service):
        """Test authentication with invalid credentials."""
        # Arrange
        email = "admin@educational.dashboard"
        wrong_password = "wrongpassword"
        
        # Act & Assert
        with pytest.raises(AuthenticationError) as exc_info:
            auth_service.authenticate_user(email, wrong_password)
        
        assert exc_info.value.code == "AUTH_ERROR"
        assert "Invalid credentials" in exc_info.value.user_message
    
    def test_authenticate_user_nonexistent_user(self, auth_service):
        """Test authentication with non-existent user."""
        # Arrange
        email = "nonexistent@example.com"
        password = "password123"
        
        # Act & Assert
        with pytest.raises(AuthenticationError) as exc_info:
            auth_service.authenticate_user(email, password)
        
        assert exc_info.value.code == "AUTH_ERROR"
        assert "Invalid credentials" in exc_info.value.user_message
    
    def test_create_access_token(self, auth_service):
        """Test access token creation."""
        # Arrange
        user_data = {
            "id": "admin-001",
            "email": "admin@educational.dashboard",
            "role": "admin"
        }
        
        # Act
        token = auth_service.create_access_token(user_data)
        
        # Assert
        assert isinstance(token, str)
        assert len(token) > 0
    
    def test_verify_token_valid(self, auth_service):
        """Test token verification with valid token."""
        # Arrange
        user_data = {
            "id": "admin-001",
            "email": "admin@educational.dashboard",
            "role": "admin"
        }
        token = auth_service.create_access_token(user_data)
        
        # Act
        token_data = auth_service.verify_token(token)
        
        # Assert
        assert token_data is not None
        assert token_data.user_id == "admin-001"
        assert token_data.email == "admin@educational.dashboard"
    
    def test_verify_token_invalid(self, auth_service):
        """Test token verification with invalid token."""
        # Arrange
        invalid_token = "invalid.token.here"
        
        # Act
        token_data = auth_service.verify_token(invalid_token)
        
        # Assert
        assert token_data is None
    
    def test_get_current_user_valid_token(self, auth_service):
        """Test getting current user with valid token."""
        # Arrange
        user_data = {
            "id": "admin-001",
            "email": "admin@educational.dashboard",
            "role": "admin"
        }
        token = auth_service.create_access_token(user_data)
        
        # Act
        current_user = auth_service.get_current_user(token)
        
        # Assert
        assert current_user is not None
        assert current_user["id"] == "admin-001"
        assert current_user["email"] == "admin@educational.dashboard"
        assert current_user["role"] == "admin"
    
    def test_get_current_user_invalid_token(self, auth_service):
        """Test getting current user with invalid token."""
        # Arrange
        invalid_token = "invalid.token.here"
        
        # Act & Assert
        with pytest.raises(AuthenticationError) as exc_info:
            auth_service.get_current_user(invalid_token)
        
        assert exc_info.value.code == "AUTH_ERROR"
        assert "Invalid token" in exc_info.value.user_message
    
    def test_get_current_user_nonexistent_user(self, auth_service):
        """Test getting current user with token for non-existent user."""
        # Arrange
        user_data = {
            "id": "nonexistent-user",
            "email": "nonexistent@example.com",
            "role": "admin"
        }
        token = auth_service.create_access_token(user_data)
        
        # Act & Assert
        with pytest.raises(AuthenticationError) as exc_info:
            auth_service.get_current_user(token)
        
        assert exc_info.value.code == "AUTH_ERROR"
        assert "User not found" in exc_info.value.user_message
