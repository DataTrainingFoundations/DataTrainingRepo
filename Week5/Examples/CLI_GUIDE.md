# Interactive CLI User Guide

## Overview

The `main.py` file has been converted to an **interactive command-line interface (CLI)** that lets you perform CRUD operations on Students and Courses with clear prompts and instructions.

## Running the Program

```bash
python main.py
```

The program will:
1. Initialize the database with sample data
2. Display the main menu
3. Wait for your input to select operations

## Main Menu

When you run the program, you'll see:

```
============================================================
  STUDENT MANAGEMENT SYSTEM - INTERACTIVE CLI
============================================================

============================================================
  MAIN MENU
============================================================

Select what you want to manage:
  1. Student Management
  2. Course Management
  3. View All Data
  4. Reset Database
  5. Exit
```

## 1. Student Management

Choose option **1** from the main menu to access:

### Student Operations Menu
```
============================================================
  STUDENT OPERATIONS
============================================================

Choose an operation:
  1. Create Student
  2. View Student by ID
  3. View Student by Email
  4. View All Students
  5. Update Student
  6. Delete Student
  7. View Students by GPA Range
  8. Back to Main Menu
```

### 1.1 Create Student
- **Prompts**:
  - `Enter student name:`
  - `Enter email address:`
  - `Enter GPA (0.0-4.0, default 0.0):`
- **Validation**: Email must be unique, GPA must be 0.0-4.0
- **Output**: Displays created student with ID

### 1.2 View Student by ID
- **Prompt**: `Enter student ID:`
- **Output**: Shows name, email, GPA, and enrolled courses

### 1.3 View Student by Email
- **Prompt**: `Enter email address:`
- **Output**: Shows student details if found

### 1.4 View All Students
- **Output**: Lists all students with ID, name, email, GPA, and course count

### 1.5 Update Student
- **Prompts**:
  - `Enter student ID:`
  - `Enter new name (or press Enter to skip):`
  - `Enter new email (or press Enter to skip):`
  - `Enter new GPA (or press Enter to skip):`
- **Output**: Shows updated student information

### 1.6 Delete Student
- **Prompts**:
  - `Enter student ID:`
  - `Are you sure? (yes/no):`
- **Output**: Confirmation of deletion

### 1.7 View Students by GPA Range
- **Prompts**:
  - `Enter minimum GPA:`
  - `Enter maximum GPA:`
- **Output**: Lists all students within the GPA range

## 2. Course Management

Choose option **2** from the main menu to access:

### Course Operations Menu
```
============================================================
  COURSE OPERATIONS
============================================================

Choose an operation:
  1. Create Course
  2. View Course by ID
  3. View Course by Code
  4. View All Courses
  5. Update Course
  6. Delete Course
  7. Manage Enrollments
  8. Back to Main Menu
```

### 2.1 Create Course
- **Prompts**:
  - `Enter course name:`
  - `Enter course code (e.g., CS101):`
  - `Enter credits (default 3):`
- **Validation**: Code must be unique, credits must be > 0
- **Output**: Displays created course with ID

### 2.2 View Course by ID
- **Prompt**: `Enter course ID:`
- **Output**: Shows code, name, credits, and enrolled students

### 2.3 View Course by Code
- **Prompt**: `Enter course code:`
- **Output**: Shows course details if found

### 2.4 View All Courses
- **Output**: Lists all courses with ID, code, name, credits, and student count

### 2.5 Update Course
- **Prompts**:
  - `Enter course ID:`
  - `Enter new name (or press Enter to skip):`
  - `Enter new code (or press Enter to skip):`
  - `Enter new credits (or press Enter to skip):`
- **Output**: Shows updated course information

### 2.6 Delete Course
- **Prompts**:
  - `Enter course ID:`
  - `Are you sure? (yes/no):`
- **Output**: Confirmation of deletion

### 2.7 Manage Enrollments

Opens the **Enrollment Operations** menu:

```
============================================================
  ENROLLMENT OPERATIONS
============================================================

Choose an operation:
  1. Enroll Student in Course
  2. Unenroll Student from Course
  3. View Students in Course
  4. Back to Course Menu
```

#### 2.7.1 Enroll Student in Course
- **Prompts**:
  - `Enter course ID:`
  - `Enter student ID:`
- **Output**: Shows enrolled student and course

#### 2.7.2 Unenroll Student from Course
- **Prompts**:
  - `Enter course ID:`
  - `Enter student ID:`
- **Output**: Confirmation of unenrollment

#### 2.7.3 View Students in Course
- **Prompt**: `Enter course ID:`
- **Output**: Lists all enrolled students with GPA

## 3. View All Data

