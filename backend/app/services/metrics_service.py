import json
import os
from typing import Dict, Any, List
from app.models.metric import CourseMetrics, StudentMetrics, DashboardMetrics
from app.services.classroom_service import ClassroomService


class MetricsService:
    """Service for calculating educational metrics and KPIs."""
    
    def __init__(self):
        """Initialize MetricsService."""
        self.classroom_service = ClassroomService(mode="MOCK")
        self.students_file = os.path.join(
            os.path.dirname(__file__), "..", "data", "mock_students.json"
        )
    
    def _load_progress_data(self) -> List[dict]:
        """Load student progress data from mock file."""
        try:
            with open(self.students_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get("progress", [])
        except FileNotFoundError:
            return []
    
    def get_course_metrics(self, course_id: str) -> CourseMetrics:
        """
        Calculate metrics for a specific course.
        
        Args:
            course_id: The course ID to calculate metrics for
            
        Returns:
            CourseMetrics object with calculated metrics
        """
        course = self.classroom_service.get_course_by_id(course_id)
        students = self.classroom_service.get_students_by_course(course_id)
        progress_data = self._load_progress_data()
        
        # Filter progress for this course
        course_progress = [p for p in progress_data if p.get("course_id") == course_id]
        
        # Calculate metrics
        total_students = len(students)
        active_students = len([p for p in course_progress if p.get("progress", 0) > 0])
        
        if course_progress:
            avg_completion = sum(p.get("progress", 0) for p in course_progress) / len(course_progress)
            avg_grade = sum(p.get("grade", 0) for p in course_progress) / len(course_progress)
            total_completed = sum(p.get("assignments_completed", 0) for p in course_progress)
            total_assignments = sum(p.get("assignments_total", 0) for p in course_progress)
        else:
            avg_completion = 0
            avg_grade = 0
            total_completed = 0
            total_assignments = 30
        
        # Engagement score (simplified calculation)
        engagement_score = (avg_completion * 0.6 + (avg_grade / 10 * 100) * 0.4) if avg_completion > 0 else 0
        
        return CourseMetrics(
            course_id=course_id,
            course_name=course.name if course else "Unknown Course",
            total_students=total_students,
            active_students=active_students,
            completion_rate=avg_completion,
            average_grade=avg_grade,
            assignments_total=total_assignments,
            assignments_completed=total_completed,
            engagement_score=engagement_score
        )
    
    def get_student_metrics(self, student_id: str) -> StudentMetrics:
        """
        Calculate metrics for a specific student.
        
        Args:
            student_id: The student ID to calculate metrics for
            
        Returns:
            StudentMetrics object with calculated metrics
        """
        progress_data = self._load_progress_data()
        student_progress = [p for p in progress_data if p.get("student_id") == student_id]
        
        if not student_progress:
            # Return default metrics if no data found
            return StudentMetrics(
                student_id=student_id,
                student_name="Unknown Student",
                courses_enrolled=0,
                courses_completed=0,
                overall_progress=0.0,
                average_grade=0.0,
                assignments_completed=0,
                assignments_pending=0,
                streak_days=0
            )
        
        # Calculate metrics
        courses_enrolled = len(student_progress)
        courses_completed = len([p for p in student_progress if p.get("progress", 0) >= 100])
        overall_progress = sum(p.get("progress", 0) for p in student_progress) / courses_enrolled
        average_grade = sum(p.get("grade", 0) for p in student_progress) / courses_enrolled
        assignments_completed = sum(p.get("assignments_completed", 0) for p in student_progress)
        assignments_total = sum(p.get("assignments_total", 0) for p in student_progress)
        assignments_pending = assignments_total - assignments_completed
        
        # Streak days (simplified)
        streak_days = 15  # Mock value
        
        return StudentMetrics(
            student_id=student_id,
            student_name=student_progress[0].get("student_name", "Unknown Student"),
            courses_enrolled=courses_enrolled,
            courses_completed=courses_completed,
            overall_progress=overall_progress,
            average_grade=average_grade,
            assignments_completed=assignments_completed,
            assignments_pending=assignments_pending,
            streak_days=streak_days
        )
    
    def get_dashboard_metrics(self, user_id: str, role: str) -> DashboardMetrics:
        """
        Get dashboard metrics tailored for a specific user role.
        
        Args:
            user_id: The user ID
            role: The user role (administrator, coordinator, teacher, student)
            
        Returns:
            DashboardMetrics object with role-specific metrics
        """
        if role == "administrator":
            return self._get_admin_dashboard(user_id)
        elif role == "coordinator":
            return self._get_coordinator_dashboard(user_id)
        elif role == "teacher":
            return self._get_teacher_dashboard(user_id)
        elif role == "student":
            return self._get_student_dashboard(user_id)
        else:
            return DashboardMetrics(
                role=role,
                user_id=user_id,
                overview={},
                metrics={}
            )
    
    def _get_admin_dashboard(self, user_id: str) -> DashboardMetrics:
        """Get metrics for administrator dashboard."""
        courses = self.classroom_service.get_courses()
        
        overview = {
            "total_courses": len(courses),
            "active_courses": len([c for c in courses if c.course_state == "ACTIVE"]),
            "total_students": 150,  # Mock value
            "total_teachers": 5  # Mock value
        }
        
        metrics = {
            "average_completion": 75.5,
            "average_grade": 8.2,
            "engagement_score": 82.3
        }
        
        return DashboardMetrics(
            role="administrator",
            user_id=user_id,
            overview=overview,
            metrics=metrics
        )
    
    def _get_coordinator_dashboard(self, user_id: str) -> DashboardMetrics:
        """Get metrics for coordinator dashboard."""
        overview = {
            "assigned_courses": 5,
            "total_students": 75,
            "active_teachers": 3
        }
        
        metrics = {
            "average_progress": 72.8,
            "completion_rate": 68.5
        }
        
        return DashboardMetrics(
            role="coordinator",
            user_id=user_id,
            overview=overview,
            metrics=metrics
        )
    
    def _get_teacher_dashboard(self, user_id: str) -> DashboardMetrics:
        """Get metrics for teacher dashboard."""
        courses = self.classroom_service.get_courses()
        # Filter courses owned by this teacher
        teacher_courses = [c for c in courses if c.owner_id == user_id]
        
        overview = {
            "total_courses": len(teacher_courses),
            "total_students": 150,
            "active_assignments": 12
        }
        
        metrics = {
            "average_completion": 78.5,
            "average_grade": 8.2,
            "pending_reviews": 8
        }
        
        return DashboardMetrics(
            role="teacher",
            user_id=user_id,
            overview=overview,
            metrics=metrics
        )
    
    def _get_student_dashboard(self, user_id: str) -> DashboardMetrics:
        """Get metrics for student dashboard."""
        student_metrics = self.get_student_metrics(user_id)
        
        overview = {
            "courses_enrolled": student_metrics.courses_enrolled,
            "overall_progress": student_metrics.overall_progress,
            "pending_assignments": student_metrics.assignments_pending
        }
        
        metrics = {
            "average_grade": student_metrics.average_grade,
            "completed_assignments": student_metrics.assignments_completed,
            "streak_days": student_metrics.streak_days
        }
        
        return DashboardMetrics(
            role="student",
            user_id=user_id,
            overview=overview,
            metrics=metrics
        )

