from fastapi import APIRouter, Depends
from app.services.metrics_service import MetricsService
from app.schemas.metric_schema import DashboardMetricsResponse
from app.schemas.response_schema import create_success_response
from app.middleware.auth_middleware import get_current_user
from app.models.user import User

router = APIRouter()


def get_metrics_service():
    """Dependency to get MetricsService instance."""
    return MetricsService()


@router.get("/dashboard", response_model=dict)
async def get_dashboard_metrics(
    current_user: User = Depends(get_current_user),
    metrics_service: MetricsService = Depends(get_metrics_service)
):
    """
    Get dashboard metrics for the current user.
    
    Returns role-specific metrics based on user role.
    Requires authentication.
    """
    metrics = metrics_service.get_dashboard_metrics(
        user_id=current_user.id,
        role=current_user.role.value
    )
    
    dashboard_data = DashboardMetricsResponse(
        role=metrics.role,
        user_id=metrics.user_id,
        overview=metrics.overview,
        metrics=metrics.metrics,
        trends=metrics.trends
    ).model_dump()
    
    return create_success_response(dashboard_data).model_dump()


@router.get("/dashboard/{role}", response_model=dict)
async def get_role_dashboard_metrics(
    role: str,
    current_user: User = Depends(get_current_user),
    metrics_service: MetricsService = Depends(get_metrics_service)
):
    """
    Get dashboard metrics for a specific role.
    
    Only admins and coordinators can access other roles' dashboards.
    Requires authentication.
    """
    # Check permission
    if current_user.role.value not in ["administrator", "coordinator"]:
        if role != current_user.role.value:
            from fastapi import HTTPException
            raise HTTPException(
                status_code=403,
                detail="You don't have permission to view this dashboard"
            )
    
    metrics = metrics_service.get_dashboard_metrics(
        user_id=current_user.id,
        role=role
    )
    
    dashboard_data = DashboardMetricsResponse(
        role=metrics.role,
        user_id=metrics.user_id,
        overview=metrics.overview,
        metrics=metrics.metrics,
        trends=metrics.trends
    ).model_dump()
    
    return create_success_response(dashboard_data).model_dump()

