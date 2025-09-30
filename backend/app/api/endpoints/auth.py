from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.user_schema import (
    LoginRequest, LoginResponse, RefreshTokenRequest, RefreshTokenResponse,
    LogoutRequest, LogoutResponse, UserProfileResponse
)
from app.schemas.response_schema import create_success_response, create_error_response
from app.services.auth_service import auth_service
from app.middleware.auth_middleware import get_current_active_user
from app.models.user import UserInDB
from app.core.exceptions import AuthenticationError, create_http_exception

router = APIRouter()


@router.post("/login")
async def login(request: LoginRequest):
    """Authenticate user and return JWT token."""
    try:
        user = auth_service.authenticate_user(request.email, request.password)
        if not user:
            return create_error_response(
                "AUTH_INVALID_CREDENTIALS",
                "Invalid email or password"
            ).model_dump()
        
        token_data = auth_service.create_token(user)
        return create_success_response(token_data).model_dump()
        
    except AuthenticationError as e:
        return create_error_response(e.code, e.message, e.details).model_dump()
    except Exception as e:
        return create_error_response(
            "AUTH_ERROR",
            "Authentication failed",
            {"detail": str(e)}
        ).model_dump()


@router.post("/refresh")
async def refresh_token(request: RefreshTokenRequest):
    """Refresh access token."""
    try:
        token_data = auth_service.refresh_token(request.refresh_token)
        if not token_data:
            return create_error_response(
                "AUTH_INVALID_TOKEN",
                "Invalid refresh token"
            ).model_dump()
        
        return create_success_response(token_data).model_dump()
        
    except Exception as e:
        return create_error_response(
            "AUTH_ERROR",
            "Token refresh failed",
            {"detail": str(e)}
        ).model_dump()


@router.post("/logout")
async def logout(request: LogoutRequest):
    """Logout user and invalidate token."""
    try:
        success = auth_service.logout_user(request.token)
        if not success:
            return create_error_response(
                "AUTH_INVALID_TOKEN",
                "Invalid token"
            ).model_dump()
        
        return create_success_response({"message": "Successfully logged out"}).model_dump()
        
    except Exception as e:
        return create_error_response(
            "AUTH_ERROR",
            "Logout failed",
            {"detail": str(e)}
        ).model_dump()


@router.get("/me")
async def get_current_user_info(current_user: UserInDB = Depends(get_current_active_user)):
    """Get current user information."""
    try:
        user_profile = auth_service.get_user_profile(current_user.id)
        if not user_profile:
            return create_error_response(
                "USER_NOT_FOUND",
                "User not found"
            ).model_dump()
        
        return create_success_response({
            "id": user_profile.id,
            "email": user_profile.email,
            "name": user_profile.name,
            "role": user_profile.role.value,
            "active": user_profile.active,
            "created_at": user_profile.created_at.isoformat(),
            "updated_at": user_profile.updated_at.isoformat()
        }).model_dump()
        
    except Exception as e:
        return create_error_response(
            "USER_ERROR",
            "Failed to get user information",
            {"detail": str(e)}
        ).model_dump()
