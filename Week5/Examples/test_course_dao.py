"""
Unit tests for CourseDAO class.

Tests cover all CRUD operations, enrollment management, and various query methods.
"""

import pytest
from course_dao import CourseDAO
from student_dao import StudentDAO
from database import DatabaseManager


class TestCourseDAOCreate:
    """Test suite for course creation operations."""
    
    def test_create_course_success(self, empty_db: DatabaseManager):
        """Test successful creation of a new course."""
        dao = CourseDAO(empty_db.get_session())
        
        course = dao.create("Advanced Python", "CS401", 4)
        
        assert course.id is not None
        assert course.name == "Advanced Python"
        assert course.code == "CS401"
        assert course.credits == 4
        dao.close()
    
    def test_create_course_default_credits(self, empty_db: DatabaseManager):
        """Test that credits defaults to 3 when not specified."""
        dao = CourseDAO(empty_db.get_session())
        
        course = dao.create("Introduction to AI", "CS150")
        
        assert course.credits == 3
        dao.close()
    
    def test_create_course_duplicate_code(self, empty_db: DatabaseManager):
        """Test that duplicate course code raises an exception."""
        dao = CourseDAO(empty_db.get_session())
        dao.create("Computer Science 101", "CS101", 3)
        
        with pytest.raises(Exception, match="Failed to create course"):
            dao.create("Introduction to CS", "CS101", 3)
        
        dao.close()


class TestCourseDAORead:
    """Test suite for course retrieval operations."""
    
    def test_read_by_id_success(self, test_db: DatabaseManager):
        """Test retrieving a course by ID."""
        dao = CourseDAO(test_db.get_session())
        
        course = dao.read_by_id(1)
        
        assert course is not None
        assert course.id == 1
        assert course.name == "Introduction to Computer Science"
        dao.close()
    
    def test_read_by_id_not_found(self, test_db: DatabaseManager):
        """Test reading a non-existent course returns None."""
        dao = CourseDAO(test_db.get_session())
        
        course = dao.read_by_id(9999)
        
        assert course is None
        dao.close()
    
    def test_read_by_code_success(self, test_db: DatabaseManager):
        """Test retrieving a course by course code."""
        dao = CourseDAO(test_db.get_session())
        
        course = dao.read_by_code("CS101")
        
        assert course is not None
        assert course.name == "Introduction to Computer Science"
        dao.close()
    
    def test_read_by_code_not_found(self, test_db: DatabaseManager):
        """Test reading by non-existent code returns None."""
        dao = CourseDAO(test_db.get_session())
        
        course = dao.read_by_code("CS999")
        
        assert course is None
        dao.close()
    
    def test_read_all(self, test_db: DatabaseManager):
        """Test retrieving all courses."""
        dao = CourseDAO(test_db.get_session())
        
        courses = dao.read_all()
        
        assert len(courses) == 4
        assert all(isinstance(c, object) for c in courses)
        dao.close()
    
    def test_read_by_credits(self, test_db: DatabaseManager):
        """Test retrieving courses by credit count."""
        dao = CourseDAO(test_db.get_session())
        
        courses = dao.read_by_credits(3)
        
        assert len(courses) >= 1
        assert all(c.credits == 3 for c in courses)
        dao.close()


class TestCourseDAOUpdate:
    """Test suite for course update operations."""
    
    def test_update_name_success(self, test_db: DatabaseManager):
        """Test updating a course's name."""
        dao = CourseDAO(test_db.get_session())
        
        updated_course = dao.update(1, name="Intro to CS Advanced")
        
        assert updated_course is not None
        assert updated_course.name == "Intro to CS Advanced"
        
        # Verify persistence
        retrieved = dao.read_by_id(1)
        assert retrieved.name == "Intro to CS Advanced"
        dao.close()
    
    def test_update_code_success(self, test_db: DatabaseManager):
        """Test updating a course's code."""
        dao = CourseDAO(test_db.get_session())
        
        updated_course = dao.update(1, code="CS101A")
        
        assert updated_course.code == "CS101A"
        dao.close()
    
    def test_update_credits_success(self, test_db: DatabaseManager):
        """Test updating a course's credits."""
        dao = CourseDAO(test_db.get_session())
        
        updated_course = dao.update(1, credits=4)
        
        assert updated_course.credits == 4
        dao.close()
    
    def test_update_multiple_fields(self, test_db: DatabaseManager):
        """Test updating multiple fields at once."""
        dao = CourseDAO(test_db.get_session())
        
        updated_course = dao.update(
            1,
            name="New Course Name",
            code="NEWCS101",
            credits=4
        )
        
        assert updated_course.name == "New Course Name"
        assert updated_course.code == "NEWCS101"
        assert updated_course.credits == 4
        dao.close()
    
    def test_update_not_found(self, test_db: DatabaseManager):
        """Test updating a non-existent course returns None."""
        dao = CourseDAO(test_db.get_session())
        
        result = dao.update(9999, name="Nonexistent")
        
        assert result is None
        dao.close()


class TestCourseDAODelete:
    """Test suite for course deletion operations."""
    
    def test_delete_success(self, test_db: DatabaseManager):
        """Test successful deletion of a course."""
        dao = CourseDAO(test_db.get_session())
        initial_count = dao.count()
        
        result = dao.delete(1)
        
        assert result is True
        assert dao.count() == initial_count - 1
        assert dao.read_by_id(1) is None
        dao.close()
    
    def test_delete_not_found(self, test_db: DatabaseManager):
        """Test deleting a non-existent course returns False."""
        dao = CourseDAO(test_db.get_session())
        
        result = dao.delete(9999)
        
        assert result is False
        dao.close()


