import uuid
from typing import List, Optional, Dict, Any
from datetime import datetime, timedelta
from app.models.report import Report, ReportType, ReportConfig, ReportStatus, ReportFormat
from app.services.metrics_service import MetricsService
from app.services.classroom_service import ClassroomService


class ReportsService:
    """
    Service for generating and managing reports.
    Supports multiple report types and export formats.
    """
    
    def __init__(self):
        """Initialize ReportsService."""
        self.metrics_service = MetricsService()
        self.classroom_service = ClassroomService()
        self._reports_store: Dict[str, Report] = {}
    
    def generate_report(
        self,
        user_id: str,
        title: str,
        config: ReportConfig,
        description: Optional[str] = None
    ) -> Report:
        """
        Generate a new report.
        
        Args:
            user_id: The user generating the report
            title: Report title
            config: Report configuration
            description: Optional description
            
        Returns:
            Generated Report object
        """
        report_id = f"report-{uuid.uuid4().hex[:8]}"
        
        # Generate report data based on type
        report_data = self._generate_report_data(config, user_id)
        
        report = Report(
            id=report_id,
            user_id=user_id,
            report_type=config.report_type,
            status=ReportStatus.COMPLETED,
            title=title,
            description=description,
            config=config,
            data=report_data,
            created_at=datetime.now(),
            completed_at=datetime.now(),
            expires_at=datetime.now() + timedelta(days=30)
        )
        
        # Store report
        self._reports_store[report_id] = report
        
        return report
    
    def _generate_report_data(self, config: ReportConfig, user_id: str) -> Dict[str, Any]:
        """Generate report data based on configuration."""
        if config.report_type == ReportType.COURSE_PERFORMANCE:
            return self._generate_course_performance_report(config)
        elif config.report_type == ReportType.STUDENT_PROGRESS:
            return self._generate_student_progress_report(config)
        elif config.report_type == ReportType.ENGAGEMENT:
            return self._generate_engagement_report(config)
        elif config.report_type == ReportType.COMPLETION_RATES:
            return self._generate_completion_rates_report(config)
        else:
            return {"message": "Custom report data"}
    
    def _generate_course_performance_report(self, config: ReportConfig) -> Dict[str, Any]:
        """Generate course performance report data."""
        course_id = config.filters.get("course_id") if config.filters else "course-001"
        metrics = self.metrics_service.get_course_metrics(course_id)
        
        return {
            "course_id": metrics.course_id,
            "course_name": metrics.course_name,
            "metrics": {
                "total_students": metrics.total_students,
                "active_students": metrics.active_students,
                "completion_rate": metrics.completion_rate,
                "average_grade": metrics.average_grade,
                "engagement_score": metrics.engagement_score
            },
            "summary": f"Course has {metrics.total_students} students with {metrics.completion_rate:.1f}% completion rate"
        }
    
    def _generate_student_progress_report(self, config: ReportConfig) -> Dict[str, Any]:
        """Generate student progress report data."""
        student_id = config.filters.get("student_id") if config.filters else "student-001"
        metrics = self.metrics_service.get_student_metrics(student_id)
        
        return {
            "student_id": metrics.student_id,
            "student_name": metrics.student_name,
            "metrics": {
                "courses_enrolled": metrics.courses_enrolled,
                "overall_progress": metrics.overall_progress,
                "average_grade": metrics.average_grade,
                "assignments_completed": metrics.assignments_completed
            },
            "summary": f"{metrics.student_name} has {metrics.overall_progress:.1f}% overall progress"
        }
    
    def _generate_engagement_report(self, config: ReportConfig) -> Dict[str, Any]:
        """Generate engagement report data."""
        courses = self.classroom_service.get_courses()
        
        return {
            "total_courses": len(courses),
            "engagement_metrics": {
                "average_engagement": 82.5,
                "active_users": 145,
                "total_activities": 1250
            },
            "summary": "Overall engagement is 82.5%"
        }
    
    def _generate_completion_rates_report(self, config: ReportConfig) -> Dict[str, Any]:
        """Generate completion rates report data."""
        return {
            "completion_metrics": {
                "overall_rate": 75.5,
                "on_time_rate": 68.3,
                "late_rate": 7.2
            },
            "by_course": [
                {"course": "eCommerce", "rate": 85.0},
                {"course": "Web Dev", "rate": 72.0},
                {"course": "Marketing", "rate": 68.0}
            ],
            "summary": "Average completion rate is 75.5%"
        }
    
    def get_report(self, report_id: str, user_id: str) -> Optional[Report]:
        """
        Get a report by ID.
        
        Args:
            report_id: The report ID
            user_id: The user ID (for security)
            
        Returns:
            Report object if found and belongs to user, None otherwise
        """
        report = self._reports_store.get(report_id)
        
        if report and report.user_id == user_id:
            return report
        
        return None
    
    def list_reports(self, user_id: str) -> List[Report]:
        """
        List all reports for a user.
        
        Args:
            user_id: The user ID
            
        Returns:
            List of Report objects
        """
        user_reports = [
            report for report in self._reports_store.values()
            if report.user_id == user_id
        ]
        
        # Sort by created_at descending
        user_reports.sort(key=lambda x: x.created_at, reverse=True)
        
        return user_reports
    
    def export_report(
        self, 
        report_id: str, 
        user_id: str, 
        format: str = "json"
    ) -> Optional[Dict[str, Any]]:
        """
        Export a report in specified format.
        
        Args:
            report_id: The report ID
            user_id: The user ID
            format: Export format (json, csv, pdf, excel)
            
        Returns:
            Exported data or None if report not found
        """
        report = self.get_report(report_id, user_id)
        
        if not report:
            return None
        
        # For now, return JSON format
        # TODO: Implement actual PDF/Excel generation
        export_data = {
            "report_id": report.id,
            "title": report.title,
            "generated_at": report.created_at.isoformat(),
            "format": format,
            "data": report.data
        }
        
        return export_data

