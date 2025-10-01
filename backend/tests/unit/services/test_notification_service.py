import pytest
from datetime import datetime
from app.services.notification_service import NotificationService
from app.models.notification import Notification, NotificationPreferences


class TestNotificationService:
    """Test suite for NotificationService following TDD methodology."""
    
    @pytest.fixture
    def notification_service(self):
        """Create a NotificationService instance for testing."""
        return NotificationService()
    
    def test_get_notifications_returns_list(self, notification_service):
        """Test that get_notifications returns a list."""
        notifications = notification_service.get_notifications("teacher-001")
        assert isinstance(notifications, list)
    
    def test_get_notifications_filters_by_user(self, notification_service):
        """Test that get_notifications only returns user's notifications."""
        notifications = notification_service.get_notifications("teacher-001")
        assert all(n.user_id == "teacher-001" for n in notifications)
    
    def test_get_unread_count_returns_int(self, notification_service):
        """Test that get_unread_count returns correct count."""
        count = notification_service.get_unread_count("teacher-001")
        assert isinstance(count, int)
        assert count >= 0
    
    def test_mark_as_read_returns_true_for_valid_id(self, notification_service):
        """Test that mark_as_read returns True for valid notification."""
        result = notification_service.mark_as_read("notif-001", "teacher-001")
        assert result is True
    
    def test_mark_as_read_returns_false_for_invalid_id(self, notification_service):
        """Test that mark_as_read returns False for invalid notification."""
        result = notification_service.mark_as_read("invalid-id", "teacher-001")
        assert result is False
    
    def test_get_preferences_returns_preferences_object(self, notification_service):
        """Test that get_preferences returns NotificationPreferences."""
        prefs = notification_service.get_preferences("teacher-001")
        assert isinstance(prefs, NotificationPreferences)
        assert prefs.user_id == "teacher-001"
    
    def test_create_notification_returns_notification(self, notification_service):
        """Test that create_notification creates new notification."""
        notif = notification_service.create_notification(
            user_id="teacher-001",
            title="Test",
            message="Test message",
            notification_type="info",
            priority="medium"
        )
        assert isinstance(notif, Notification)
        assert notif.title == "Test"
        assert notif.user_id == "teacher-001"

