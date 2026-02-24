# Interactive CLI Demo Script

## Quick Demo - Run These Commands in Sequence

Here's a step-by-step walkthrough you can follow:

### 1. Start the Program
```bash
python main.py
```

You'll see the welcome message and main menu.

### 2. Create a New Student (Option 1 > 1)

When prompted:
```
Main Menu > 1 (Student Management) > 1 (Create Student)

Enter student name: Sarah Johnson
Enter email address: sarah.johnson@university.edu
Enter GPA (0.0-4.0, default 0.0): 3.9
```

Expected output:
```
✅ Student created successfully!
   ID: 6
   Name: Sarah Johnson
   Email: sarah.johnson@university.edu
   GPA: 3.9
```

### 3. Create a New Course (Option 2 > 1)

When prompted:
```
Main Menu > 2 (Course Management) > 1 (Create Course)

Enter course name: Machine Learning Basics
Enter course code (e.g., CS101): CS450
Enter credits (default 3): 3
```

Expected output:
```
✅ Course created successfully!
   ID: 5
   Code: CS450
   Name: Machine Learning Basics
   Credits: 3
```

### 4. Enroll the Student (Option 2 > 7 > 1)

When prompted:
```
Main Menu > 2 (Course Management) > 7 (Manage Enrollments) > 1 (Enroll Student)

Enter course ID: 5
Enter student ID: 6
```

Expected output:
```
✅ Sarah Johnson enrolled in CS450 successfully!
```

### 5. View Student Details (Option 1 > 2)

When prompted:
```
Main Menu > 1 (Student Management) > 2 (View Student by ID)

Enter student ID: 6
```

Expected output:
```
✅ STUDENT DETAILS
----------------------------------------
ID:       6
Name:     Sarah Johnson
Email:    sarah.johnson@university.edu
GPA:      3.9
Courses:  1
  Enrolled in:
    • CS450 - Machine Learning Basics
```

### 6. View Course Details (Option 2 > 2)

When prompted:
```
Main Menu > 2 (Course Management) > 2 (View Course by ID)

Enter course ID: 5
```

Expected output:
```
✅ COURSE DETAILS
----------------------------------------
ID:       5
Code:     CS450
Name:     Machine Learning Basics
Credits:  3
Students: 1
  Enrolled students:
    • Sarah Johnson (GPA: 3.9)
```

### 7. Update Student GPA (Option 1 > 5)

When prompted:
```
Main Menu > 1 (Student Management) > 5 (Update Student)

Enter student ID: 6

Current Info: Sarah Johnson | sarah.johnson@university.edu | GPA: 3.9
Leave field blank to skip (no change)

Enter new name (or press Enter to skip): [press Enter]
Enter new email (or press Enter to skip): [press Enter]
Enter new GPA (or press Enter to skip): 3.95
```

Expected output:
```
✅ Student updated successfully!
ID:       6
Name:     Sarah Johnson
Email:    sarah.johnson@university.edu
GPA:      3.95
Courses:  1
  Enrolled in:
    • CS450 - Machine Learning Basics
```

### 8. View All Students (Option 1 > 4)

When prompted:
```
Main Menu > 1 (Student Management) > 4 (View All Students)
```

Expected output:
```
📚 ALL STUDENTS
----------------------------------------
  ID 1: Alice Johnson
    Email: alice.johnson@university.edu | GPA: 3.85
    Enrolled in 3 courses

  ID 2: Bob Smith
    Email: bob.smith@university.edu | GPA: 3.45
    Enrolled in 2 courses

[... more students ...]

  ID 6: Sarah Johnson
    Email: sarah.johnson@university.edu | GPA: 3.95
    Enrolled in 1 courses
```

### 9. View All Courses (Option 2 > 4)

When prompted:
```
Main Menu > 2 (Course Management) > 4 (View All Courses)
```

Expected output:
```
📚 ALL COURSES
----------------------------------------
  ID 1: CS101 - Introduction to Computer Science
    Credits: 3 | Students: 3

  ID 2: CS201 - Data Structures
    Credits: 4 | Students: 2

[... more courses ...]

  ID 5: CS450 - Machine Learning Basics
    Credits: 3 | Students: 1
```

