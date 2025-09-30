import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestAuthIntegration:
    """Integration tests for authentication endpoints."""
    
    def test_health_check(self):
        """Test health check endpoint."""
        response = client.get("/api/v1/health/health")
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        assert data["data"]["status"] == "healthy"
    
    def test_login_valid_credentials(self):
        """Test login with valid credentials."""
        response = client.post(
            "/api/v1/auth/login",
            json={
                "email": "admin@educational.dashboard",
                "password": "admin123"
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        assert "access_token" in data["data"]
        assert data["data"]["token_type"] == "bearer"
        assert "user" in data["data"]
    
    def test_login_invalid_credentials(self):
        """Test login with invalid credentials."""
        response = client.post(
            "/api/v1/auth/login",
            json={
                "email": "admin@educational.dashboard",
                "password": "wrongpassword"
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert "error" in data
        assert data["error"]["code"] == "AUTH_INVALID_CREDENTIALS"
    
    def test_login_nonexistent_user(self):
        """Test login with nonexistent user."""
        response = client.post(
            "/api/v1/auth/login",
            json={
                "email": "nonexistent@example.com",
                "password": "password"
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert "error" in data
        assert data["error"]["code"] == "AUTH_INVALID_CREDENTIALS"
    
    def test_get_current_user_with_valid_token(self):
        """Test getting current user with valid token."""
        # First login to get token
        login_response = client.post(
            "/api/v1/auth/login",
            json={
                "email": "admin@educational.dashboard",
                "password": "admin123"
            }
        )
        assert login_response.status_code == 200
        token = login_response.json()["data"]["access_token"]
        
        # Use token to get current user
        response = client.get(
            "/api/v1/auth/me",
            headers={"Authorization": f"Bearer {token}"}
        )
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        assert data["data"]["email"] == "admin@educational.dashboard"
        assert data["data"]["role"] == "administrator"
    
    def test_get_current_user_without_token(self):
        """Test getting current user without token."""
        response = client.get("/api/v1/auth/me")
        assert response.status_code == 403
    
    def test_get_current_user_with_invalid_token(self):
        """Test getting current user with invalid token."""
        response = client.get(
            "/api/v1/auth/me",
            headers={"Authorization": "Bearer invalid_token"}
        )
        assert response.status_code == 401
    
    def test_logout(self):
        """Test logout endpoint."""
        # First login to get a valid token
        login_response = client.post(
            "/api/v1/auth/login",
            json={
                "email": "admin@educational.dashboard",
                "password": "admin123"
            }
        )
        assert login_response.status_code == 200
        token = login_response.json()["data"]["access_token"]
        
        # Now test logout with valid token
        response = client.post(
            "/api/v1/auth/logout",
            json={"token": token}
        )
        assert response.status_code == 200
        data = response.json()
        assert "data" in data
        assert "message" in data["data"]
