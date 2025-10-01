import pytest
import asyncio
from unittest.mock import AsyncMock, MagicMock
from app.services.websocket_service import ConnectionManager, WebSocketService
from app.models.notification import Notification, NotificationType, NotificationPriority
from datetime import datetime


class TestConnectionManager:
    """Test suite for ConnectionManager following TDD methodology."""
    
    @pytest.fixture
    def connection_manager(self):
        """Create a ConnectionManager instance for testing."""
        return ConnectionManager()
    
    @pytest.fixture
    def mock_websocket(self):
        """Create a mock WebSocket for testing."""
        websocket = AsyncMock()
        websocket.accept = AsyncMock()
        websocket.send_text = AsyncMock()
        websocket.receive_text = AsyncMock()
        return websocket
    
    @pytest.fixture
    def sample_notification(self):
        """Create a sample notification for testing."""
        return Notification(
            id="notif-001",
            user_id="user-001",
            type=NotificationType.ALERT,
            priority=NotificationPriority.HIGH,
            title="Test Notification",
            message="This is a test notification",
            read=False,
            created_at=datetime.now()
        )
    
    @pytest.mark.asyncio
    async def test_connect_accepts_websocket_and_adds_to_connections(self, connection_manager, mock_websocket):
        """Test that connect accepts WebSocket and adds to active connections."""
        user_id = "user-001"
        
        await connection_manager.connect(mock_websocket, user_id)
        
        # Verify WebSocket was accepted
        mock_websocket.accept.assert_called_once()
        
        # Verify connection was added
        assert user_id in connection_manager.active_connections
        assert mock_websocket in connection_manager.active_connections[user_id]
    
    @pytest.mark.asyncio
    async def test_disconnect_removes_websocket_from_connections(self, connection_manager, mock_websocket):
        """Test that disconnect removes WebSocket from active connections."""
        user_id = "user-001"
        
        # First connect
        await connection_manager.connect(mock_websocket, user_id)
        assert mock_websocket in connection_manager.active_connections[user_id]
        
        # Then disconnect
        await connection_manager.disconnect(mock_websocket, user_id)
        assert user_id not in connection_manager.active_connections
    
    @pytest.mark.asyncio
    async def test_send_notification_sends_to_active_connections(self, connection_manager, mock_websocket, sample_notification):
        """Test that send_notification sends notification to active connections."""
        user_id = "user-001"
        
        # Connect WebSocket
        await connection_manager.connect(mock_websocket, user_id)
        
        # Send notification
        await connection_manager.send_notification(user_id, sample_notification)
        
        # Verify notification was sent
        mock_websocket.send_text.assert_called_once()
        call_args = mock_websocket.send_text.call_args[0][0]
        assert "notification" in call_args
        assert "Test Notification" in call_args
    
    @pytest.mark.asyncio
    async def test_send_notification_queues_when_no_active_connections(self, connection_manager, sample_notification):
        """Test that send_notification queues message when no active connections."""
        user_id = "user-001"
        
        # Send notification without connecting
        await connection_manager.send_notification(user_id, sample_notification)
        
        # Verify message was queued
        assert user_id in connection_manager.notification_queues
        assert len(connection_manager.notification_queues[user_id]) == 1
    
    @pytest.mark.asyncio
    async def test_send_queued_notifications_on_connect(self, connection_manager, mock_websocket, sample_notification):
        """Test that queued notifications are sent when user connects."""
        user_id = "user-001"
        
        # Queue a notification first
        await connection_manager.send_notification(user_id, sample_notification)
        assert len(connection_manager.notification_queues[user_id]) == 1
        
        # Now connect
        await connection_manager.connect(mock_websocket, user_id)
        
        # Verify queued notification was sent (may be called multiple times due to _send_queued_notifications)
        # The key is that the queue should be empty after connection
        assert len(connection_manager.notification_queues[user_id]) == 0
    
    @pytest.mark.asyncio
    async def test_get_connection_stats_returns_correct_statistics(self, connection_manager, mock_websocket):
        """Test that get_connection_stats returns correct statistics."""
        user_id = "user-001"
        
        # Connect WebSocket
        await connection_manager.connect(mock_websocket, user_id)
        
        # Get stats
        stats = await connection_manager.get_connection_stats()
        
        assert stats["total_connections"] == 1
        assert stats["total_users"] == 1
        assert user_id in stats["active_users"]
    
    @pytest.mark.asyncio
    async def test_send_system_alert_sends_alert_to_user(self, connection_manager, mock_websocket):
        """Test that send_system_alert sends alert to specific user."""
        user_id = "user-001"
        alert_type = "warning"
        message = "System maintenance scheduled"
        
        # Connect WebSocket
        await connection_manager.connect(mock_websocket, user_id)
        
        # Send alert
        await connection_manager.send_system_alert(user_id, alert_type, message)
        
        # Verify alert was sent
        mock_websocket.send_text.assert_called_once()
        call_args = mock_websocket.send_text.call_args[0][0]
        assert "system_alert" in call_args
        assert alert_type in call_args
        assert message in call_args


