import json
import os
import uuid
from typing import List, Optional
from datetime import datetime
from app.models.notification import (
    Notification, 
    NotificationPreferences,
    NotificationType,
    NotificationPriority
)


class NotificationService:
    """
    Service for managing notifications.
    Supports in-app notifications with mock email/telegram.
    """
    
    def __init__(self):
        """Initialize NotificationService."""
        self.notifications_file = os.path.join(
            os.path.dirname(__file__), "..", "data", "mock_notifications.json"
        )
        self._data = None
    
    def _load_data(self) -> dict:
        """Load notifications data from file."""
        if self._data is None:
            try:
                with open(self.notifications_file, 'r', encoding='utf-8') as f:
                    self._data = json.load(f)
            except FileNotFoundError:
                self._data = {"notifications": [], "preferences": []}
        return self._data
    
    def get_notifications(
        self, 
        user_id: str, 
        unread_only: bool = False
    ) -> List[Notification]:
        """
        Get notifications for a specific user.
        
        Args:
            user_id: The user ID to get notifications for
            unread_only: If True, only return unread notifications
            
        Returns:
            List of Notification objects
        """
        data = self._load_data()
        notifications = []
        
        for notif_data in data.get("notifications", []):
            if notif_data.get("user_id") == user_id:
                if unread_only and notif_data.get("read", False):
                    continue
                
                notification = Notification(**notif_data)
                notifications.append(notification)
        
        # Sort by created_at descending (newest first)
        notifications.sort(key=lambda x: x.created_at, reverse=True)
        
        return notifications
    
    def get_unread_count(self, user_id: str) -> int:
        """
        Get count of unread notifications for a user.
        
        Args:
            user_id: The user ID
            
        Returns:
            Count of unread notifications
        """
        notifications = self.get_notifications(user_id)
        unread = [n for n in notifications if not n.read]
        return len(unread)
    
    def mark_as_read(self, notification_id: str, user_id: str) -> bool:
        """
        Mark a notification as read.
        
        Args:
            notification_id: The notification ID
            user_id: The user ID (for security)
            
        Returns:
            True if marked successfully, False otherwise
        """
        data = self._load_data()
        
        for notif in data.get("notifications", []):
            if notif.get("id") == notification_id and notif.get("user_id") == user_id:
                notif["read"] = True
                return True
        
        return False
    
    def get_preferences(self, user_id: str) -> NotificationPreferences:
        """
        Get notification preferences for a user.
        
        Args:
            user_id: The user ID
            
        Returns:
            NotificationPreferences object
        """
        data = self._load_data()
        
        # Find user preferences
        for prefs_data in data.get("preferences", []):
            if prefs_data.get("user_id") == user_id:
                return NotificationPreferences(**prefs_data)
        
        # Return default preferences if not found
        return NotificationPreferences(
            user_id=user_id,
            channels={"in_app": True, "email": False, "telegram": False},
            types={"assignment": True, "student_risk": True, "announcement": True, "grade": True}
        )
    
    def create_notification(
        self,
        user_id: str,
        title: str,
        message: str,
        notification_type: str,
        priority: str,
        data: Optional[dict] = None
    ) -> Notification:
        """
        Create a new notification.
        
        Args:
            user_id: The user to notify
            title: Notification title
            message: Notification message
            notification_type: Type of notification
            priority: Priority level
            data: Additional data
            
        Returns:
            Created Notification object
        """
        notification = Notification(
            id=f"notif-{uuid.uuid4().hex[:8]}",
            user_id=user_id,
            type=NotificationType(notification_type),
            priority=NotificationPriority(priority),
            title=title,
            message=message,
            data=data,
            read=False,
            created_at=datetime.now()
        )
        
        return notification