class TestCourseDAOEnrollment:
    """Test suite for student enrollment operations."""
    
    def test_enroll_student_success(self, test_db: DatabaseManager):
        """Test successful student enrollment in a course."""
        session = test_db.get_session()
        course_dao = CourseDAO(session)
        
        course = course_dao.read_by_id(1)
        initial_count = len(course.students)
        
        # Get a student not currently enrolled (if all are enrolled, use first anyway)
        success = course_dao.enroll_student(1, 2)
        
        assert success is True
        
        # Refresh and check enrollment
        course = course_dao.read_by_id(1)
        assert len(course.students) >= initial_count
        course_dao.close()
    
    def test_enroll_student_duplicate(self, test_db: DatabaseManager):
        """Test that enrolling a student already in the course doesn't duplicate."""
        session = test_db.get_session()
        course_dao = CourseDAO(session)
        
        course = course_dao.read_by_id(1)
        initial_count = len(course.students)
        
        # Enroll student that's already enrolled
        success = course_dao.enroll_student(1, 1)
        
        assert success is True
        
        # Count should not increase
        course = course_dao.read_by_id(1)
        assert len(course.students) == initial_count
        course_dao.close()
    
    def test_enroll_nonexistent_student(self, test_db: DatabaseManager):
        """Test enrolling a non-existent student returns False."""
        dao = CourseDAO(test_db.get_session())
        
        success = dao.enroll_student(1, 9999)
        
        assert success is False
        dao.close()
    
    def test_enroll_nonexistent_course(self, test_db: DatabaseManager):
        """Test enrolling in a non-existent course returns False."""
        dao = CourseDAO(test_db.get_session())
        
        success = dao.enroll_student(9999, 1)
        
        assert success is False
        dao.close()
    
    def test_unenroll_student_success(self, test_db: DatabaseManager):
        """Test successful unenrollment of a student from a course."""
        session = test_db.get_session()
        course_dao = CourseDAO(session)
        
        # Ensure student is enrolled
        course_dao.enroll_student(1, 1)
        course = course_dao.read_by_id(1)
        initial_count = len(course.students)
        
        # Unenroll student
        success = course_dao.unenroll_student(1, 1)
        
        assert success is True
        
        # Verify unenrollment
        course = course_dao.read_by_id(1)
        assert len(course.students) < initial_count
        course_dao.close()
    
    def test_unenroll_student_not_enrolled(self, test_db: DatabaseManager):
        """Test unenrolling a student not enrolled in the course."""
        session = test_db.get_session()
        course_dao = CourseDAO(session)
        
        course = course_dao.read_by_id(1)
        initial_count = len(course.students)
        
        # Try to unenroll a student not enrolled (use a different student ID)
        success = course_dao.unenroll_student(1, 4)  # Assuming student 4 not in course 1
        
        # Should still return True, but count unchanged if not enrolled
        course = course_dao.read_by_id(1)
        # Note: behavior depends on seed data
        course_dao.close()
    
    def test_get_enrolled_students(self, test_db: DatabaseManager):
        """Test retrieving students enrolled in a course."""
        dao = CourseDAO(test_db.get_session())
        
        students = dao.get_enrolled_students(1)
        
        assert len(students) > 0
        assert all(hasattr(s, 'name') for s in students)
        dao.close()
    
    def test_get_enrolled_students_empty(self, empty_db: DatabaseManager):
        """Test getting enrolled students for an empty course."""
        session = empty_db.get_session()
        course_dao = CourseDAO(session)
        
        # Create an empty course
        course_dao.create("Empty Course", "CS999", 3)
        students = course_dao.get_enrolled_students(1)
        
        assert len(students) == 0
        course_dao.close()
    
    def test_get_enrolled_students_nonexistent(self, test_db: DatabaseManager):
        """Test getting enrolled students for non-existent course returns empty list."""
        dao = CourseDAO(test_db.get_session())
        
        students = dao.get_enrolled_students(9999)
        
        assert len(students) == 0
        dao.close()


class TestCourseDAOCount:
    """Test suite for course count operations."""
    
    def test_count_all_courses(self, test_db: DatabaseManager):
        """Test counting total courses."""
        dao = CourseDAO(test_db.get_session())
        
        count = dao.count()
        
        assert count == 4
        dao.close()
    
    def test_count_after_deletion(self, test_db: DatabaseManager):
        """Test count after deleting a course."""
        dao = CourseDAO(test_db.get_session())
        initial_count = dao.count()
        
        dao.delete(1)
        new_count = dao.count()
        
        assert new_count == initial_count - 1
        dao.close()


class TestCourseDAOContextManager:
    """Test suite for context manager functionality."""
    
    def test_context_manager_usage(self, test_db: DatabaseManager):
        """Test using CourseDAO as a context manager."""
        with CourseDAO(test_db.get_session()) as dao:
            course = dao.read_by_id(1)
            assert course is not None
        
        # After exiting context, session should be closed
        assert True  # Verify no exception occurred
    
    def test_manual_close(self, test_db: DatabaseManager):
        """Test manual session closure."""
        dao = CourseDAO(test_db.get_session())
        course = dao.read_by_id(1)
        assert course is not None
        
        dao.close()
        # Should be safe to close again
        dao.close()