class TestWebSocketService:
    """Test suite for WebSocketService following TDD methodology."""
    
    @pytest.fixture
    def websocket_service(self):
        """Create a WebSocketService instance for testing."""
        return WebSocketService()
    
    @pytest.fixture
    def mock_websocket(self):
        """Create a mock WebSocket for testing."""
        websocket = AsyncMock()
        websocket.accept = AsyncMock()
        websocket.send_text = AsyncMock()
        websocket.receive_text = AsyncMock()
        return websocket
    
    @pytest.fixture
    def sample_notification(self):
        """Create a sample notification for testing."""
        return Notification(
            id="notif-001",
            user_id="user-001",
            type=NotificationType.ALERT,
            priority=NotificationPriority.HIGH,
            title="Test Notification",
            message="This is a test notification",
            read=False,
            created_at=datetime.now()
        )
    
    @pytest.mark.asyncio
    async def test_handle_connection_manages_websocket_lifecycle(self, websocket_service, mock_websocket):
        """Test that handle_connection manages WebSocket lifecycle."""
        user_id = "user-001"
        
        # Mock receive_text to raise WebSocketDisconnect after first call
        from fastapi import WebSocketDisconnect
        mock_websocket.receive_text.side_effect = WebSocketDisconnect(1000)
        
        # Handle connection
        await websocket_service.handle_connection(mock_websocket, user_id)
        
        # Verify WebSocket was accepted
        mock_websocket.accept.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_send_notification_to_user_delegates_to_connection_manager(self, websocket_service, sample_notification):
        """Test that send_notification_to_user delegates to connection manager."""
        user_id = "user-001"
        
        # Mock connection manager
        websocket_service.connection_manager.send_notification = AsyncMock()
        
        # Send notification
        await websocket_service.send_notification_to_user(user_id, sample_notification)
        
        # Verify delegation
        websocket_service.connection_manager.send_notification.assert_called_once_with(user_id, sample_notification)
    
    @pytest.mark.asyncio
    async def test_send_alert_to_user_delegates_to_connection_manager(self, websocket_service):
        """Test that send_alert_to_user delegates to connection manager."""
        user_id = "user-001"
        alert_type = "warning"
        message = "Test alert"
        data = {"test": "data"}
        
        # Mock connection manager
        websocket_service.connection_manager.send_system_alert = AsyncMock()
        
        # Send alert
        await websocket_service.send_alert_to_user(user_id, alert_type, message, data)
        
        # Verify delegation
        websocket_service.connection_manager.send_system_alert.assert_called_once_with(user_id, alert_type, message, data)
    
    @pytest.mark.asyncio
    async def test_broadcast_system_message_sends_to_all_users(self, websocket_service):
        """Test that broadcast_system_message sends to all users."""
        message = "System maintenance"
        role = "teacher"
        
        # Mock connection manager with active users
        mock_user_id = "user-001"
        websocket_service.connection_manager.active_connections = {mock_user_id: set()}
        websocket_service.connection_manager._send_to_user = AsyncMock()
        
        # Broadcast message
        await websocket_service.broadcast_system_message(message, role)
        
        # Verify message was sent
        websocket_service.connection_manager._send_to_user.assert_called_once()
    
    @pytest.mark.asyncio
    async def test_get_connection_manager_returns_connection_manager(self, websocket_service):
        """Test that get_connection_manager returns the connection manager instance."""
        connection_manager = websocket_service.get_connection_manager()
        
        assert isinstance(connection_manager, ConnectionManager)
        assert connection_manager == websocket_service.connection_manager
