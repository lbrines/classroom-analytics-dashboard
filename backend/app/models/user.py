"""User models."""

from typing import Optional
from pydantic import BaseModel, EmailStr
from enum import Enum


class UserRole(str, Enum):
    """User roles enumeration."""
    ADMIN = "admin"
    COORDINATOR = "coordinator"
    TEACHER = "teacher"
    STUDENT = "student"


class UserBase(BaseModel):
    """Base user model."""
    email: EmailStr
    name: str
    role: UserRole
    active: bool = True


class UserCreate(UserBase):
    """User creation model."""
    password: str


class UserUpdate(BaseModel):
    """User update model."""
    email: Optional[EmailStr] = None
    name: Optional[str] = None
    role: Optional[UserRole] = None
    active: Optional[bool] = None


class UserInDB(UserBase):
    """User model for database."""
    id: str
    password: str


class User(UserBase):
    """User model for API responses."""
    id: str


class UserLogin(BaseModel):
    """User login model."""
    email: EmailStr
    password: str


class Token(BaseModel):
    """Token model."""
    access_token: str
    token_type: str = "bearer"
    expires_in: int


class TokenData(BaseModel):
    """Token data model."""
    user_id: Optional[str] = None
    email: Optional[str] = None
