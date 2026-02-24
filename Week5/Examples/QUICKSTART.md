# Quick Start Guide

## Installation & Setup (1 minute)

```bash
# Navigate to project directory
cd Week5/Examples

# Install dependencies
pip install -r requirements.txt
```

## Run Example Demonstration (30 seconds)

```bash
python main.py
```

Shows all CRUD operations in action with formatted output.

## Run Tests (10 seconds)

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test file
pytest test_student_dao.py -v

# Run specific test class
pytest test_student_dao.py::TestStudentDAOCreate -v
```

## Basic Usage Examples

### Initialize Database

```python
from database import db_manager

# Create tables
db_manager.create_tables()

# Seed sample data
db_manager.seed_sample_data()
```

### StudentDAO - CRUD Operations

```python
from database import db_manager
from student_dao import StudentDAO

# Create a session
session = db_manager.get_session()
student_dao = StudentDAO(session)

# CREATE
student = student_dao.create("Jane Doe", "jane@university.edu", 3.8)

# READ
student = student_dao.read_by_id(1)
student = student_dao.read_by_email("jane@university.edu")
all_students = student_dao.read_all()
high_gpa = student_dao.read_by_gpa_range(3.5, 4.0)

# UPDATE
student_dao.update(1, gpa=3.9)

# DELETE
student_dao.delete(1)

# COUNT
total = student_dao.count()

# Close session
session.close()
```

### StudentDAO - Context Manager (Recommended)

```python
from database import db_manager
from student_dao import StudentDAO

# Automatically handles session cleanup
with StudentDAO(db_manager.get_session()) as dao:
    student = dao.create("John Doe", "john@university.edu", 3.5)
    all_students = dao.read_all()
    dao.update(student.id, gpa=3.7)
    # Session automatically closed on exit
```

### CourseDAO - CRUD Operations

```python
from database import db_manager
from course_dao import CourseDAO

with CourseDAO(db_manager.get_session()) as dao:
    # CREATE
    course = dao.create("Advanced Python", "CS401", 4)
    
    # READ
    course = dao.read_by_id(1)
    course = dao.read_by_code("CS401")
    all_courses = dao.read_all()
    courses = dao.read_by_credits(3)
    
    # UPDATE
    dao.update(1, credits=4)
    
    # DELETE
    dao.delete(1)
    
    # COUNT
    total = dao.count()
```

### Enrollment Management

```python
from database import db_manager
from course_dao import CourseDAO

with CourseDAO(db_manager.get_session()) as dao:
    # Enroll student in course
    success = dao.enroll_student(course_id=1, student_id=5)
    
    # Get students in a course
    students = dao.get_enrolled_students(1)
    for student in students:
        print(student.name)
    
    # Unenroll student
    success = dao.unenroll_student(course_id=1, student_id=5)
```

## Project File Reference

| File | Purpose |
|------|---------|
| `models.py` | SQLAlchemy ORM models (Student, Course) |
| `database.py` | Database connection, session factory, initialization |
| `student_dao.py` | StudentDAO with complete CRUD operations |
| `course_dao.py` | CourseDAO with CRUD + enrollment operations |
| `conftest.py` | Pytest fixtures and test configuration |
| `test_student_dao.py` | 30+ tests for StudentDAO |
| `test_course_dao.py` | 22+ tests for CourseDAO |
| `main.py` | Runnable example demonstrating all features |
| `requirements.txt` | Python package dependencies |
| `README.md` | Comprehensive documentation |

## Database Schema

### Student Table
- `id` (Integer, Primary Key)
- `name` (String, Required)
- `email` (String, Required, Unique)
- `gpa` (Float, Default: 0.0)
- `courses` (Relationship, Many-to-Many)

### Course Table
- `id` (Integer, Primary Key)
- `name` (String, Required)
- `code` (String, Required, Unique)
- `credits` (Integer, Default: 3)
- `students` (Relationship, Many-to-Many)

### Student-Course Association
- `student_id` (Foreign Key)
- `course_id` (Foreign Key)

## Common Patterns

### Error Handling

```python
from student_dao import StudentDAO

try:
    with StudentDAO(session) as dao:
        student = dao.create("Name", "email@test.edu", 3.5)
except Exception as e:
    print(f"Error: {e}")
    # Exception contains details about what failed
```

### Batch Operations

```python
with StudentDAO(session) as dao:
    # Create multiple students
    for name, email, gpa in students_list:
        dao.create(name, email, gpa)
    
    # Read all at once
    all_students = dao.read_all()
```

### Filtering

```python
with StudentDAO(session) as dao:
    # Find high-performing students
    honors = dao.read_by_gpa_range(3.5, 4.0)
    
    # Find specific student
    student = dao.read_by_email("alice@test.edu")
```

## Test Examples

```python
# Run specific test
pytest test_student_dao.py::TestStudentDAOCreate::test_create_student_success -v

# Run tests matching pattern
pytest -k "create" -v

# Run tests with detailed output
pytest -vv

# Stop after first failure
pytest -x

# Show local variables on failure
pytest -l
```

## Tips & Tricks

1. **Always use context managers** for automatic session cleanup
   ```python
   with StudentDAO(session) as dao:
       # Your code here
   ```

2. **Check return values** for operations that might fail
   ```python
   if dao.delete(student_id):
       print("Deleted successfully")
   else:
       print("Student not found")
   ```

3. **Use read_all() to refresh relationships**
   ```python
   # After modifying enrollments
   course = dao.read_by_id(course_id)
   students = course.students  # Updated list
   ```

4. **Exception handling for unique constraint violations**
   ```python
   try:
       dao.create("Name", duplicate_email, 3.0)
   except Exception as e:
       print(f"Email already exists: {e}")
   ```

5. **Count before and after** for operations
   ```python
   before = dao.count()
   dao.delete(1)
   after = dao.count()
   assert after == before - 1
   ```

## Database Persistence

The default database is SQLite file at `school.db` in the current directory. To reset:

```python
from database import db_manager

# Drop all tables (WARNING: destructive!)
db_manager.drop_tables()

# Recreate and reseed
db_manager.create_tables()
db_manager.seed_sample_data()
```

## Performance Notes

- In-memory database for testing (much faster)
- SQLite for simple projects
- Consider PostgreSQL/MySQL for production
- Add database indexes for frequently queried fields
- Use lazy loading for relationships to save memory

## Extending the System

To add a new DAO:

1. Create a model in `models.py`
2. Create a new `*_dao.py` file
3. Implement CRUD methods following the pattern
4. Add test file `test_*_dao.py`
5. Update `database.py` seed method if needed

Example:
```python
# professor_dao.py
from professor import Professor
from database import db_manager

class ProfessorDAO:
    def __init__(self, session):
        self.session = session
    
    def create(self, name, department):
        professor = Professor(name=name, department=department)
        self.session.add(professor)
        self.session.commit()
        return professor
    
    # Add other CRUD methods...
```
