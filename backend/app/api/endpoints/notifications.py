from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.services.notification_service import NotificationService
from app.schemas.notification_schema import (
    NotificationResponse,
    NotificationListResponse,
    MarkAsReadRequest,
    NotificationPreferencesResponse
)
from app.schemas.response_schema import create_success_response
from app.middleware.auth_middleware import get_current_user
from app.models.user import User

router = APIRouter()


def get_notification_service():
    """Dependency to get NotificationService instance."""
    return NotificationService()


@router.get("/notifications", response_model=dict)
async def get_notifications(
    unread_only: bool = False,
    current_user: User = Depends(get_current_user),
    notification_service: NotificationService = Depends(get_notification_service)
):
    """
    Get notifications for current user.
    
    Requires authentication.
    """
    notifications = notification_service.get_notifications(
        user_id=current_user.id,
        unread_only=unread_only
    )
    unread_count = notification_service.get_unread_count(current_user.id)
    
    notifications_data = [
        NotificationResponse(
            id=n.id,
            user_id=n.user_id,
            type=n.type.value,
            priority=n.priority.value,
            title=n.title,
            message=n.message,
            data=n.data,
            read=n.read,
            created_at=n.created_at,
            expires_at=n.expires_at
        ).model_dump()
        for n in notifications
    ]
    
    response_data = {
        "notifications": notifications_data,
        "total": len(notifications_data),
        "unread_count": unread_count
    }
    
    return create_success_response(response_data).model_dump()


@router.put("/notifications/{notification_id}/read", response_model=dict)
async def mark_notification_as_read(
    notification_id: str,
    current_user: User = Depends(get_current_user),
    notification_service: NotificationService = Depends(get_notification_service)
):
    """
    Mark a notification as read.
    
    Requires authentication.
    """
    success = notification_service.mark_as_read(notification_id, current_user.id)
    
    if not success:
        raise HTTPException(status_code=404, detail="Notification not found")
    
    response_data = {
        "notification_id": notification_id,
        "status": "marked_as_read"
    }
    
    return create_success_response(response_data).model_dump()


@router.get("/notifications/preferences", response_model=dict)
async def get_notification_preferences(
    current_user: User = Depends(get_current_user),
    notification_service: NotificationService = Depends(get_notification_service)
):
    """
    Get notification preferences for current user.
    
    Requires authentication.
    """
    preferences = notification_service.get_preferences(current_user.id)
    
    preferences_data = NotificationPreferencesResponse(
        user_id=preferences.user_id,
        channels=preferences.channels,
        types=preferences.types,
        quiet_hours_enabled=preferences.quiet_hours_enabled,
        quiet_hours_start=preferences.quiet_hours_start,
        quiet_hours_end=preferences.quiet_hours_end
    ).model_dump()
    
    return create_success_response(preferences_data).model_dump()

