"""Tests for mock service."""

import pytest
import json
from pathlib import Path
from app.services.mock_service import MockService
from app.models.user import User, UserRole, UserLogin


class TestMockService:
    """Test cases for MockService."""
    
    @pytest.fixture
    def mock_service(self):
        """Create MockService instance for testing."""
        return MockService()
    
    def test_load_mock_users_success(self, mock_service):
        """Test successful loading of mock users."""
        # Arrange & Act
        users = mock_service.load_mock_users()
        
        # Assert
        assert isinstance(users, list)
        assert len(users) >= 4  # We expect at least 4 users from mock data
        
        # Check that all users have required fields
        for user in users:
            assert "id" in user
            assert "email" in user
            assert "password" in user
            assert "role" in user
            assert "name" in user
            assert "active" in user
            assert user["role"] in ["admin", "coordinator", "teacher", "student"]
    
    def test_get_user_by_email_success(self, mock_service):
        """Test successful user retrieval by email."""
        # Arrange
        test_email = "admin@educational.dashboard"
        
        # Act
        user = mock_service.get_user_by_email(test_email)
        
        # Assert
        assert user is not None
        assert user["email"] == test_email
        assert user["role"] == "admin"
        assert user["name"] == "System Administrator"
    
    def test_get_user_by_email_not_found(self, mock_service):
        """Test user retrieval with non-existent email."""
        # Arrange
        non_existent_email = "nonexistent@example.com"
        
        # Act
        user = mock_service.get_user_by_email(non_existent_email)
        
        # Assert
        assert user is None
    
    def test_get_user_by_id_success(self, mock_service):
        """Test successful user retrieval by ID."""
        # Arrange
        test_id = "admin-001"
        
        # Act
        user = mock_service.get_user_by_id(test_id)
        
        # Assert
        assert user is not None
        assert user["id"] == test_id
        assert user["email"] == "admin@educational.dashboard"
    
    def test_get_user_by_id_not_found(self, mock_service):
        """Test user retrieval with non-existent ID."""
        # Arrange
        non_existent_id = "nonexistent-id"
        
        # Act
        user = mock_service.get_user_by_id(non_existent_id)
        
        # Assert
        assert user is None
    
    def test_verify_user_credentials_success(self, mock_service):
        """Test successful credential verification."""
        # Arrange
        email = "admin@educational.dashboard"
        password = "admin123"
        
        # Act
        user = mock_service.verify_user_credentials(email, password)
        
        # Assert
        assert user is not None
        assert user["email"] == email
        assert user["password"] == password
    
    def test_verify_user_credentials_wrong_password(self, mock_service):
        """Test credential verification with wrong password."""
        # Arrange
        email = "admin@educational.dashboard"
        wrong_password = "wrongpassword"
        
        # Act
        user = mock_service.verify_user_credentials(email, wrong_password)
        
        # Assert
        assert user is None
    
    def test_verify_user_credentials_wrong_email(self, mock_service):
        """Test credential verification with wrong email."""
        # Arrange
        wrong_email = "wrong@example.com"
        password = "admin123"
        
        # Act
        user = mock_service.verify_user_credentials(wrong_email, password)
        
        # Assert
        assert user is None
    
    def test_get_all_users(self, mock_service):
        """Test retrieval of all users."""
        # Act
        users = mock_service.get_all_users()
        
        # Assert
        assert isinstance(users, list)
        assert len(users) >= 4
        
        # Check that we have at least one user of each role
        roles = [user["role"] for user in users]
        assert "admin" in roles
        assert "coordinator" in roles
        assert "teacher" in roles
        assert "student" in roles
