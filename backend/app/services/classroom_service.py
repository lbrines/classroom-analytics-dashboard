import json
import os
from typing import List, Optional
from app.models.course import Course, CourseState
from app.models.student import Student, StudentProgress


class ClassroomService:
    """
    Service for managing Google Classroom data.
    Supports dual mode: GOOGLE (real API) and MOCK (test data).
    """
    
    def __init__(self, mode: str = "MOCK"):
        """
        Initialize ClassroomService.
        
        Args:
            mode: Operation mode - "GOOGLE" or "MOCK"
        """
        self.mode = mode
        self.courses_file = os.path.join(
            os.path.dirname(__file__), "..", "data", "mock_courses.json"
        )
        self.students_file = os.path.join(
            os.path.dirname(__file__), "..", "data", "mock_students.json"
        )
        self._courses_cache = None
        self._students_cache = None
    
    def _load_courses(self) -> List[dict]:
        """Load courses from mock data file."""
        if self._courses_cache is None:
            try:
                with open(self.courses_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self._courses_cache = data.get("courses", [])
            except FileNotFoundError:
                self._courses_cache = []
        return self._courses_cache
    
    def _load_students(self) -> List[dict]:
        """Load students from mock data file."""
        if self._students_cache is None:
            try:
                with open(self.students_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self._students_cache = data.get("students", [])
            except FileNotFoundError:
                self._students_cache = []
        return self._students_cache
    
    def get_courses(self) -> List[Course]:
        """
        Get all courses.
        
        Returns:
            List of Course objects
        """
        if self.mode == "MOCK":
            courses_data = self._load_courses()
            return [Course(**course_data) for course_data in courses_data]
        else:
            # TODO: Implement Google Classroom API call
            raise NotImplementedError("Google Classroom API not yet implemented")
    
    def get_course_by_id(self, course_id: str) -> Optional[Course]:
        """
        Get a specific course by ID.
        
        Args:
            course_id: The course ID to search for
            
        Returns:
            Course object if found, None otherwise
        """
        courses = self.get_courses()
        for course in courses:
            if course.id == course_id:
                return course
        return None
    
    def get_students_by_course(self, course_id: str) -> List[Student]:
        """
        Get all students enrolled in a specific course.
        
        Args:
            course_id: The course ID to get students for
            
        Returns:
            List of Student objects
        """
        if self.mode == "MOCK":
            students_data = self._load_students()
            course_students = [
                Student(**student_data)
                for student_data in students_data
                if student_data.get("course_id") == course_id
            ]
            return course_students
        else:
            # TODO: Implement Google Classroom API call
            raise NotImplementedError("Google Classroom API not yet implemented")
    
    def sync_courses(self) -> int:
        """
        Sync courses from Google Classroom.
        
        Returns:
            Number of courses synced
        """
        if self.mode == "MOCK":
            # In mock mode, just return the count of existing courses
            courses = self.get_courses()
            return len(courses)
        else:
            # TODO: Implement Google Classroom API sync
            raise NotImplementedError("Google Classroom API sync not yet implemented")

