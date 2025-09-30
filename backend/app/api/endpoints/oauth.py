from fastapi import APIRouter, Depends, HTTPException, Query
from app.schemas.oauth_schema import (
    OAuthURLRequest, OAuthURLResponse, OAuthCallbackRequest, OAuthCallbackResponse,
    OAuthRevokeRequest, OAuthRevokeResponse, OAuthStatusResponse
)
from app.schemas.response_schema import create_success_response, create_error_response
from app.services.oauth_service import oauth_service
from app.middleware.auth_middleware import get_current_active_user
from app.models.user import UserInDB
from app.core.exceptions import AuthenticationError, create_http_exception

router = APIRouter()


@router.get("/google/url")
async def get_google_oauth_url(state: str = Query(None, description="State parameter for OAuth")):
    """Get Google OAuth authorization URL."""
    try:
        result = oauth_service.get_authorization_url(state)
        return create_success_response(result).model_dump()
        
    except AuthenticationError as e:
        return create_error_response(e.code, e.message, e.details).model_dump()
    except Exception as e:
        return create_error_response(
            "OAUTH_ERROR",
            "Failed to get OAuth URL",
            {"detail": str(e)}
        ).model_dump()


@router.get("/google/callback")
async def google_oauth_callback(
    code: str = Query(..., description="Authorization code from Google"),
    state: str = Query(..., description="State parameter")
):
    """Handle Google OAuth callback."""
    try:
        result = oauth_service.handle_callback(code, state)
        return create_success_response(result).model_dump()
        
    except AuthenticationError as e:
        return create_error_response(e.code, e.message, e.details).model_dump()
    except Exception as e:
        return create_error_response(
            "OAUTH_ERROR",
            "OAuth callback failed",
            {"detail": str(e)}
        ).model_dump()


@router.post("/google/revoke")
async def revoke_google_oauth(
    current_user: UserInDB = Depends(get_current_active_user)
):
    """Revoke Google OAuth connection."""
    try:
        success = oauth_service.revoke_token(current_user.id)
        if not success:
            return create_error_response(
                "OAUTH_NOT_CONNECTED",
                "No OAuth connection found"
            ).model_dump()
        
        return create_success_response({"message": "OAuth connection revoked successfully"}).model_dump()
        
    except Exception as e:
        return create_error_response(
            "OAUTH_ERROR",
            "Failed to revoke OAuth connection",
            {"detail": str(e)}
        ).model_dump()


@router.get("/status")
async def get_oauth_status(
    current_user: UserInDB = Depends(get_current_active_user)
):
    """Get OAuth connection status."""
    try:
        status_info = oauth_service.get_oauth_status(current_user.id)
        return create_success_response(status_info).model_dump()
        
    except Exception as e:
        return create_error_response(
            "OAUTH_ERROR",
            "Failed to get OAuth status",
            {"detail": str(e)}
        ).model_dump()
