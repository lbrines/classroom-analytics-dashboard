from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Optional
from app.services.auth_service import auth_service
from app.models.user import UserInDB
from app.core.exceptions import AuthenticationError, create_http_exception

# Security scheme
security = HTTPBearer()


async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> UserInDB:
    """Get current authenticated user from JWT token."""
    try:
        token = credentials.credentials
        user = auth_service.get_user_from_token(token)
        
        if not user:
            raise AuthenticationError("Invalid token")
        
        if not user.active:
            raise AuthenticationError("User account is disabled")
        
        return user
        
    except AuthenticationError as e:
        raise create_http_exception(e)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": {"code": "AUTH_ERROR", "message": "Authentication failed"}}
        )


async def get_current_active_user(current_user: UserInDB = Depends(get_current_user)) -> UserInDB:
    """Get current active user."""
    if not current_user.active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": {"code": "USER_INACTIVE", "message": "Inactive user"}}
        )
    return current_user


def require_role(required_role: str):
    """Decorator to require specific role."""
    def role_checker(current_user: UserInDB = Depends(get_current_active_user)) -> UserInDB:
        if current_user.role.value != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail={"error": {"code": "INSUFFICIENT_PERMISSIONS", "message": f"Role {required_role} required"}}
            )
        return current_user
    return role_checker


def require_any_role(required_roles: list):
    """Decorator to require any of the specified roles."""
    def role_checker(current_user: UserInDB = Depends(get_current_active_user)) -> UserInDB:
        if current_user.role.value not in required_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail={"error": {"code": "INSUFFICIENT_PERMISSIONS", "message": f"One of roles {required_roles} required"}}
            )
        return current_user
    return role_checker
