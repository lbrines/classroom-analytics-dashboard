from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class CourseResponse(BaseModel):
    id: str
    name: str
    section: Optional[str] = None
    description: Optional[str] = None
    room: Optional[str] = None
    owner_id: str
    enrollment_code: Optional[str] = None
    course_state: str
    creation_time: datetime
    update_time: datetime
    alternate_link: Optional[str] = None


class CourseListResponse(BaseModel):
    courses: List[CourseResponse]
    total: int


class CourseSyncResponse(BaseModel):
    synced_count: int
    message: str

