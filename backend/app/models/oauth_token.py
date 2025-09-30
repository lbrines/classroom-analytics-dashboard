from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class OAuthTokenBase(BaseModel):
    user_id: str
    provider: str
    access_token: str
    refresh_token: Optional[str] = None
    expires_at: datetime
    scope: str


class OAuthTokenCreate(OAuthTokenBase):
    pass


class OAuthTokenUpdate(BaseModel):
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None
    expires_at: Optional[datetime] = None
    scope: Optional[str] = None


class OAuthTokenInDB(OAuthTokenBase):
    id: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class OAuthToken(OAuthTokenBase):
    id: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
