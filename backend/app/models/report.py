from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum


class ReportType(str, Enum):
    COURSE_PERFORMANCE = "course_performance"
    STUDENT_PROGRESS = "student_progress"
    ENGAGEMENT = "engagement"
    COMPLETION_RATES = "completion_rates"
    CUSTOM = "custom"


class ReportFormat(str, Enum):
    JSON = "json"
    CSV = "csv"
    PDF = "pdf"
    EXCEL = "excel"


class ReportStatus(str, Enum):
    PENDING = "pending"
    GENERATING = "generating"
    COMPLETED = "completed"
    FAILED = "failed"


class ReportConfig(BaseModel):
    report_type: ReportType
    filters: Optional[Dict[str, Any]] = None
    date_range: Optional[Dict[str, str]] = None
    include_charts: bool = False
    role_context: Optional[str] = None


class Report(BaseModel):
    id: str
    user_id: str
    report_type: ReportType
    status: ReportStatus
    title: str
    description: Optional[str] = None
    config: ReportConfig
    data: Optional[Dict[str, Any]] = None
    created_at: datetime
    completed_at: Optional[datetime] = None
    expires_at: Optional[datetime] = None
    file_path: Optional[str] = None
    file_size: Optional[int] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": "report-001",
                "user_id": "teacher-001",
                "report_type": "course_performance",
                "status": "completed",
                "title": "eCommerce Course Performance Report",
                "description": "Detailed performance metrics for Q3 2025",
                "config": {
                    "report_type": "course_performance",
                    "filters": {"course_id": "course-001"},
                    "include_charts": True
                },
                "created_at": "2025-09-30T10:00:00Z",
                "completed_at": "2025-09-30T10:00:15Z"
            }
        }


class ScheduledReport(BaseModel):
    id: str
    user_id: str
    report_config: ReportConfig
    schedule: str  # cron expression
    enabled: bool = True
    last_run: Optional[datetime] = None
    next_run: Optional[datetime] = None

