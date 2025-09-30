from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class StudentBase(BaseModel):
    user_id: str
    full_name: str
    email_address: Optional[EmailStr] = None
    photo_url: Optional[str] = None


class Student(StudentBase):
    course_id: str
    profile_id: Optional[str] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "student-001",
                "full_name": "Ana Martinez",
                "email_address": "student1@educational.dashboard",
                "course_id": "123456789",
                "photo_url": None,
                "profile_id": "profile-001"
            }
        }


class StudentProgress(BaseModel):
    student_id: str
    student_name: str
    course_id: str
    course_name: str
    progress: float  # Percentage 0-100
    grade: Optional[float] = None
    assignments_completed: int = 0
    assignments_total: int = 0
    last_activity: Optional[datetime] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "student_id": "student-001",
                "student_name": "Ana Martinez",
                "course_id": "123456789",
                "course_name": "eCommerce Specialist",
                "progress": 85.0,
                "grade": 8.9,
                "assignments_completed": 28,
                "assignments_total": 30,
                "last_activity": "2025-09-30T15:30:00Z"
            }
        }

