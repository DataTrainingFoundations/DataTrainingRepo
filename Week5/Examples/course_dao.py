"""
Data Access Object (DAO) for Course entity.

This module implements all CRUD (Create, Read, Update, Delete) operations
for the Course entity using the DAO pattern.
"""

from typing import List, Optional
from sqlalchemy.orm import Session
from models import Course, Student
from database import db_manager


class CourseDAO:
    """
    Data Access Object for Course entity.
    
    Provides CRUD operations for managing Course records and student enrollments.
    """
    
    def __init__(self, session: Optional[Session] = None):
        """
        Initialize the CourseDAO.
        
        Args:
            session: SQLAlchemy Session object. If None, a new session is created.
        """
        self.session = session or db_manager.get_session()
        self._owns_session = session is None  # Track if this DAO created the session
    
    def create(self, name: str, code: str, credits: int = 3) -> Course:
        """
        Create and save a new course to the database.
        
        Args:
            name: Course name
            code: Course code (e.g., CS101, must be unique)
            credits: Number of credit hours (default: 3)
        
        Returns:
            The created Course object with assigned ID
        
        Raises:
            Exception: If code already exists or other database errors occur
        """
        try:
            course = Course(name=name, code=code, credits=credits)
            self.session.add(course)
            self.session.commit()
            return course
        except Exception as e:
            self.session.rollback()
            raise Exception(f"Failed to create course: {e}")
    
    def read_by_id(self, course_id: int) -> Optional[Course]:
        """
        Retrieve a course by its ID.
        
        Args:
            course_id: The course's unique identifier
        
        Returns:
            Course object if found, None otherwise
        """
        return self.session.query(Course).filter(Course.id == course_id).first()
    
    def read_by_code(self, code: str) -> Optional[Course]:
        """
        Retrieve a course by its course code.
        
        Args:
            code: The course code (e.g., CS101)
        
        Returns:
            Course object if found, None otherwise
        """
        return self.session.query(Course).filter(Course.code == code).first()
    
    def read_all(self) -> List[Course]:
        """
        Retrieve all courses from the database.
        
        Returns:
            List of all Course objects
        """
        return self.session.query(Course).all()
    
    def read_by_credits(self, credits: int) -> List[Course]:
        """
        Retrieve all courses with a specific number of credits.
        
        Args:
            credits: Number of credit hours
        
        Returns:
            List of Course objects matching the credit count
        """
        return self.session.query(Course).filter(Course.credits == credits).all()
    
    def update(self, course_id: int, name: str = None, code: str = None, credits: int = None) -> Optional[Course]:
        """
        Update an existing course's information.
        
        Args:
            course_id: The course's unique identifier
            name: New course name (optional, update only if provided)
            code: New course code (optional, update only if provided)
            credits: New number of credits (optional, update only if provided)
        
        Returns:
            Updated Course object if found, None otherwise
        
        Raises:
            Exception: If update fails due to database constraints
        """
        try:
            course = self.read_by_id(course_id)
            if not course:
                return None
            
            if name is not None:
                course.name = name
            if code is not None:
                course.code = code
            if credits is not None:
                course.credits = credits
            
            self.session.commit()
            return course
        except Exception as e:
            self.session.rollback()
            raise Exception(f"Failed to update course: {e}")
    
    def delete(self, course_id: int) -> bool:
        """
        Delete a course from the database.
        
        Args:
            course_id: The course's unique identifier
        
        Returns:
            True if deletion was successful, False if course not found
        """
        try:
            course = self.read_by_id(course_id)
            if not course:
                return False
            
            self.session.delete(course)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            raise Exception(f"Failed to delete course: {e}")
    
    def enroll_student(self, course_id: int, student_id: int) -> bool:
        """
        Enroll a student in a course.
        
        Args:
            course_id: The course's unique identifier
            student_id: The student's unique identifier
        
        Returns:
            True if enrollment was successful, False if course or student not found
        
        Raises:
            Exception: If enrollment fails due to database errors
        """
        try:
            course = self.read_by_id(course_id)
            if not course:
                return False
            
            # Import here to avoid circular imports
            from student_dao import StudentDAO
            student_dao = StudentDAO(self.session)
            student = student_dao.read_by_id(student_id)
            if not student:
                return False
            
            # Check if already enrolled
            if student not in course.students:
                course.students.append(student)
                self.session.commit()
            
            return True
        except Exception as e:
            self.session.rollback()
            raise Exception(f"Failed to enroll student: {e}")
    
    def unenroll_student(self, course_id: int, student_id: int) -> bool:
        """
        Remove a student from a course.
        
        Args:
            course_id: The course's unique identifier
            student_id: The student's unique identifier
        
        Returns:
            True if unenrollment was successful, False if course or student not found
        
        Raises:
            Exception: If unenrollment fails due to database errors
        """
        try:
            course = self.read_by_id(course_id)
            if not course:
                return False
            
            # Import here to avoid circular imports
            from student_dao import StudentDAO
            student_dao = StudentDAO(self.session)
            student = student_dao.read_by_id(student_id)
            if not student:
                return False
            
            # Check if enrolled before removing
            if student in course.students:
                course.students.remove(student)
                self.session.commit()
            
            return True
        except Exception as e:
            self.session.rollback()
            raise Exception(f"Failed to unenroll student: {e}")
    
    def get_enrolled_students(self, course_id: int) -> List[Student]:
        """
        Get all students enrolled in a specific course.
        
        Args:
            course_id: The course's unique identifier
        
        Returns:
            List of Student objects enrolled in the course, or empty list if course not found
        """
        course = self.read_by_id(course_id)
        return course.students if course else []
    
    def count(self) -> int:
        """
        Get the total number of courses in the database.
        
        Returns:
            Total count of courses
        """
        return self.session.query(Course).count()
    
    def close(self) -> None:
        """Close the database session if this DAO owns it."""
        if self._owns_session and self.session:
            self.session.close()
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - closes session."""
        self.close()
