from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.services.reports_service import ReportsService
from app.models.report import ReportType, ReportConfig
from app.schemas.response_schema import create_success_response
from app.middleware.auth_middleware import get_current_user
from app.models.user import User

router = APIRouter()


def get_reports_service():
    """Dependency to get ReportsService instance."""
    return ReportsService()


@router.post("/reports/generate", response_model=dict)
async def generate_report(
    report_type: str,
    title: str,
    filters: dict = None,
    current_user: User = Depends(get_current_user),
    reports_service: ReportsService = Depends(get_reports_service)
):
    """
    Generate a new report.
    
    Requires authentication.
    """
    config = ReportConfig(
        report_type=ReportType(report_type),
        filters=filters
    )
    
    report = reports_service.generate_report(
        user_id=current_user.id,
        title=title,
        config=config
    )
    
    report_data = {
        "id": report.id,
        "title": report.title,
        "type": report.report_type.value,
        "status": report.status.value,
        "created_at": report.created_at.isoformat(),
        "data": report.data
    }
    
    return create_success_response(report_data).model_dump()


@router.get("/reports", response_model=dict)
async def list_reports(
    current_user: User = Depends(get_current_user),
    reports_service: ReportsService = Depends(get_reports_service)
):
    """
    List all reports for current user.
    
    Requires authentication.
    """
    reports = reports_service.list_reports(current_user.id)
    
    reports_data = [
        {
            "id": r.id,
            "title": r.title,
            "type": r.report_type.value,
            "status": r.status.value,
            "created_at": r.created_at.isoformat()
        }
        for r in reports
    ]
    
    response_data = {
        "reports": reports_data,
        "total": len(reports_data)
    }
    
    return create_success_response(response_data).model_dump()


@router.get("/reports/{report_id}/export", response_model=dict)
async def export_report(
    report_id: str,
    format: str = "json",
    current_user: User = Depends(get_current_user),
    reports_service: ReportsService = Depends(get_reports_service)
):
    """
    Export a report in specified format.
    
    Requires authentication.
    """
    exported = reports_service.export_report(report_id, current_user.id, format)
    
    if not exported:
        raise HTTPException(status_code=404, detail="Report not found")
    
    return create_success_response(exported).model_dump()

