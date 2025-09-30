from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime


class CourseMetrics(BaseModel):
    course_id: str
    course_name: str
    total_students: int
    active_students: int
    completion_rate: float
    average_grade: float
    assignments_total: int
    assignments_completed: int
    engagement_score: float
    
    class Config:
        json_schema_extra = {
            "example": {
                "course_id": "123456789",
                "course_name": "eCommerce Specialist",
                "total_students": 150,
                "active_students": 142,
                "completion_rate": 78.5,
                "average_grade": 8.2,
                "assignments_total": 45,
                "assignments_completed": 38,
                "engagement_score": 85.3
            }
        }


class StudentMetrics(BaseModel):
    student_id: str
    student_name: str
    courses_enrolled: int
    courses_completed: int
    overall_progress: float
    average_grade: float
    assignments_completed: int
    assignments_pending: int
    streak_days: int
    
    class Config:
        json_schema_extra = {
            "example": {
                "student_id": "student-001",
                "student_name": "Ana Martinez",
                "courses_enrolled": 2,
                "courses_completed": 1,
                "overall_progress": 67.5,
                "average_grade": 8.7,
                "assignments_completed": 28,
                "assignments_pending": 12,
                "streak_days": 15
            }
        }


class DashboardMetrics(BaseModel):
    role: str
    user_id: str
    overview: Dict[str, Any]
    metrics: Dict[str, Any]
    trends: Optional[Dict[str, Any]] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "role": "teacher",
                "user_id": "teacher-001",
                "overview": {
                    "total_courses": 3,
                    "total_students": 150,
                    "active_assignments": 12
                },
                "metrics": {
                    "average_completion": 78.5,
                    "average_grade": 8.2
                }
            }
        }

