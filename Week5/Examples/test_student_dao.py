"""
Unit tests for StudentDAO class.

Tests cover all CRUD operations and various query methods.
"""

import pytest
from student_dao import StudentDAO
from database import DatabaseManager


class TestStudentDAOCreate:
    """Test suite for student creation operations."""
    
    def test_create_student_success(self, empty_db: DatabaseManager):
        """Test successful creation of a new student."""
        dao = StudentDAO(empty_db.get_session())
        
        student = dao.create("John Doe", "john.doe@university.edu", 3.5)
        
        assert student.id is not None
        assert student.name == "John Doe"
        assert student.email == "john.doe@university.edu"
        assert student.gpa == 3.5
        dao.close()
    
    def test_create_student_default_gpa(self, empty_db: DatabaseManager):
        """Test that GPA defaults to 0.0 when not specified."""
        dao = StudentDAO(empty_db.get_session())
        
        student = dao.create("Jane Doe", "jane.doe@university.edu")
        
        assert student.gpa == 0.0
        dao.close()
    
    def test_create_student_duplicate_email(self, empty_db: DatabaseManager):
        """Test that duplicate email raises an exception."""
        dao = StudentDAO(empty_db.get_session())
        dao.create("John Doe", "john@university.edu", 3.0)
        
        with pytest.raises(Exception, match="Failed to create student"):
            dao.create("Jane Doe", "john@university.edu", 3.5)
        
        dao.close()


class TestStudentDAORead:
    """Test suite for student retrieval operations."""
    
    def test_read_by_id_success(self, test_db: DatabaseManager):
        """Test retrieving a student by ID."""
        dao = StudentDAO(test_db.get_session())
        
        student = dao.read_by_id(1)
        
        assert student is not None
        assert student.id == 1
        assert student.name == "Alice Johnson"
        dao.close()
    
    def test_read_by_id_not_found(self, test_db: DatabaseManager):
        """Test reading a non-existent student returns None."""
        dao = StudentDAO(test_db.get_session())
        
        student = dao.read_by_id(9999)
        
        assert student is None
        dao.close()
    
    def test_read_by_email_success(self, test_db: DatabaseManager):
        """Test retrieving a student by email."""
        dao = StudentDAO(test_db.get_session())
        
        student = dao.read_by_email("alice.johnson@university.edu")
        
        assert student is not None
        assert student.name == "Alice Johnson"
        dao.close()
    
    def test_read_by_email_not_found(self, test_db: DatabaseManager):
        """Test reading by non-existent email returns None."""
        dao = StudentDAO(test_db.get_session())
        
        student = dao.read_by_email("nonexistent@university.edu")
        
        assert student is None
        dao.close()
    
    def test_read_all(self, test_db: DatabaseManager):
        """Test retrieving all students."""
        dao = StudentDAO(test_db.get_session())
        
        students = dao.read_all()
        
        assert len(students) == 5
        assert all(isinstance(s, object) for s in students)
        dao.close()
    
    def test_read_by_gpa_range(self, test_db: DatabaseManager):
        """Test retrieving students within a GPA range."""
        dao = StudentDAO(test_db.get_session())
        
        # Students with GPA between 3.7 and 3.9
        students = dao.read_by_gpa_range(3.7, 3.9)
        
        assert len(students) == 2  # Alice (3.85) and Eve (3.75)
        assert all(3.7 <= s.gpa <= 3.9 for s in students)
        dao.close()
    
    def test_read_by_gpa_range_empty(self, test_db: DatabaseManager):
        """Test GPA range query with no matches."""
        dao = StudentDAO(test_db.get_session())
        
        students = dao.read_by_gpa_range(2.0, 2.5)
        
        assert len(students) == 0
        dao.close()


