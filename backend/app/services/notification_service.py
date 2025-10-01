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
    
    def update_preferences(self, user_id: str, preferences_data: dict) -> bool:
        """
        Update notification preferences for a user.
        
        Args:
            user_id: The user ID
            preferences_data: Dictionary with preference updates
            
        Returns:
            True if successful, False otherwise
        """
        try:
            data = self._load_data()
            
            # Find existing preferences
            prefs_found = False
            for i, prefs_data in enumerate(data.get("preferences", [])):
                if prefs_data.get("user_id") == user_id:
                    # Update existing preferences
                    if "channels" in preferences_data:
                        prefs_data["channels"].update(preferences_data["channels"])
                    if "types" in preferences_data:
                        prefs_data["types"].update(preferences_data["types"])
                    if "quiet_hours_enabled" in preferences_data:
                        prefs_data["quiet_hours_enabled"] = preferences_data["quiet_hours_enabled"]
                    if "quiet_hours_start" in preferences_data:
                        prefs_data["quiet_hours_start"] = preferences_data["quiet_hours_start"]
                    if "quiet_hours_end" in preferences_data:
                        prefs_data["quiet_hours_end"] = preferences_data["quiet_hours_end"]
                    prefs_found = True
                    break
            
            if not prefs_found:
                # Create new preferences
                new_prefs = {
                    "user_id": user_id,
                    "channels": preferences_data.get("channels", {
                        "in_app": True,
                        "email": False,
                        "telegram": False
                    }),
                    "types": preferences_data.get("types", {
                        "assignment": True,
                        "student_risk": True,
                        "announcement": True,
                        "grade": False,
                        "system": True
                    }),
                    "quiet_hours_enabled": preferences_data.get("quiet_hours_enabled", False),
                    "quiet_hours_start": preferences_data.get("quiet_hours_start", "22:00"),
                    "quiet_hours_end": preferences_data.get("quiet_hours_end", "08:00")
                }
                
                if "preferences" not in data:
                    data["preferences"] = []
                data["preferences"].append(new_prefs)
            
            # Save updated data (in a real implementation, this would be persisted)
            self._data = data
            return True
            
        except Exception as e:
            print(f"Error updating preferences: {e}")
            return False

