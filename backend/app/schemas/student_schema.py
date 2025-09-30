from pydantic import BaseModel, EmailStr
from typing import Optional, List


class StudentResponse(BaseModel):
    user_id: str
    full_name: str
    email_address: Optional[EmailStr] = None
    course_id: str
    profile_id: Optional[str] = None
    photo_url: Optional[str] = None


class StudentListResponse(BaseModel):
    students: List[StudentResponse]
    total: int
    course_id: str

