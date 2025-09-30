"""Tests for response helper."""

import pytest
from datetime import datetime
from app.utils.response_helper import ResponseHelper
from app.models.response import SuccessResponse, ErrorResponse, ResponseMeta, ErrorDetail


class TestResponseHelper:
    """Test cases for ResponseHelper."""
    
    @pytest.fixture
    def response_helper(self):
        """Create ResponseHelper instance for testing."""
        return ResponseHelper()
    
    def test_create_success_response(self, response_helper):
        """Test successful response creation."""
        # Arrange
        data = {"message": "Success", "user_id": "123"}
        request_id = "req-123"
        
        # Act
        response = response_helper.create_success_response(data, request_id)
        
        # Assert
        assert isinstance(response, SuccessResponse)
        assert response.data == data
        assert response.meta.request_id == request_id
        assert response.meta.version == "1.0.0"
        assert isinstance(response.meta.timestamp, str)
    
    def test_create_error_response(self, response_helper):
        """Test error response creation."""
        # Arrange
        error_code = "AUTH_ERROR"
        error_message = "Authentication failed"
        user_message = "Invalid credentials"
        details = {"field": "email", "reason": "not found"}
        request_id = "req-123"
        
        # Act
        response = response_helper.create_error_response(
            error_code, error_message, user_message, details, request_id
        )
        
        # Assert
        assert isinstance(response, ErrorResponse)
        assert response.error.code == error_code
        assert response.error.message == error_message
        assert response.error.user_message == user_message
        assert response.error.details == details
        assert response.meta.request_id == request_id
        assert response.meta.version == "1.0.0"
        assert isinstance(response.meta.timestamp, str)
    
    def test_create_success_response_without_request_id(self, response_helper):
        """Test successful response creation without request ID."""
        # Arrange
        data = {"message": "Success"}
        
        # Act
        response = response_helper.create_success_response(data)
        
        # Assert
        assert isinstance(response, SuccessResponse)
        assert response.data == data
        assert response.meta.request_id is None
        assert response.meta.version == "1.0.0"
    
    def test_create_error_response_without_details(self, response_helper):
        """Test error response creation without details."""
        # Arrange
        error_code = "VALIDATION_ERROR"
        error_message = "Validation failed"
        user_message = "Please check your input"
        
        # Act
        response = response_helper.create_error_response(
            error_code, error_message, user_message
        )
        
        # Assert
        assert isinstance(response, ErrorResponse)
        assert response.error.code == error_code
        assert response.error.message == error_message
        assert response.error.user_message == user_message
        assert response.error.details is None
    
    def test_create_meta(self, response_helper):
        """Test metadata creation."""
        # Arrange
        request_id = "req-456"
        
        # Act
        meta = response_helper.create_meta(request_id)
        
        # Assert
        assert isinstance(meta, ResponseMeta)
        assert meta.request_id == request_id
        assert meta.version == "1.0.0"
        assert isinstance(meta.timestamp, str)
    
    def test_create_meta_without_request_id(self, response_helper):
        """Test metadata creation without request ID."""
        # Act
        meta = response_helper.create_meta()
        
        # Assert
        assert isinstance(meta, ResponseMeta)
        assert meta.request_id is None
        assert meta.version == "1.0.0"
        assert isinstance(meta.timestamp, str)
