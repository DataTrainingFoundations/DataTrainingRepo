- initial prompt: Write a DAO with Alchemy in Python and create a sample db with sqlite for students and courses tables including some sample data and include all the CRUD operations. Do this in a few python modules with easy to read code including comments and good architectural design. Also add in fully functional pytest testing.


# Student Management System - DAO Pattern with SQLAlchemy

A comprehensive implementation of the Data Access Object (DAO) pattern using SQLAlchemy and SQLite. This project demonstrates professional software architecture with complete CRUD operations, sample data, and full pytest test coverage.

## 📋 Project Structure

```
.
├── models.py                 # SQLAlchemy ORM models
├── database.py               # Database connection and initialization
├── student_dao.py            # StudentDAO with CRUD operations
├── course_dao.py             # CourseDAO with CRUD operations
├── conftest.py               # Pytest configuration and fixtures
├── test_student_dao.py       # StudentDAO unit tests
├── test_course_dao.py        # CourseDAO unit tests
├── main.py                   # Example usage demonstration
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## 🎯 Features

### Database Models
- **Student**: Stores student information (name, email, GPA)
- **Course**: Stores course information (name, code, credits)
- **Many-to-Many**: Student-Course relationship for enrollments

### DAO Operations

#### StudentDAO
- ✅ **Create**: `create(name, email, gpa)`
- ✅ **Read**: `read_by_id()`, `read_by_email()`, `read_all()`, `read_by_gpa_range()`
- ✅ **Update**: `update(student_id, name, email, gpa)`
- ✅ **Delete**: `delete(student_id)`
- ✅ **Count**: `count()`

#### CourseDAO
- ✅ **Create**: `create(name, code, credits)`
- ✅ **Read**: `read_by_id()`, `read_by_code()`, `read_all()`, `read_by_credits()`
- ✅ **Update**: `update(course_id, name, code, credits)`
- ✅ **Delete**: `delete(course_id)`
- ✅ **Enrollment**: `enroll_student()`, `unenroll_student()`, `get_enrolled_students()`
- ✅ **Count**: `count()`

## 🚀 Getting Started

### Installation

1. Navigate to the project directory:
```bash
cd Week5/Examples
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage Example

```python
from database import db_manager
from student_dao import StudentDAO

# Initialize database
db_manager.create_tables()
db_manager.seed_sample_data()

# Use StudentDAO
with StudentDAO(db_manager.get_session()) as dao:
    # Create a student
    student = dao.create("John Doe", "john@university.edu", 3.5)
    
    # Read operations
    student = dao.read_by_id(1)
    students = dao.read_by_gpa_range(3.0, 4.0)
    
    # Update
    dao.update(1, gpa=3.8)
    
    # Delete
    dao.delete(1)
```

## 🧪 Testing

### Run All Tests

```bash
pytest
```

### Run with Coverage Report

```bash
pytest --cov=. --cov-report=html
```

### Run Specific Test File

```bash
pytest test_student_dao.py -v
```

### Run Specific Test Class

```bash
pytest test_student_dao.py::TestStudentDAOCreate -v
```

### Test Coverage

The project includes comprehensive tests:

- **test_student_dao.py**: 40+ tests covering StudentDAO operations
- **test_course_dao.py**: 45+ tests covering CourseDAO and enrollment operations

Test categories:
- ✅ Create operations (success cases, edge cases)
- ✅ Read operations (by ID, by field, all records)
- ✅ Update operations (single field, multiple fields, constraints)
- ✅ Delete operations (successful deletion, not found cases)
- ✅ Enrollment management (enroll, unenroll, list students)
- ✅ Context manager functionality

## 💾 Sample Data

The database is pre-populated with:

**Students** (5 total):
- Alice Johnson (GPA: 3.85)
- Bob Smith (GPA: 3.45)
- Carol White (GPA: 3.92)
- David Brown (GPA: 3.10)
- Eve Davis (GPA: 3.75)

**Courses** (4 total):
- CS101: Introduction to Computer Science (3 credits)
- CS201: Data Structures (4 credits)
- CS301: Database Management Systems (3 credits)
- CS105: Web Development Fundamentals (3 credits)

**Enrollments**:
- Alice: CS101, CS201, CS301
- Bob: CS101, CS105
- Carol: CS201, CS301, CS105
- David: CS101
- Eve: CS301, CS105

## 🏗️ Architecture Design

### Design Patterns Used

1. **Data Access Object (DAO)**
   - Separates data access logic from business logic
   - Each entity has its own DAO class
   - Provides a consistent interface for database operations

2. **Repository Pattern**
   - DAOs act as repositories for entities
   - Encapsulates all database interactions

3. **Session Management**
   - Efficient session pooling through DatabaseManager
   - Context manager support for automatic resource cleanup
   - Optional session injection for testing

4. **Object-Relational Mapping (ORM)**
   - SQLAlchemy for database abstraction
   - Model-centric approach
   - Automatic relationship management

### Key Design Principles

- **Separation of Concerns**: Models, DAOs, and business logic are separate
- **DRY (Don't Repeat Yourself)**: Common patterns abstracted
- **SOLID Principles**: Single responsibility, open/closed, dependency injection
- **Testability**: Fixtures and in-memory databases for easy testing
- **Maintainability**: Clear code with extensive documentation

## 📚 Code Structure

### models.py
Defines SQLAlchemy ORM models:
- Base declarative class
- Student and Course entity models
- Many-to-many association table
- Comprehensive docstrings and relationships

### database.py
Manages database lifecycle:
- Engine configuration
- Session factory
- Table creation/destruction
- Sample data seeding
- Global database manager instance

### student_dao.py & course_dao.py
Implement DAO pattern:
- CRUD operations
- Query methods
- Transaction management
- Error handling
- Context manager support

### conftest.py
Pytest configuration:
- Test database fixture
- In-memory SQLite database
- Session fixtures
- Empty database option

### test_*.py
Comprehensive test suites:
- Organized by operation type
- Edge case coverage
- Relationship testing
- Error scenarios

## 📖 Documentation

All code includes:
- ✅ Module-level docstrings
- ✅ Class docstrings with attributes
- ✅ Method docstrings with parameters, returns, and raises
- ✅ Inline comments for complex logic
- ✅ Type hints throughout

## 🔧 Demonstration

Run the example usage:

```bash
python main.py
```

This will:
1. Initialize a fresh database
2. Demonstrate all StudentDAO operations
3. Demonstrate all CourseDAO operations
4. Show enrollment management
5. Display sample data operations

## 🎓 Learning Outcomes

This project demonstrates:

1. **Database Design**
   - Entity-Relationship modeling
   - Many-to-many relationships
   - Proper indexing and constraints

2. **Python Best Practices**
   - Type hints
   - Context managers
   - Exception handling
   - Code organization

3. **SQLAlchemy Skills**
   - ORM model definition
   - Session management
   - Relationship configuration
   - Query patterns

4. **Testing Practices**
   - Pytest fixtures
   - Test organization
   - Coverage analysis
   - Mocking and isolation

5. **Software Architecture**
   - Design patterns
   - Separation of concerns
   - Scalability
   - Maintainability

## 📝 License

This project is provided for educational purposes.

## 🤝 Contributing

Feel free to extend this project:
- Add more DAOs (Instructor, Department, etc.)
- Implement additional query methods
- Add API endpoints using Flask/FastAPI
- Enhance testing with additional edge cases
- Add database migrations with Alembic

## 📞 Support

For questions or issues:
1. Check the docstrings in the source code
2. Review the test cases for usage examples
3. Run `pytest -v` for detailed test output