### 10. View All Data (Option 3)

When prompted:
```
Main Menu > 3 (View All Data)
```

Shows comprehensive list of:
- All students with details
- All courses with details

### 11. Try Error Handling

#### Try creating duplicate email (should fail):
```
Main Menu > 1 > 1

Enter student name: Test Student
Enter email address: sarah.johnson@university.edu
Enter GPA (0.0-4.0, default 0.0): 3.5

❌ Error creating student: Failed to create student: (...)
```

#### Try invalid GPA (should fail):
```
Main Menu > 1 > 1

Enter student name: Another Student
Enter email address: another@test.edu
Enter GPA (0.0-4.0, default 0.0): 5.0

❌ GPA must be between 0.0 and 4.0
```

### 12. Reset Database (Option 4)

When prompted:
```
Main Menu > 4 (Reset Database)

⚠️  RESET DATABASE
This will delete all data. Are you sure? (yes/no): yes

🔧 Initializing database...
Sample data successfully seeded to the database.
✓ Database initialized with sample data

✅ Database reset successfully!
```

### 13. Exit Program (Option 5)

When prompted:
```
Main Menu > 5 (Exit)

👋 Thank you for using Student Management System!
```

---

## Interactive Menu Flow Diagram

```
START
  │
  ├─→ MAIN MENU
       │
       ├─ 1 → STUDENT MENU
       │      ├─ 1 → Create Student
       │      ├─ 2 → View by ID
       │      ├─ 3 → View by Email
       │      ├─ 4 → View All
       │      ├─ 5 → Update
       │      ├─ 6 → Delete
       │      ├─ 7 → View by GPA Range
       │      └─ 8 → Back
       │
       ├─ 2 → COURSE MENU
       │      ├─ 1 → Create Course
       │      ├─ 2 → View by ID
       │      ├─ 3 → View by Code
       │      ├─ 4 → View All
       │      ├─ 5 → Update
       │      ├─ 6 → Delete
       │      ├─ 7 → ENROLLMENT MENU
       │      │     ├─ 1 → Enroll Student
       │      │     ├─ 2 → Unenroll Student
       │      │     ├─ 3 → View Course Students
       │      │     └─ 4 → Back
       │      └─ 8 → Back
       │
       ├─ 3 → View All Data
       │      (Students + Courses)
       │
       ├─ 4 → Reset Database
       │      (Confirm: yes/no)
       │
       └─ 5 → EXIT

```

---

## Common Tasks Reference

### Add a course and enroll multiple students:
1. Create course (Menu: 2 > 1)
2. Enroll student 1 (Menu: 2 > 7 > 1)
3. Enroll student 2 (Menu: 2 > 7 > 1)
4. View students in course (Menu: 2 > 7 > 3)

### Update multiple students:
1. View all (Menu: 1 > 4) - to see IDs
2. Update student 1 (Menu: 1 > 5)
3. Update student 2 (Menu: 1 > 5)

### Find high GPA students:
1. View by GPA range (Menu: 1 > 7)
2. Enter min: 3.8
3. Enter max: 4.0

### Manage course enrollments:
1. Create course (Menu: 2 > 1)
2. Enroll students (Menu: 2 > 7 > 1)
3. View enrolled (Menu: 2 > 7 > 3)
4. Unenroll if needed (Menu: 2 > 7 > 2)

---

## Expected Output Features

✅ **Clear Headers** - Each section marked with = separators
✅ **Emoji Indicators** - Visual feedback (✅, ❌, 📚, 🔍, etc.)
✅ **Validation** - Input checking with helpful error messages
✅ **Confirmation** - Delete operations require confirmation
✅ **Detailed Display** - Full information about created/viewed records
✅ **Relationships** - Shows related data (courses for students, etc.)
✅ **Continue Prompt** - "Press Enter to continue..." after each operation

---

## That's It!

You now have a fully interactive CLI for managing students and courses.

- **Create** new students and courses
- **Read** details by ID, email, or code
- **Update** information with flexible field selection
- **Delete** with confirmation protection
- **Manage enrollments** between students and courses
- **View relationships** automatically displayed

Enjoy! 🚀
