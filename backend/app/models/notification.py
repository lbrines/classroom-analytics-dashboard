from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum


class NotificationType(str, Enum):
    ALERT = "alert"
    INFO = "info"
    WARNING = "warning"
    SUCCESS = "success"


class NotificationPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


class NotificationAction(BaseModel):
    label: str
    url: Optional[str] = None
    action: Optional[str] = None


class Notification(BaseModel):
    id: str
    user_id: str
    type: NotificationType
    priority: NotificationPriority
    title: str
    message: str
    data: Optional[Dict[str, Any]] = None
    read: bool = False
    created_at: datetime
    expires_at: Optional[datetime] = None
    actions: Optional[List[NotificationAction]] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": "notif-001",
                "user_id": "teacher-001",
                "type": "alert",
                "priority": "high",
                "title": "Student at Risk",
                "message": "John Smith has missed 3 consecutive assignments",
                "data": {
                    "student_id": "student-045",
                    "course_id": "course-001",
                    "assignments_missed": 3
                },
                "read": False,
                "created_at": "2025-09-28T14:30:00Z",
                "expires_at": "2025-10-05T14:30:00Z"
            }
        }


class NotificationPreferences(BaseModel):
    user_id: str
    channels: Dict[str, bool]  # in_app, email, telegram
    types: Dict[str, bool]  # assignment, student_risk, announcement, grade
    quiet_hours_enabled: bool = False
    quiet_hours_start: Optional[str] = None
    quiet_hours_end: Optional[str] = None
    digest_enabled: bool = False
    digest_frequency: Optional[str] = None
    digest_time: Optional[str] = None

