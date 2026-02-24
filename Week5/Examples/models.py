"""
Database models using SQLAlchemy ORM.

This module defines the Student and Course entities with their relationships.
"""

from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship

# Base class for all models
Base = declarative_base()

# Association table for many-to-many relationship between students and courses
student_course_association = Table(
    'student_course',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('student.id'), primary_key=True),
    Column('course_id', Integer, ForeignKey('course.id'), primary_key=True)
)


class Student(Base):
    """
    Student model representing a student entity.
    
    Attributes:
        id: Primary key, unique identifier
        name: Student's full name
        email: Student's email address
        gpa: Grade Point Average (0.0 - 4.0)
        courses: Relationship to Course entities through many-to-many association
    """
    __tablename__ = 'student'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    gpa = Column(Float, default=0.0)
    
    # Relationship to courses
    courses = relationship(
        'Course',
        secondary=student_course_association,
        back_populates='students',
        lazy='select'
    )
    
    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', email='{self.email}', gpa={self.gpa})>"


class Course(Base):
    """
    Course model representing a course entity.
    
    Attributes:
        id: Primary key, unique identifier
        name: Course name
        code: Course code (e.g., CS101)
        credits: Number of credit hours
        students: Relationship to Student entities through many-to-many association
    """
    __tablename__ = 'course'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    code = Column(String(20), nullable=False, unique=True)
    credits = Column(Integer, default=3)
    
    # Relationship to students
    students = relationship(
        'Student',
        secondary=student_course_association,
        back_populates='courses',
        lazy='select'
    )
    
    def __repr__(self):
        return f"<Course(id={self.id}, name='{self.name}', code='{self.code}', credits={self.credits})>"
