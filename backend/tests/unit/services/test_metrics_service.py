import pytest
from app.services.metrics_service import MetricsService
from app.models.metric import CourseMetrics, StudentMetrics, DashboardMetrics


class TestMetricsService:
    """Test suite for MetricsService following TDD methodology."""
    
    @pytest.fixture
    def metrics_service(self):
        """Create a MetricsService instance for testing."""
        return MetricsService()
    
    def test_get_course_metrics_returns_metrics_object(self, metrics_service):
        """Test that get_course_metrics returns CourseMetrics object."""
        metrics = metrics_service.get_course_metrics("course-001")
        assert isinstance(metrics, CourseMetrics)
        assert metrics.course_id == "course-001"
    
    def test_get_course_metrics_calculates_totals(self, metrics_service):
        """Test that course metrics calculates student totals."""
        metrics = metrics_service.get_course_metrics("course-001")
        assert metrics.total_students > 0
        assert metrics.active_students >= 0
        assert metrics.active_students <= metrics.total_students
    
    def test_get_course_metrics_calculates_rates(self, metrics_service):
        """Test that course metrics calculates rates as percentages."""
        metrics = metrics_service.get_course_metrics("course-001")
        assert 0 <= metrics.completion_rate <= 100
        assert metrics.average_grade >= 0
        assert 0 <= metrics.engagement_score <= 100
    
    def test_get_student_metrics_returns_metrics_object(self, metrics_service):
        """Test that get_student_metrics returns StudentMetrics object."""
        metrics = metrics_service.get_student_metrics("student-001")
        assert isinstance(metrics, StudentMetrics)
        assert metrics.student_id == "student-001"
    
    def test_get_student_metrics_calculates_progress(self, metrics_service):
        """Test that student metrics calculates progress correctly."""
        metrics = metrics_service.get_student_metrics("student-001")
        assert metrics.courses_enrolled >= metrics.courses_completed
        assert 0 <= metrics.overall_progress <= 100
        assert metrics.average_grade >= 0
    
    def test_get_dashboard_metrics_admin_returns_overview(self, metrics_service):
        """Test that get_dashboard_metrics for admin returns overview."""
        metrics = metrics_service.get_dashboard_metrics("admin-001", "administrator")
        assert isinstance(metrics, DashboardMetrics)
        assert metrics.role == "administrator"
        assert "overview" in metrics.model_dump()
    
    def test_get_dashboard_metrics_teacher_returns_course_data(self, metrics_service):
        """Test that get_dashboard_metrics for teacher returns course data."""
        metrics = metrics_service.get_dashboard_metrics("teacher-001", "teacher")
        assert isinstance(metrics, DashboardMetrics)
        assert metrics.role == "teacher"
        assert "metrics" in metrics.model_dump()
    
    def test_get_dashboard_metrics_student_returns_personal_data(self, metrics_service):
        """Test that get_dashboard_metrics for student returns personal data."""
        metrics = metrics_service.get_dashboard_metrics("student-001", "student")
        assert isinstance(metrics, DashboardMetrics)
        assert metrics.role == "student"
        assert metrics.user_id == "student-001"

