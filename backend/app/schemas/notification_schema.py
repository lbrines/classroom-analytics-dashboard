from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class NotificationResponse(BaseModel):
    id: str
    user_id: str
    type: str
    priority: str
    title: str
    message: str
    data: Optional[Dict[str, Any]] = None
    read: bool
    created_at: datetime
    expires_at: Optional[datetime] = None


class NotificationListResponse(BaseModel):
    notifications: List[NotificationResponse]
    total: int
    unread_count: int


class MarkAsReadRequest(BaseModel):
    notification_id: str


class NotificationPreferencesResponse(BaseModel):
    user_id: str
    channels: Dict[str, bool]
    types: Dict[str, bool]
    quiet_hours_enabled: bool
    quiet_hours_start: Optional[str] = None
    quiet_hours_end: Optional[str] = None

