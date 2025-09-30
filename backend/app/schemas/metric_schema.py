from pydantic import BaseModel
from typing import Dict, Any, Optional


class CourseMetricsResponse(BaseModel):
    course_id: str
    course_name: str
    total_students: int
    active_students: int
    completion_rate: float
    average_grade: float
    assignments_total: int
    assignments_completed: int
    engagement_score: float


class StudentMetricsResponse(BaseModel):
    student_id: str
    student_name: str
    courses_enrolled: int
    courses_completed: int
    overall_progress: float
    average_grade: float
    assignments_completed: int
    assignments_pending: int
    streak_days: int


class DashboardMetricsResponse(BaseModel):
    role: str
    user_id: str
    overview: Dict[str, Any]
    metrics: Dict[str, Any]
    trends: Optional[Dict[str, Any]] = None

