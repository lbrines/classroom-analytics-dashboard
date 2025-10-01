import asyncio
import json
import logging
from typing import Dict, List, Set, Optional, Any
from datetime import datetime
from fastapi import WebSocket, WebSocketDisconnect
from app.models.notification import Notification
from app.services.notification_service import NotificationService

logger = logging.getLogger(__name__)


class ConnectionManager:
    """Manages WebSocket connections and real-time notifications."""
    
    def __init__(self):
        # Store active connections by user_id
        self.active_connections: Dict[str, Set[WebSocket]] = {}
        # Store notification queue for each user
        self.notification_queues: Dict[str, List[Dict[str, Any]]] = {}
        self.notification_service = NotificationService()
    
    async def connect(self, websocket: WebSocket, user_id: str):
        """Accept a WebSocket connection and add to active connections."""
        await websocket.accept()
        
        if user_id not in self.active_connections:
            self.active_connections[user_id] = set()
            self.notification_queues[user_id] = []
        
        self.active_connections[user_id].add(websocket)
        
        # Send any queued notifications
        await self._send_queued_notifications(user_id)
        
        logger.info(f"User {user_id} connected. Total connections: {len(self.active_connections[user_id])}")
    
    async def disconnect(self, websocket: WebSocket, user_id: str):
        """Remove WebSocket connection."""
        if user_id in self.active_connections:
            self.active_connections[user_id].discard(websocket)
            
            # Clean up empty user connections
            if not self.active_connections[user_id]:
                del self.active_connections[user_id]
                if user_id in self.notification_queues:
                    del self.notification_queues[user_id]
        
        logger.info(f"User {user_id} disconnected")
    
    async def send_notification(self, user_id: str, notification: Notification):
        """Send notification to specific user."""
        notification_data = {
            "type": "notification",
            "data": {
                "id": notification.id,
                "title": notification.title,
                "message": notification.message,
                "type": notification.type.value,
                "priority": notification.priority.value,
                "created_at": notification.created_at.isoformat(),
                "data": notification.data,
                "actions": [action.model_dump() for action in (notification.actions or [])]
            }
        }
        
        await self._send_to_user(user_id, notification_data)
    
    async def send_system_alert(self, user_id: str, alert_type: str, message: str, data: Optional[Dict] = None):
        """Send system alert to specific user."""
        alert_data = {
            "type": "system_alert",
            "data": {
                "alert_type": alert_type,
                "message": message,
                "timestamp": datetime.now().isoformat(),
                "data": data or {}
            }
        }
        
        await self._send_to_user(user_id, alert_data)
    
    async def broadcast_to_role(self, role: str, message: Dict[str, Any]):
        """Broadcast message to all users with specific role."""
        # This would require user role lookup - simplified for now
        for user_id in self.active_connections.keys():
            await self._send_to_user(user_id, message)
    
    async def _send_to_user(self, user_id: str, message: Dict[str, Any]):
        """Send message to specific user."""
        if user_id not in self.active_connections:
            # Queue message for later delivery
            if user_id not in self.notification_queues:
                self.notification_queues[user_id] = []
            self.notification_queues[user_id].append(message)
            return
        
        # Send to all active connections for this user
        disconnected_connections = set()
        for websocket in self.active_connections[user_id]:
            try:
                await websocket.send_text(json.dumps(message))
            except WebSocketDisconnect:
                disconnected_connections.add(websocket)
            except Exception as e:
                logger.error(f"Error sending message to {user_id}: {e}")
                disconnected_connections.add(websocket)
        
        # Remove disconnected connections
        for websocket in disconnected_connections:
            self.active_connections[user_id].discard(websocket)
    
    async def _send_queued_notifications(self, user_id: str):
        """Send any queued notifications when user connects."""
        if user_id not in self.notification_queues:
            return
        
        queued_notifications = self.notification_queues[user_id]
        if not queued_notifications:
            return
        
        for notification in queued_notifications:
            await self._send_to_user(user_id, notification)
        
        # Clear queue after sending
        self.notification_queues[user_id] = []
    
    async def get_connection_stats(self) -> Dict[str, Any]:
        """Get WebSocket connection statistics."""
        total_connections = sum(len(connections) for connections in self.active_connections.values())
        total_users = len(self.active_connections)
        
        return {
            "total_connections": total_connections,
            "total_users": total_users,
            "active_users": list(self.active_connections.keys()),
            "queued_notifications": {
                user_id: len(queue) 
                for user_id, queue in self.notification_queues.items()
            }
        }


class WebSocketService:
    """Service for managing WebSocket operations and real-time features."""
    
    def __init__(self):
        self.connection_manager = ConnectionManager()
    
    async def handle_connection(self, websocket: WebSocket, user_id: str):
        """Handle WebSocket connection lifecycle."""
        await self.connection_manager.connect(websocket, user_id)
        
        try:
            while True:
                # Keep connection alive and handle incoming messages
                data = await websocket.receive_text()
                message = json.loads(data)
                
                # Handle different message types
                if message.get("type") == "ping":
                    await websocket.send_text(json.dumps({"type": "pong", "timestamp": datetime.now().isoformat()}))
                elif message.get("type") == "subscribe":
                    # Handle subscription to specific notification types
                    await self._handle_subscription(websocket, user_id, message)
                elif message.get("type") == "mark_read":
                    # Handle marking notifications as read
                    await self._handle_mark_read(user_id, message)
        
        except WebSocketDisconnect:
            await self.connection_manager.disconnect(websocket, user_id)
        except Exception as e:
            logger.error(f"WebSocket error for user {user_id}: {e}")
            await self.connection_manager.disconnect(websocket, user_id)
    
    async def _handle_subscription(self, websocket: WebSocket, user_id: str, message: Dict[str, Any]):
        """Handle notification type subscription."""
        # Store subscription preferences for user
        # This would be persisted in a real implementation
        logger.info(f"User {user_id} subscribed to: {message.get('data', {})}")
        
        await websocket.send_text(json.dumps({
            "type": "subscription_confirmed",
            "data": message.get("data", {})
        }))
    
    async def _handle_mark_read(self, user_id: str, message: Dict[str, Any]):
        """Handle marking notification as read."""
        notification_id = message.get("data", {}).get("notification_id")
        if notification_id:
            success = self.connection_manager.notification_service.mark_as_read(notification_id, user_id)
            logger.info(f"Marked notification {notification_id} as read for user {user_id}: {success}")
    
    async def send_notification_to_user(self, user_id: str, notification: Notification):
        """Send notification to specific user via WebSocket."""
        await self.connection_manager.send_notification(user_id, notification)
    
    async def send_alert_to_user(self, user_id: str, alert_type: str, message: str, data: Optional[Dict] = None):
        """Send alert to specific user via WebSocket."""
        await self.connection_manager.send_system_alert(user_id, alert_type, message, data)
    
    async def broadcast_system_message(self, message: str, role: Optional[str] = None):
        """Broadcast system message to all users or specific role."""
        broadcast_data = {
            "type": "system_broadcast",
            "data": {
                "message": message,
                "timestamp": datetime.now().isoformat(),
                "role": role
            }
        }
        
        if role:
            await self.connection_manager.broadcast_to_role(role, broadcast_data)
        else:
            # Broadcast to all users
            for user_id in self.connection_manager.active_connections.keys():
                await self.connection_manager._send_to_user(user_id, broadcast_data)
    
    def get_connection_manager(self) -> ConnectionManager:
        """Get the connection manager instance."""
        return self.connection_manager


# Global WebSocket service instance
websocket_service = WebSocketService()

