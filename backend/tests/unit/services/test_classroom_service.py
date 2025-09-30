import pytest
from app.services.classroom_service import ClassroomService
from app.models.course import Course, CourseState
from app.models.student import Student


class TestClassroomService:
    """Test suite for ClassroomService following TDD methodology."""
    
    @pytest.fixture
    def classroom_service(self):
        """Create a ClassroomService instance for testing."""
        return ClassroomService(mode="MOCK")
    
    def test_get_courses_returns_list(self, classroom_service):
        """Test that get_courses returns a list of courses."""
        courses = classroom_service.get_courses()
        assert isinstance(courses, list)
        assert len(courses) > 0
    
    def test_get_courses_returns_course_objects(self, classroom_service):
        """Test that get_courses returns Course objects."""
        courses = classroom_service.get_courses()
        assert all(isinstance(course, Course) for course in courses)
    
    def test_get_course_by_id_returns_course(self, classroom_service):
        """Test that get_course_by_id returns a specific course."""
        course = classroom_service.get_course_by_id("course-001")
        assert course is not None
        assert isinstance(course, Course)
        assert course.id == "course-001"
    
    def test_get_course_by_invalid_id_returns_none(self, classroom_service):
        """Test that get_course_by_id returns None for invalid ID."""
        course = classroom_service.get_course_by_id("invalid-id")
        assert course is None
    
    def test_get_students_by_course_returns_list(self, classroom_service):
        """Test that get_students_by_course returns a list of students."""
        students = classroom_service.get_students_by_course("course-001")
        assert isinstance(students, list)
        assert len(students) > 0
    
    def test_get_students_by_course_returns_student_objects(self, classroom_service):
        """Test that get_students_by_course returns Student objects."""
        students = classroom_service.get_students_by_course("course-001")
        assert all(isinstance(student, Student) for student in students)
    
    def test_get_students_by_invalid_course_returns_empty_list(self, classroom_service):
        """Test that get_students_by_course returns empty list for invalid course."""
        students = classroom_service.get_students_by_course("invalid-course")
        assert isinstance(students, list)
        assert len(students) == 0
    
    def test_sync_courses_returns_count(self, classroom_service):
        """Test that sync_courses returns the count of synced courses."""
        count = classroom_service.sync_courses()
        assert isinstance(count, int)
        assert count >= 0

