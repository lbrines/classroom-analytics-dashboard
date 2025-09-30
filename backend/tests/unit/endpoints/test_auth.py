"""Tests for auth endpoints."""

import pytest
from fastapi.testclient import TestClient
from app.main import app


class TestAuthEndpoints:
    """Test cases for authentication endpoints."""
    
    @pytest.fixture
    def client(self):
        """Create test client."""
        return TestClient(app)
    
    def test_login_success(self, client):
        """Test successful login."""
        # Arrange
        login_data = {
            "email": "admin@educational.dashboard",
            "password": "admin123"
        }
        
        # Act
        response = client.post("/api/v1/auth/login", json=login_data)
        
        # Assert
        assert response.status_code == 200
        
        response_data = response.json()
        assert "data" in response_data
        assert "meta" in response_data
        assert "access_token" in response_data["data"]
        assert response_data["data"]["token_type"] == "bearer"
        assert "expires_in" in response_data["data"]
    
    def test_login_invalid_credentials(self, client):
        """Test login with invalid credentials."""
        # Arrange
        login_data = {
            "email": "admin@educational.dashboard",
            "password": "wrongpassword"
        }
        
        # Act
        response = client.post("/api/v1/auth/login", json=login_data)
        
        # Assert
        assert response.status_code == 401
        
        response_data = response.json()
        assert "error" in response_data
        assert "meta" in response_data
        assert response_data["error"]["code"] == "AUTH_ERROR"
        assert "Invalid credentials" in response_data["error"]["user_message"]
    
    def test_login_nonexistent_user(self, client):
        """Test login with non-existent user."""
        # Arrange
        login_data = {
            "email": "nonexistent@example.com",
            "password": "password123"
        }
        
        # Act
        response = client.post("/api/v1/auth/login", json=login_data)
        
        # Assert
        assert response.status_code == 401
        
        response_data = response.json()
        assert "error" in response_data
        assert response_data["error"]["code"] == "AUTH_ERROR"
    
    def test_login_missing_fields(self, client):
        """Test login with missing required fields."""
        # Arrange
        login_data = {
            "email": "admin@educational.dashboard"
            # missing password
        }
        
        # Act
        response = client.post("/api/v1/auth/login", json=login_data)
        
        # Assert
        assert response.status_code == 422
    
    def test_get_current_user_success(self, client):
        """Test getting current user with valid token."""
        # Arrange
        # First login to get token
        login_data = {
            "email": "admin@educational.dashboard",
            "password": "admin123"
        }
        login_response = client.post("/api/v1/auth/login", json=login_data)
        token = login_response.json()["data"]["access_token"]
        
        # Act
        headers = {"Authorization": f"Bearer {token}"}
        response = client.get("/api/v1/auth/me", headers=headers)
        
        # Assert
        assert response.status_code == 200
        
        response_data = response.json()
        assert "data" in response_data
        assert response_data["data"]["email"] == "admin@educational.dashboard"
        assert response_data["data"]["role"] == "admin"
        assert response_data["data"]["name"] == "System Administrator"
    
    def test_get_current_user_invalid_token(self, client):
        """Test getting current user with invalid token."""
        # Arrange
        invalid_token = "invalid.token.here"
        headers = {"Authorization": f"Bearer {invalid_token}"}
        
        # Act
        response = client.get("/api/v1/auth/me", headers=headers)
        
        # Assert
        assert response.status_code == 401
        
        response_data = response.json()
        assert "error" in response_data
        assert response_data["error"]["code"] == "AUTH_ERROR"
    
    def test_get_current_user_no_token(self, client):
        """Test getting current user without token."""
        # Act
        response = client.get("/api/v1/auth/me")
        
        # Assert
        assert response.status_code == 403
    
    def test_logout_success(self, client):
        """Test successful logout."""
        # Arrange
        # First login to get token
        login_data = {
            "email": "admin@educational.dashboard",
            "password": "admin123"
        }
        login_response = client.post("/api/v1/auth/login", json=login_data)
        token = login_response.json()["data"]["access_token"]
        
        # Act
        headers = {"Authorization": f"Bearer {token}"}
        response = client.post("/api/v1/auth/logout", headers=headers)
        
        # Assert
        assert response.status_code == 200
        
        response_data = response.json()
        assert "data" in response_data
        assert response_data["data"]["message"] == "Successfully logged out"
    
    def test_logout_invalid_token(self, client):
        """Test logout with invalid token."""
        # Arrange
        invalid_token = "invalid.token.here"
        headers = {"Authorization": f"Bearer {invalid_token}"}
        
        # Act
        response = client.post("/api/v1/auth/logout", headers=headers)
        
        # Assert
        assert response.status_code == 401
