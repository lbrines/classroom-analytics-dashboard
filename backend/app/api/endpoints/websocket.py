from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
import json
from app.services.websocket_service import websocket_service
from app.core.config import settings
from app.models.user import User

router = APIRouter()
security = HTTPBearer(auto_error=False)


async def get_current_user_websocket(
    credentials: HTTPAuthorizationCredentials = Depends(security)
) -> User:
    """Extract and validate user from WebSocket token."""
    if not credentials:
        raise HTTPException(status_code=401, detail="Authentication required")
    
    try:
        payload = jwt.decode(
            credentials.credentials,
            settings.secret_key,
            algorithms=[settings.algorithm]
        )
        user_id: str = payload.get("sub")
        email: str = payload.get("email")
        role: str = payload.get("role")
        
        if user_id is None or email is None or role is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        
        return User(
            id=user_id,
            email=email,
            role=role,
            name=payload.get("name", ""),
            active=True
        )
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


@router.websocket("/ws/notifications")
async def websocket_notifications_endpoint(
    websocket: WebSocket,
    token: str = None
):
    """
    WebSocket endpoint for real-time notifications.
    
    Query parameters:
    - token: JWT token for authentication
    
    Message format:
    {
        "type": "ping|subscribe|mark_read",
        "data": {...}
    }
    """
    if not token:
        await websocket.close(code=1008, reason="Authentication token required")
        return
    
    try:
        # Decode token to get user info
        payload = jwt.decode(
            token,
            settings.secret_key,
            algorithms=[settings.algorithm]
        )
        user_id = payload.get("sub")
        user_role = payload.get("role")
        
        if not user_id or not user_role:
            await websocket.close(code=1008, reason="Invalid token")
            return
        
        # Handle WebSocket connection
        await websocket_service.handle_connection(websocket, user_id)
        
    except jwt.PyJWTError:
        await websocket.close(code=1008, reason="Invalid token")
    except WebSocketDisconnect:
        pass
    except Exception as e:
        print(f"WebSocket error: {e}")
        await websocket.close(code=1011, reason="Internal server error")


@router.get("/ws/stats")
async def get_websocket_stats():
    """Get WebSocket connection statistics (for monitoring)."""
    stats = await websocket_service.get_connection_manager().get_connection_stats()
    return {
        "status": "success",
        "data": stats
    }


@router.post("/ws/broadcast")
async def broadcast_message(
    message: str,
    role: str = None,
    current_user: User = Depends(get_current_user_websocket)
):
    """
    Broadcast system message to all users or specific role.
    Requires authentication.
    """
    # Only admins and coordinators can broadcast
    if current_user.role not in ["administrator", "coordinator"]:
        raise HTTPException(
            status_code=403,
            detail="Only administrators and coordinators can broadcast messages"
        )
    
    await websocket_service.broadcast_system_message(message, role)
    
    return {
        "status": "success",
        "message": f"Message broadcasted to {role or 'all users'}"
    }


@router.post("/ws/send-alert/{user_id}")
async def send_alert_to_user(
    user_id: str,
    alert_type: str,
    message: str,
    current_user: User = Depends(get_current_user_websocket)
):
    """
    Send alert to specific user.
    Requires authentication.
    """
    # Users can only send alerts to themselves or admins can send to anyone
    if current_user.id != user_id and current_user.role != "administrator":
        raise HTTPException(
            status_code=403,
            detail="You can only send alerts to yourself"
        )
    
    await websocket_service.send_alert_to_user(user_id, alert_type, message)
    
    return {
        "status": "success",
        "message": f"Alert sent to user {user_id}"
    }

