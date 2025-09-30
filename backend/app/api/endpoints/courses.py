from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.services.classroom_service import ClassroomService
from app.schemas.course_schema import CourseResponse, CourseListResponse, CourseSyncResponse
from app.schemas.response_schema import create_success_response
from app.middleware.auth_middleware import get_current_user
from app.models.user import User

router = APIRouter()


def get_classroom_service():
    """Dependency to get ClassroomService instance."""
    return ClassroomService(mode="MOCK")


@router.get("/courses", response_model=dict)
async def get_courses(
    current_user: User = Depends(get_current_user),
    classroom_service: ClassroomService = Depends(get_classroom_service)
):
    """
    Get all courses.
    
    Requires authentication.
    """
    courses = classroom_service.get_courses()
    
    courses_data = [
        CourseResponse(
            id=course.id,
            name=course.name,
            section=course.section,
            description=course.description,
            room=course.room,
            owner_id=course.owner_id,
            enrollment_code=course.enrollment_code,
            course_state=course.course_state.value,
            creation_time=course.creation_time,
            update_time=course.update_time,
            alternate_link=course.alternate_link
        ).model_dump()
        for course in courses
    ]
    
    response_data = {
        "courses": courses_data,
        "total": len(courses_data)
    }
    
    return create_success_response(response_data).model_dump()


@router.get("/courses/{course_id}", response_model=dict)
async def get_course(
    course_id: str,
    current_user: User = Depends(get_current_user),
    classroom_service: ClassroomService = Depends(get_classroom_service)
):
    """
    Get a specific course by ID.
    
    Requires authentication.
    """
    course = classroom_service.get_course_by_id(course_id)
    
    if not course:
        raise HTTPException(status_code=404, detail=f"Course {course_id} not found")
    
    course_data = CourseResponse(
        id=course.id,
        name=course.name,
        section=course.section,
        description=course.description,
        room=course.room,
        owner_id=course.owner_id,
        enrollment_code=course.enrollment_code,
        course_state=course.course_state.value,
        creation_time=course.creation_time,
        update_time=course.update_time,
        alternate_link=course.alternate_link
    ).model_dump()
    
    return create_success_response(course_data).model_dump()


@router.post("/sync", response_model=dict)
async def sync_courses(
    current_user: User = Depends(get_current_user),
    classroom_service: ClassroomService = Depends(get_classroom_service)
):
    """
    Sync courses from Google Classroom.
    
    Requires authentication.
    Only available for admin and coordinator roles.
    """
    if current_user.role not in ["administrator", "coordinator"]:
        raise HTTPException(
            status_code=403,
            detail="Only administrators and coordinators can sync courses"
        )
    
    synced_count = classroom_service.sync_courses()
    
    response_data = {
        "synced_count": synced_count,
        "message": f"Successfully synced {synced_count} courses"
    }
    
    return create_success_response(response_data).model_dump()

