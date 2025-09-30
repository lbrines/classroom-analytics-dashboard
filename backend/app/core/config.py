"""Configuration settings for the application."""

from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Application settings."""
    
    # Environment
    environment: str = "development"
    
    # Ports
    frontend_port: int = 3000
    backend_port: int = 8000
    database_port: int = 5432
    
    # Backend
    port: int = 8000
    jwt_secret: str = "dev-secret-key-change-in-production"
    jwt_expires_in: str = "24h"
    cors_origin: str = "http://localhost:3000"
    log_level: str = "debug"
    
    # OAuth
    google_client_id: str = "your-google-client-id.apps.googleusercontent.com"
    google_client_secret: str = "your-google-client-secret"
    google_redirect_uri: str = "http://localhost:3000/oauth/callback"
    google_scopes: str = "profile,email,openid"
    oauth_pkce_enabled: bool = True
    oauth_state_secret: str = "your-random-state-secret"
    oauth_refresh_token_rotation_enabled: bool = True
    oauth_refresh_token_expiry_days: int = 30
    oauth_access_token_expiry_minutes: int = 15
    oauth_enforce_https: bool = True
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