Choose option **3** from the main menu to see:
- List of all students (ID, name, email, GPA)
- List of all courses (ID, code, name, credits)

## 4. Reset Database

Choose option **4** from the main menu to:
- Delete all data
- Recreate tables with fresh sample data
- Requires confirmation: `Are you sure? (yes/no):`

## 5. Exit

Choose option **5** to exit the program.

---

## Usage Examples

### Create a New Student

```
Main Menu > 1 (Student Management) > 1 (Create Student)

Enter student name: John Smith
Enter email address: john.smith@university.edu
Enter GPA (0.0-4.0, default 0.0): 3.8

✅ Student created successfully!
   ID: 6
   Name: John Smith
   Email: john.smith@university.edu
   GPA: 3.8
```

### Create a New Course

```
Main Menu > 2 (Course Management) > 1 (Create Course)

Enter course name: Advanced Web Development
Enter course code (e.g., CS101): CS350
Enter credits (default 3): 4

✅ Course created successfully!
   ID: 5
   Code: CS350
   Name: Advanced Web Development
   Credits: 4
```

### Enroll a Student

```
Main Menu > 2 (Course Management) > 7 (Manage Enrollments) > 1 (Enroll)

Enter course ID: 1
Enter student ID: 1

✅ Alice Johnson enrolled in CS101 successfully!
```

### Update Student GPA

```
Main Menu > 1 (Student Management) > 5 (Update Student)

Enter student ID: 1

Current Info: Alice Johnson | alice.johnson@university.edu | GPA: 3.85
Leave field blank to skip (no change)

Enter new name (or press Enter to skip): [press Enter]
Enter new email (or press Enter to skip): [press Enter]
Enter new GPA (or press Enter to skip): 3.95

✅ Student updated successfully!
ID:       1
Name:     Alice Johnson
Email:    alice.johnson@university.edu
GPA:      3.95
Courses:  3
  Enrolled in:
    • CS101 - Introduction to Computer Science
    • CS201 - Data Structures
    • CS301 - Database Management Systems
```

---

## Tips & Tricks

### Skip Optional Fields
When updating records, you can press **Enter** without typing to leave a field unchanged.

### Confirmation Prompts
Delete operations require confirmation. Type **yes** or **y** to confirm, anything else to cancel.

### View Related Data
When viewing a student, you see their enrolled courses.
When viewing a course, you see enrolled students.

### Sample Data
The program starts with 5 pre-loaded students and 4 courses. You can reset anytime with option 4.

### Error Messages
- ❌ **Red X**: Indicates an error
- ✅ **Green Check**: Indicates success
- **Details**: Error messages explain what went wrong

---

## Keyboard Navigation

| Key | Action |
|-----|--------|
| **1-8** | Select menu option |
| **Enter** | Confirm input / Continue to next prompt |
| **Press Enter** | Skip optional field (during updates) |

---

## Sample Data

The program comes with pre-loaded data:

### Students
1. Alice Johnson (alice.johnson@university.edu) - GPA: 3.85
2. Bob Smith (bob.smith@university.edu) - GPA: 3.45
3. Carol White (carol.white@university.edu) - GPA: 3.92
4. David Brown (david.brown@university.edu) - GPA: 3.10
5. Eve Davis (eve.davis@university.edu) - GPA: 3.75

### Courses
1. CS101 - Introduction to Computer Science (3 credits)
2. CS201 - Data Structures (4 credits)
3. CS301 - Database Management Systems (3 credits)
4. CS105 - Web Development Fundamentals (3 credits)

---

## Troubleshooting

### "Email already exists"
- Each student must have a unique email
- Try a different email address

### "Student/Course not found"
- Verify the ID is correct
- Use option to view all to see available IDs

### "Invalid input format"
- For IDs and numbers, enter only digits
- For text, type the actual value

### "GPA must be between 0.0 and 4.0"
- GPA values must be in the range 0.0 to 4.0
- Example valid values: 3.5, 3.85, 4.0

---

## Running Tests

The program is fully testable. Run tests separately:

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test class
pytest test_student_dao.py::TestStudentDAOCreate -v
```

The CLI doesn't interfere with the test suite.

---

## Differences from Old main.py

| Old Version | New Version |
|-------------|-------------|
| Automatic demonstration | Interactive menu |
| No user input | Full user control |
| Read-only operations | Full CRUD operations |
| Static output | Dynamic based on inputs |
| Single run | Loop until exit |

---

## Next Steps

1. **Run the program**: `python main.py`
2. **Explore the menus**: Try different operations
3. **Create test data**: Add your own students and courses
4. **Test enrollments**: Practice managing course enrollments
5. **Review code**: Check how operations are implemented

Enjoy exploring the Student Management System!
