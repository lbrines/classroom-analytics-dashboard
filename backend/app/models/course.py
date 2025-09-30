from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from enum import Enum


class CourseState(str, Enum):
    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    PROVISIONED = "PROVISIONED"
    DECLINED = "DECLINED"


class CourseBase(BaseModel):
    id: str
    name: str
    section: Optional[str] = None
    description: Optional[str] = None
    room: Optional[str] = None
    owner_id: str
    enrollment_code: Optional[str] = None
    course_state: CourseState = CourseState.ACTIVE


class Course(CourseBase):
    creation_time: datetime
    update_time: datetime
    alternate_link: Optional[str] = None
    teacher_group_email: Optional[str] = None
    course_group_email: Optional[str] = None
    guardians_enabled: bool = False
    calendar_id: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "id": "123456789",
                "name": "eCommerce Specialist",
                "section": "Section A",
                "description": "Complete eCommerce course",
                "room": "Virtual Room 1",
                "owner_id": "teacher-001",
                "enrollment_code": "abc123",
                "course_state": "ACTIVE",
                "creation_time": "2025-08-15T10:00:00Z",
                "update_time": "2025-09-20T15:30:00Z",
                "alternate_link": "https://classroom.google.com/c/123456789",
                "guardians_enabled": False
            }
        }

