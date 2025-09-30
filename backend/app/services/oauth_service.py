import secrets
from datetime import datetime, timedelta
from typing import Optional, Dict, Any
from google.auth.transport import requests
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from app.core.config import settings
from app.services.mock_service import mock_service
from app.core.exceptions import AuthenticationError


class OAuthService:
    """Service for handling OAuth operations."""
    
    def __init__(self):
        self.client_config = {
            "web": {
                "client_id": settings.google_client_id,
                "client_secret": settings.google_client_secret,
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "redirect_uris": [settings.google_redirect_uri]
            }
        }
        self.scopes = [
            "https://www.googleapis.com/auth/userinfo.email",
            "https://www.googleapis.com/auth/userinfo.profile",
            "https://www.googleapis.com/auth/classroom.courses.readonly"
        ]
    
    def get_authorization_url(self, state: Optional[str] = None) -> Dict[str, str]:
        """Get Google OAuth authorization URL."""
        if not settings.google_client_id:
            raise AuthenticationError("Google OAuth not configured")
        
        flow = Flow.from_client_config(
            self.client_config,
            scopes=self.scopes,
            redirect_uri=settings.google_redirect_uri
        )
        
        if not state:
            state = secrets.token_urlsafe(32)
        
        authorization_url, _ = flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true',
            state=state
        )
        
        return {
            "auth_url": authorization_url,
            "state": state
        }
    
    def handle_callback(self, code: str, state: str) -> Dict[str, Any]:
        """Handle OAuth callback and exchange code for tokens."""
        if not settings.google_client_id:
            raise AuthenticationError("Google OAuth not configured")
        
        flow = Flow.from_client_config(
            self.client_config,
            scopes=self.scopes,
            redirect_uri=settings.google_redirect_uri
        )
        
        try:
            flow.fetch_token(code=code)
            credentials = flow.credentials
            
            # Get user info from Google
            user_info = self._get_user_info(credentials)
            
            # Find or create user
            user = self._find_or_create_user(user_info)
            
            # Save OAuth token
            token_data = {
                "user_id": user.id,
                "provider": "google",
                "access_token": credentials.token,
                "refresh_token": credentials.refresh_token,
                "expires_at": (datetime.utcnow() + timedelta(seconds=credentials.expiry)).isoformat() + "Z",
                "scope": " ".join(self.scopes)
            }
            
            oauth_token = mock_service.save_oauth_token(token_data)
            
            # Create JWT token for our system
            from app.services.auth_service import auth_service
            jwt_response = auth_service.create_token(user)
            
            return {
                "access_token": jwt_response["access_token"],
                "token_type": "bearer",
                "expires_in": jwt_response["expires_in"],
                "user": jwt_response["user"]
            }
            
        except Exception as e:
            raise AuthenticationError(f"OAuth callback failed: {str(e)}")
    
    def _get_user_info(self, credentials: Credentials) -> Dict[str, Any]:
        """Get user information from Google."""
        try:
            request = requests.Request()
            user_info_response = request.get(
                'https://www.googleapis.com/oauth2/v2/userinfo',
                headers={'Authorization': f'Bearer {credentials.token}'}
            )
            return user_info_response.json()
        except Exception as e:
            raise AuthenticationError(f"Failed to get user info: {str(e)}")
    
    def _find_or_create_user(self, user_info: Dict[str, Any]) -> Any:
        """Find existing user or create new one from Google user info."""
        email = user_info.get("email")
        if not email:
            raise AuthenticationError("No email found in Google user info")
        
        # Try to find existing user
        user = mock_service.get_user_by_email(email)
        if user:
            return user
        
        # Create new user (in mock, we'll just return a default user)
        # In a real implementation, this would create a new user in the database
        default_user = mock_service.get_user_by_email("teacher1@educational.dashboard")
        if default_user:
            return default_user
        
        raise AuthenticationError("Unable to create or find user")
    
    def revoke_token(self, user_id: str) -> bool:
        """Revoke OAuth token for user."""
        oauth_token = mock_service.get_oauth_token_by_user(user_id, "google")
        if not oauth_token:
            return False
        
        try:
            credentials = Credentials(
                token=oauth_token.access_token,
                refresh_token=oauth_token.refresh_token
            )
            credentials.revoke(requests.Request())
            
            # Delete token from our system
            mock_service.delete_oauth_token(user_id, "google")
            return True
            
        except Exception:
            return False
    
    def get_oauth_status(self, user_id: str) -> Dict[str, Any]:
        """Get OAuth connection status for user."""
        oauth_token = mock_service.get_oauth_token_by_user(user_id, "google")
        
        if not oauth_token:
            return {
                "connected": False,
                "provider": None,
                "user_info": None
            }
        
        # Check if token is still valid
        expires_at = datetime.fromisoformat(oauth_token.expires_at.replace('Z', '+00:00'))
        if expires_at < datetime.utcnow():
            return {
                "connected": False,
                "provider": "google",
                "user_info": None
            }
        
        return {
            "connected": True,
            "provider": "google",
            "user_info": {
                "email": "user@example.com",  # Mock data
                "name": "Google User",
                "picture": "https://via.placeholder.com/150"
            }
        }


# Global instance
oauth_service = OAuthService()