class TestStudentDAOUpdate:
    """Test suite for student update operations."""
    
    def test_update_name_success(self, test_db: DatabaseManager):
        """Test updating a student's name."""
        dao = StudentDAO(test_db.get_session())
        
        updated_student = dao.update(1, name="Alice Smith")
        
        assert updated_student is not None
        assert updated_student.name == "Alice Smith"
        
        # Verify persistence
        retrieved = dao.read_by_id(1)
        assert retrieved.name == "Alice Smith"
        dao.close()
    
    def test_update_gpa_success(self, test_db: DatabaseManager):
        """Test updating a student's GPA."""
        dao = StudentDAO(test_db.get_session())
        
        updated_student = dao.update(1, gpa=4.0)
        
        assert updated_student.gpa == 4.0
        dao.close()
    
    def test_update_email_success(self, test_db: DatabaseManager):
        """Test updating a student's email."""
        dao = StudentDAO(test_db.get_session())
        
        updated_student = dao.update(1, email="newemail@university.edu")
        
        assert updated_student.email == "newemail@university.edu"
        dao.close()
    
    def test_update_multiple_fields(self, test_db: DatabaseManager):
        """Test updating multiple fields at once."""
        dao = StudentDAO(test_db.get_session())
        
        updated_student = dao.update(
            1,
            name="Alice New",
            email="alice.new@university.edu",
            gpa=3.95
        )
        
        assert updated_student.name == "Alice New"
        assert updated_student.email == "alice.new@university.edu"
        assert updated_student.gpa == 3.95
        dao.close()
    
    def test_update_not_found(self, test_db: DatabaseManager):
        """Test updating a non-existent student returns None."""
        dao = StudentDAO(test_db.get_session())
        
        result = dao.update(9999, name="Nonexistent")
        
        assert result is None
        dao.close()
    
    def test_update_duplicate_email(self, test_db: DatabaseManager):
        """Test that updating to a duplicate email raises an exception."""
        dao = StudentDAO(test_db.get_session())
        
        # Try to update Alice's email to Bob's email
        with pytest.raises(Exception, match="Failed to update student"):
            dao.update(1, email="bob.smith@university.edu")
        
        dao.close()


class TestStudentDAODelete:
    """Test suite for student deletion operations."""
    
    def test_delete_success(self, test_db: DatabaseManager):
        """Test successful deletion of a student."""
        dao = StudentDAO(test_db.get_session())
        initial_count = dao.count()
        
        result = dao.delete(1)
        
        assert result is True
        assert dao.count() == initial_count - 1
        assert dao.read_by_id(1) is None
        dao.close()
    
    def test_delete_not_found(self, test_db: DatabaseManager):
        """Test deleting a non-existent student returns False."""
        dao = StudentDAO(test_db.get_session())
        
        result = dao.delete(9999)
        
        assert result is False
        dao.close()
    
    def test_delete_cascade(self, test_db: DatabaseManager):
        """Test that deleting a student removes enrollment relationships."""
        dao = StudentDAO(test_db.get_session())
        
        student = dao.read_by_id(1)
        initial_courses = len(student.courses)
        assert initial_courses > 0
        
        dao.delete(1)
        
        # Verify student is deleted
        assert dao.read_by_id(1) is None
        dao.close()


class TestStudentDAOCount:
    """Test suite for student count operations."""
    
    def test_count_all_students(self, test_db: DatabaseManager):
        """Test counting total students."""
        dao = StudentDAO(test_db.get_session())
        
        count = dao.count()
        
        assert count == 5
        dao.close()
    
    def test_count_after_deletion(self, test_db: DatabaseManager):
        """Test count after deleting a student."""
        dao = StudentDAO(test_db.get_session())
        initial_count = dao.count()
        
        dao.delete(1)
        new_count = dao.count()
        
        assert new_count == initial_count - 1
        dao.close()


class TestStudentDAOContextManager:
    """Test suite for context manager functionality."""
    
    def test_context_manager_usage(self, test_db: DatabaseManager):
        """Test using StudentDAO as a context manager."""
        with StudentDAO(test_db.get_session()) as dao:
            student = dao.read_by_id(1)
            assert student is not None
        
        # After exiting context, session should be closed
        assert True  # Verify no exception occurred
    
    def test_manual_close(self, test_db: DatabaseManager):
        """Test manual session closure."""
        dao = StudentDAO(test_db.get_session())
        student = dao.read_by_id(1)
        assert student is not None
        
        dao.close()
        # Should be safe to close again
        dao.close()
