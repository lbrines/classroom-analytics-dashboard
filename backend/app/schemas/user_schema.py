from pydantic import BaseModel, EmailStr
from typing import Optional
from app.models.user import UserRole


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int
    user: dict


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class RefreshTokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int


class LogoutRequest(BaseModel):
    token: str


class LogoutResponse(BaseModel):
    message: str


class UserProfileResponse(BaseModel):
    id: str
    email: EmailStr
    name: str
    role: UserRole
    active: bool
    created_at: str
    updated_at: str


class ChangePasswordRequest(BaseModel):
    current_password: str
    new_password: str


class ChangePasswordResponse(BaseModel):
    message: str
