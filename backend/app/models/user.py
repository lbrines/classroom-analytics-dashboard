from pydantic import BaseModel, EmailStr
from typing import Optional, List
from enum import Enum
from datetime import datetime


class UserRole(str, Enum):
    ADMINISTRATOR = "administrator"
    COORDINATOR = "coordinator"
    TEACHER = "teacher"
    STUDENT = "student"


class UserBase(BaseModel):
    email: EmailStr
    name: str
    role: UserRole
    active: bool = True


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    name: Optional[str] = None
    role: Optional[UserRole] = None
    active: Optional[bool] = None


class UserInDB(UserBase):
    id: str
    password_hash: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class User(UserBase):
    id: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class UserList(BaseModel):
    users: List[User]
    total: int
    page: int
    size: int
