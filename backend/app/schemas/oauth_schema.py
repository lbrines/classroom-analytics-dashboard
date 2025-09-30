from pydantic import BaseModel
from typing import Optional


class OAuthURLRequest(BaseModel):
    provider: str = "google"
    redirect_uri: Optional[str] = None


class OAuthURLResponse(BaseModel):
    auth_url: str
    state: str


class OAuthCallbackRequest(BaseModel):
    code: str
    state: str
    provider: str = "google"


class OAuthCallbackResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int
    user: dict


class OAuthRevokeRequest(BaseModel):
    provider: str = "google"


class OAuthRevokeResponse(BaseModel):
    message: str


class OAuthStatusResponse(BaseModel):
    connected: bool
    provider: Optional[str] = None
    user_info: Optional[dict] = None
