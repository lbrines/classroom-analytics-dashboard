from pydantic_settings import BaseSettings
from typing import Optional
import os


class Settings(BaseSettings):
    # Environment
    environment: str = "development"
    port: int = 8000
    
    # JWT Configuration
    jwt_secret: str = "dev-secret-key-change-in-production"
    jwt_expires_in: str = "24h"
    
    # CORS Configuration
    cors_origin: str = "http://localhost:3000"
    
    # Logging
    log_level: str = "debug"
    
    # Google OAuth
    google_client_id: Optional[str] = None
    google_client_secret: Optional[str] = None
    google_redirect_uri: str = "http://localhost:3000/oauth/callback"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# Global settings instance
settings = Settings()
