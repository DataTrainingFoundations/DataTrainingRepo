"""
Database connection and initialization module.

This module handles database setup, session management, and data seeding.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base, Student, Course


class DatabaseManager:
    """
    Manages database connection, session creation, and initialization.
    
    Attributes:
        database_url: SQLite connection string
        engine: SQLAlchemy engine instance
        SessionLocal: Session factory for creating database sessions
    """
    
    def __init__(self, database_url: str = "sqlite:///./school.db"):
        """
        Initialize the database manager.
        
        Args:
            database_url: Database connection URL (default: SQLite local file)
        """
        self.database_url = database_url
        self.engine = create_engine(
            database_url,
            connect_args={"check_same_thread": False},
            echo=False
        )
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
    
    def create_tables(self) -> None:
        """Create all tables in the database."""
        Base.metadata.create_all(bind=self.engine)
    
    def drop_tables(self) -> None:
        """Drop all tables from the database."""
        Base.metadata.drop_all(bind=self.engine)
    
    def get_session(self) -> Session:
        """
        Create and return a new database session.
        
        Returns:
            A SQLAlchemy Session object for database operations
        """
        return self.SessionLocal()
    
    def seed_sample_data(self) -> None:
        """
        Populate the database with sample students and courses data.
        
        This method creates:
        - 5 sample students with varying GPAs
        - 4 sample courses
        - Enrolls students in courses
        """
        session = self.get_session()
        try:
            # Create sample students
            students = [
                Student(name="Alice Johnson", email="alice.johnson@university.edu", gpa=3.85),
                Student(name="Bob Smith", email="bob.smith@university.edu", gpa=3.45),
                Student(name="Carol White", email="carol.white@university.edu", gpa=3.92),
                Student(name="David Brown", email="david.brown@university.edu", gpa=3.10),
                Student(name="Eve Davis", email="eve.davis@university.edu", gpa=3.75),
            ]
            
            # Create sample courses
            courses = [
                Course(name="Introduction to Computer Science", code="CS101", credits=3),
                Course(name="Data Structures", code="CS201", credits=4),
                Course(name="Database Management Systems", code="CS301", credits=3),
                Course(name="Web Development Fundamentals", code="CS105", credits=3),
            ]
            
            # Add students and courses to session
            session.add_all(students)
            session.add_all(courses)
            session.flush()  # Ensure IDs are assigned
            
            # Enroll students in courses
            students[0].courses = [courses[0], courses[1], courses[2]]  # Alice in 3 courses
            students[1].courses = [courses[0], courses[3]]              # Bob in 2 courses
            students[2].courses = [courses[1], courses[2], courses[3]]  # Carol in 3 courses
            students[3].courses = [courses[0]]                          # David in 1 course
            students[4].courses = [courses[2], courses[3]]              # Eve in 2 courses
            
            # Commit all changes
            session.commit()
            print("Sample data successfully seeded to the database.")
            
        except Exception as e:
            session.rollback()
            print(f"Error seeding data: {e}")
            raise
        finally:
            session.close()


# Global database manager instance
db_manager = DatabaseManager()
