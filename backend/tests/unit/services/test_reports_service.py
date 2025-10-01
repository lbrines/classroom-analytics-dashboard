import pytest
from app.services.reports_service import ReportsService
from app.models.report import Report, ReportType, ReportConfig, ReportStatus


class TestReportsService:
    """Test suite for ReportsService following TDD methodology."""
    
    @pytest.fixture
    def reports_service(self):
        """Create a ReportsService instance for testing."""
        return ReportsService()
    
    def test_generate_report_returns_report_object(self, reports_service):
        """Test that generate_report returns a Report object."""
        config = ReportConfig(report_type=ReportType.COURSE_PERFORMANCE)
        report = reports_service.generate_report(
            user_id="teacher-001",
            title="Test Report",
            config=config
        )
        assert isinstance(report, Report)
        assert report.title == "Test Report"
    
    def test_generate_report_has_completed_status(self, reports_service):
        """Test that generated report has completed status."""
        config = ReportConfig(report_type=ReportType.STUDENT_PROGRESS)
        report = reports_service.generate_report(
            user_id="teacher-001",
            title="Progress Report",
            config=config
        )
        assert report.status == ReportStatus.COMPLETED
        assert report.completed_at is not None
    
    def test_generate_report_includes_data(self, reports_service):
        """Test that generated report includes data."""
        config = ReportConfig(report_type=ReportType.ENGAGEMENT)
        report = reports_service.generate_report(
            user_id="teacher-001",
            title="Engagement Report",
            config=config
        )
        assert report.data is not None
        assert isinstance(report.data, dict)
    
    def test_get_report_by_id_returns_report(self, reports_service):
        """Test that get_report_by_id returns report for valid ID."""
        # First generate a report
        config = ReportConfig(report_type=ReportType.COURSE_PERFORMANCE)
        created = reports_service.generate_report("teacher-001", "Test", config)
        
        # Then retrieve it
        report = reports_service.get_report(created.id, "teacher-001")
        assert report is not None
        assert report.id == created.id
    
    def test_get_report_by_id_returns_none_for_invalid(self, reports_service):
        """Test that get_report_by_id returns None for invalid ID."""
        report = reports_service.get_report("invalid-id", "teacher-001")
        assert report is None
    
    def test_list_reports_returns_list(self, reports_service):
        """Test that list_reports returns list of reports."""
        reports = reports_service.list_reports("teacher-001")
        assert isinstance(reports, list)
    
    def test_export_report_returns_data(self, reports_service):
        """Test that export_report returns exportable data."""
        config = ReportConfig(report_type=ReportType.COURSE_PERFORMANCE)
        report = reports_service.generate_report("teacher-001", "Test", config)
        
        exported = reports_service.export_report(report.id, "teacher-001", "json")
        assert exported is not None
        assert isinstance(exported, dict)

