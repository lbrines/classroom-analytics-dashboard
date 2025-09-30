"""Tests for health endpoint."""

import pytest
from fastapi.testclient import TestClient
from app.main import app


class TestHealthEndpoint:
    """Test cases for health endpoint."""
    
    @pytest.fixture
    def client(self):
        """Create test client."""
        return TestClient(app)
    
    def test_health_check_success(self, client):
        """Test successful health check."""
        # Act
        response = client.get("/api/v1/health")
        
        # Assert
        assert response.status_code == 200
        
        response_data = response.json()
        assert "data" in response_data
        assert "meta" in response_data
        assert response_data["data"]["status"] == "healthy"
        assert response_data["data"]["message"] == "Service is running"
        assert response_data["meta"]["version"] == "1.0.0"
        assert "timestamp" in response_data["meta"]
    
    def test_health_check_response_structure(self, client):
        """Test health check response structure."""
        # Act
        response = client.get("/api/v1/health")
        
        # Assert
        assert response.status_code == 200
        
        response_data = response.json()
        
        # Check data structure
        assert "status" in response_data["data"]
        assert "message" in response_data["data"]
        assert "timestamp" in response_data["data"]
        
        # Check meta structure
        assert "timestamp" in response_data["meta"]
        assert "version" in response_data["meta"]
        assert response_data["meta"]["version"] == "1.0.0"
