"""Authentication endpoints."""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.models.user import UserLogin, Token
from app.services.auth_service import AuthService
from app.services.mock_service import MockService
from app.utils.response_helper import ResponseHelper
from app.core.exceptions import AuthenticationError

router = APIRouter()
security = HTTPBearer()
response_helper = ResponseHelper()

# Initialize services
mock_service = MockService()
auth_service = AuthService(mock_service)


@router.post("/login", response_model=dict)
async def login(login_data: UserLogin):
    """Login endpoint."""
    try:
        # Authenticate user
        user = auth_service.authenticate_user(login_data.email, login_data.password)
        
        # Create access token
        access_token = auth_service.create_access_token(user)
        
        # Create token response
        token_data = Token(
            access_token=access_token,
            token_type="bearer",
            expires_in=86400  # 24 hours
        )
        
        response = response_helper.create_success_response(token_data.model_dump())
        return response.model_dump()
    
    except AuthenticationError as e:
        raise e


@router.get("/me", response_model=dict)
async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Get current user endpoint."""
    try:
        # Get current user from token
        user = auth_service.get_current_user(credentials.credentials)
        
        # Remove password from response
        user_response = {
            "id": user["id"],
            "email": user["email"],
            "name": user["name"],
            "role": user["role"],
            "active": user["active"]
        }
        
        response = response_helper.create_success_response(user_response)
        return response.model_dump()
    
    except AuthenticationError as e:
        raise e


@router.post("/logout", response_model=dict)
async def logout(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Logout endpoint."""
    try:
        # Verify token is valid (even though we're logging out)
        auth_service.get_current_user(credentials.credentials)
        
        response = response_helper.create_success_response({
            "message": "Successfully logged out"
        })
        return response.model_dump()
    
    except AuthenticationError as e:
        raise e
