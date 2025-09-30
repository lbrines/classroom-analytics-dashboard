from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.services.classroom_service import ClassroomService
from app.schemas.student_schema import StudentResponse, StudentListResponse
from app.schemas.response_schema import create_success_response
from app.middleware.auth_middleware import get_current_user
from app.models.user import User

router = APIRouter()


def get_classroom_service():
    """Dependency to get ClassroomService instance."""
    return ClassroomService(mode="MOCK")


@router.get("/courses/{course_id}/students", response_model=dict)
async def get_course_students(
    course_id: str,
    current_user: User = Depends(get_current_user),
    classroom_service: ClassroomService = Depends(get_classroom_service)
):
    """
    Get all students enrolled in a specific course.
    
    Requires authentication.
    """
    # Verify course exists
    course = classroom_service.get_course_by_id(course_id)
    if not course:
        raise HTTPException(status_code=404, detail=f"Course {course_id} not found")
    
    students = classroom_service.get_students_by_course(course_id)
    
    students_data = [
        StudentResponse(
            user_id=student.user_id,
            full_name=student.full_name,
            email_address=student.email_address,
            course_id=student.course_id,
            profile_id=student.profile_id,
            photo_url=student.photo_url
        ).model_dump()
        for student in students
    ]
    
    response_data = {
        "students": students_data,
        "total": len(students_data),
        "course_id": course_id
    }
    
    return create_success_response(response_data).model_dump()

