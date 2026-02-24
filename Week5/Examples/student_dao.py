"""
Data Access Object (DAO) for Student entity.

This module implements all CRUD (Create, Read, Update, Delete) operations
for the Student entity using the DAO pattern.
"""

from typing import List, Optional
from sqlalchemy.orm import Session
from models import Student
from database import db_manager


class StudentDAO:
    """
    Data Access Object for Student entity.
    
    Provides CRUD operations for managing Student records in the database.
    """
    
    def __init__(self, session: Optional[Session] = None):
        """
        Initialize the StudentDAO.
        
        Args:
            session: SQLAlchemy Session object. If None, a new session is created.
        """
        self.session = session or db_manager.get_session()
        self._owns_session = session is None  # Track if this DAO created the session
    
    def create(self, name: str, email: str, gpa: float = 0.0) -> Student:
        """
        Create and save a new student to the database.
        
        Args:
            name: Student's full name
            email: Student's email address (must be unique)
            gpa: Grade Point Average (default: 0.0)
        
        Returns:
            The created Student object with assigned ID
        
        Raises:
            Exception: If email already exists or other database errors occur
        """
        try:
            student = Student(name=name, email=email, gpa=gpa)
            self.session.add(student)
            self.session.commit()
            return student
        except Exception as e:
            self.session.rollback()
            raise Exception(f"Failed to create student: {e}")
    
    def read_by_id(self, student_id: int) -> Optional[Student]:
        """
        Retrieve a student by their ID.
        
        Args:
            student_id: The student's unique identifier
        
        Returns:
            Student object if found, None otherwise
        """
        return self.session.query(Student).filter(Student.id == student_id).first()
    
    def read_by_email(self, email: str) -> Optional[Student]:
        """
        Retrieve a student by their email address.
        
        Args:
            email: The student's email address
        
        Returns:
            Student object if found, None otherwise
        """
        return self.session.query(Student).filter(Student.email == email).first()
    
    def read_all(self) -> List[Student]:
        """
        Retrieve all students from the database.
        
        Returns:
            List of all Student objects
        """
        return self.session.query(Student).all()
    
    def read_by_gpa_range(self, min_gpa: float, max_gpa: float) -> List[Student]:
        """
        Retrieve students within a specific GPA range.
        
        Args:
            min_gpa: Minimum GPA value (inclusive)
            max_gpa: Maximum GPA value (inclusive)
        
        Returns:
            List of Student objects matching the GPA range
        """
        return self.session.query(Student).filter(
            Student.gpa >= min_gpa,
            Student.gpa <= max_gpa
        ).all()
    
    def update(self, student_id: int, name: str = None, email: str = None, gpa: float = None) -> Optional[Student]:
        """
        Update an existing student's information.
        
        Args:
            student_id: The student's unique identifier
            name: New name (optional, update only if provided)
            email: New email (optional, update only if provided)
            gpa: New GPA (optional, update only if provided)
        
        Returns:
            Updated Student object if found, None otherwise
        
        Raises:
            Exception: If update fails due to database constraints
        """
        try:
            student = self.read_by_id(student_id)
            if not student:
                return None
            
            if name is not None:
                student.name = name
            if email is not None:
                student.email = email
            if gpa is not None:
                student.gpa = gpa
            
            self.session.commit()
            return student
        except Exception as e:
            self.session.rollback()
            raise Exception(f"Failed to update student: {e}")
    
    def delete(self, student_id: int) -> bool:
        """
        Delete a student from the database.
        
        Args:
            student_id: The student's unique identifier
        
        Returns:
            True if deletion was successful, False if student not found
        """
        try:
            student = self.read_by_id(student_id)
            if not student:
                return False
            
            self.session.delete(student)
            self.session.commit()
            return True
        except Exception as e:
            self.session.rollback()
            raise Exception(f"Failed to delete student: {e}")
    
    def count(self) -> int:
        """
        Get the total number of students in the database.
        
        Returns:
            Total count of students
        """
        return self.session.query(Student).count()
    
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
