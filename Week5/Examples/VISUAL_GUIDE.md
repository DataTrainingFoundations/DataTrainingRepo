# 🎯 Interactive CLI - Visual Guide

## Program Flow Diagram

```
┌─────────────────────────────────────┐
│  START: python main.py              │
└────────────────┬────────────────────┘
                 │
                 ▼
         ┌───────────────┐
         │  Initialize   │
         │  Database     │
         │  (seed data)  │
         └───────┬───────┘
                 │
                 ▼
    ╔════════════════════════╗
    ║      MAIN MENU         ║
    ╠════════════════════════╣
    ║  1. Student Mgmt       ║
    ║  2. Course Mgmt        ║
    ║  3. View All Data      ║
    ║  4. Reset Database     ║
    ║  5. Exit               ║
    ╚════════════════════════╝
         │      │      │      │       │
         │      │      │      │       └──→ EXIT
         │      │      │      │
         │      │      │      └──→ ┌──────────────┐
         │      │      │           │ Reset Data   │
         │      │      │           │ Confirm: Y/N │
         │      │      │           └──────────────┘
         │      │      │
         │      │      └──→ View all students + courses
         │      │
         │      └──→ ╔═════════════════════════╗
         │           ║   COURSE MENU (8 ops)   ║
         │           ╠═════════════════════════╣
         │           ║  1. Create Course       ║
         │           ║  2. View by ID          ║
         │           ║  3. View by Code        ║
         │           ║  4. View All            ║
         │           ║  5. Update Course       ║
         │           ║  6. Delete Course       ║
         │           ║  7. Manage Enrollments  ║
         │           ║  8. Back                ║
         │           ╚═════════════════════════╝
         │                  │
         │                  └──→ ╔════════════════════════╗
         │                       ║ ENROLLMENT MENU (4)    ║
         │                       ╠════════════════════════╣
         │                       ║  1. Enroll Student     ║
         │                       ║  2. Unenroll Student   ║
         │                       ║  3. View Students      ║
         │                       ║  4. Back               ║
         │                       ╚════════════════════════╝
         │
         └──→ ╔═════════════════════════╗
             ║   STUDENT MENU (8 ops)   ║
             ╠═════════════════════════╣
             ║  1. Create Student      ║
             ║  2. View by ID          ║
             ║  3. View by Email       ║
             ║  4. View All            ║
             ║  5. Update Student      ║
             ║  6. Delete Student      ║
             ║  7. View by GPA Range   ║
             ║  8. Back                ║
             ╚═════════════════════════╝
```

---

## Operation Categories

### 📝 CREATE Operations (2)
```
Student Menu → 1: Create Student
├─ Input: Name, Email, GPA
├─ Validation: Email unique, GPA 0.0-4.0
└─ Output: Student ID + details

Course Menu → 1: Create Course
├─ Input: Name, Code, Credits
├─ Validation: Code unique, Credits > 0
└─ Output: Course ID + details
```

### 🔍 READ Operations (8)
```
Student Operations (5):
├─ View by ID → Input: Student ID
├─ View by Email → Input: Email
├─ View All → Shows all students
├─ View by GPA → Input: Min, Max GPA
└─ [View from Detail Display]

Course Operations (3):
├─ View by ID → Input: Course ID
├─ View by Code → Input: Course Code
└─ View All → Shows all courses
```

### ✏️ UPDATE Operations (2)
```
Student Menu → 5: Update Student
├─ Input: Student ID
├─ Prompt: New name, email, GPA (skip = press Enter)
├─ Validation: GPA 0.0-4.0, unique email
└─ Output: Updated student details

Course Menu → 5: Update Course
├─ Input: Course ID
├─ Prompt: New name, code, credits (skip = press Enter)
├─ Validation: Credits > 0, unique code
└─ Output: Updated course details
```

### 🗑️ DELETE Operations (2)
```
Student Menu → 6: Delete Student
├─ Input: Student ID
├─ Confirmation: "Are you sure? (yes/no)"
└─ Output: Confirmation message

Course Menu → 6: Delete Course
├─ Input: Course ID
├─ Confirmation: "Are you sure? (yes/no)"
└─ Output: Confirmation message
```

### 👥 ENROLLMENT Operations (3)
```
Course Menu → 7: Manage Enrollments
├─ 1: Enroll Student
│  ├─ Input: Course ID, Student ID
│  └─ Output: Enrollment confirmation
├─ 2: Unenroll Student
│  ├─ Input: Course ID, Student ID
│  └─ Output: Unenrollment confirmation
└─ 3: View Students in Course
   ├─ Input: Course ID
   └─ Output: List of enrolled students
```

---

## Data Input/Output Flow

### Student Creation Flow
```
CREATE STUDENT
    │
    ├─→ User Input: Name
    │   └─→ Validate: Not empty
    │
    ├─→ User Input: Email
    │   └─→ Validate: Not empty, Unique
    │
    ├─→ User Input: GPA (optional)
    │   └─→ Validate: 0.0-4.0 (if provided)
    │
    ├─→ Database Insert
    │   └─→ Auto-assign ID
    │
    └─→ Display Output
        ├─ ID: 6
        ├─ Name: John Smith
        ├─ Email: john@test.edu
        └─ GPA: 3.8
```

### Student Update Flow
```
UPDATE STUDENT
    │
    ├─→ User Input: Student ID
    │   └─→ Fetch: Current details
    │
    ├─→ Display: Current Info
    │
    ├─→ User Input: New values (or skip)
    │   ├─ Name: [press Enter to skip]
    │   ├─ Email: [press Enter to skip]
    │   └─ GPA: 3.95
    │
    ├─→ Validate: Updated values
    │
    ├─→ Database Update
    │
    └─→ Display Output
        ├─ Name: John Smith (unchanged)
        ├─ Email: john@test.edu (unchanged)
        └─ GPA: 3.95 (updated)
```

### Enrollment Flow
```
ENROLL STUDENT
    │
    ├─→ User Input: Course ID
    │   └─→ Fetch: Course details
    │
    ├─→ User Input: Student ID
    │   └─→ Fetch: Student details
    │
    ├─→ Validate: Both exist
    │
    ├─→ Database Insert: Association
    │
    └─→ Output: "Alice Johnson enrolled in CS101"
```

---

## Error Handling Flow

### Duplicate Email Error
```
CREATE STUDENT
    │
    ├─→ Input: Email = "alice@test.edu" (exists)
    │
    ├─→ Validate: Check uniqueness
    │
    ├─→ Error: Email already exists
    │
    └─→ Output: "❌ Error creating student: Failed to create student"
        └─→ Return to menu
```

### Invalid GPA Error
```
UPDATE STUDENT
    │
    ├─→ Input: GPA = 5.0
    │
    ├─→ Validate: 0.0 ≤ GPA ≤ 4.0
    │
    ├─→ Error: GPA out of range
    │
    └─→ Output: "❌ GPA must be between 0.0 and 4.0"
        └─→ Return to menu
```

### Not Found Error
```
DELETE STUDENT
    │
    ├─→ Input: ID = 9999
    │
    ├─→ Lookup: Query database
    │
    ├─→ Error: No match found
    │
    └─→ Output: "❌ Student with ID 9999 not found"
        └─→ Return to menu
```

---

## Menu Navigation Flow

```
┌─────────────────┐
│   MAIN MENU     │
└────────┬────────┘
         │
    ┌────┴─────────────────────────────┐
    │                                   │
    ▼                                   ▼
┌──────────────┐                 ┌──────────────┐
│STUDENT MENU  │                 │ COURSE MENU  │
├──────────────┤                 ├──────────────┤
│ 1. Create    │                 │ 1. Create    │
│ 2. View (ID) │                 │ 2. View (ID) │
│ 3. View (E)  │                 │ 3. View (C)  │
│ 4. View All  │                 │ 4. View All  │
│ 5. Update    │                 │ 5. Update    │
│ 6. Delete    │                 │ 6. Delete    │
│ 7. View GPA  │                 │ 7. Manage EN │
│ 8. Back ←───────────────────────→ 8. Back      │
└──────────────┘                 └──────┬───────┘
                                        │
                                        ▼
                                ┌────────────────┐
                                │ ENROLLMENT     │
                                ├────────────────┤
                                │ 1. Enroll      │
                                │ 2. Unenroll    │
                                │ 3. View List   │
                                │ 4. Back ←──────┘
                                └────────────────┘
```

---

## Sample Interaction Timeline

```
[1] python main.py
    └─→ Database initialized with 5 students, 4 courses

[2] Main Menu: 1 (Student Management)
    └─→ Shows Student Menu

[3] Student Menu: 1 (Create Student)
    ├─→ Prompts: Name, Email, GPA
    ├─→ User inputs: "John Smith", "john@test.edu", "3.8"
    └─→ Output: "✅ Student created! ID: 6"

[4] Student Menu: 8 (Back)
    └─→ Returns to Main Menu

[5] Main Menu: 2 (Course Management)
    └─→ Shows Course Menu

[6] Course Menu: 7 (Manage Enrollments)
    └─→ Shows Enrollment Menu

[7] Enrollment Menu: 1 (Enroll)
    ├─→ Prompts: Course ID, Student ID
    ├─→ User inputs: "1", "6"
    └─→ Output: "✅ John Smith enrolled in CS101!"

[8] Enrollment Menu: 4 (Back)
    └─→ Returns to Course Menu

[9] Course Menu: 8 (Back)
    └─→ Returns to Main Menu

[10] Main Menu: 5 (Exit)
     └─→ "👋 Thank you for using Student Management System!"
```

---

## Visual Output Examples

### Success Message
```
✅ Student created successfully!
   ID: 6
   Name: John Smith
   Email: john@test.edu
   GPA: 3.8
```

### Error Message
```
❌ Error creating student: (Email already exists)
```

### List Output
```
📚 ALL STUDENTS
----------------------------------------
  ID 1: Alice Johnson
    Email: alice@test.edu | GPA: 3.85
    Enrolled in 3 courses

  ID 2: Bob Smith
    Email: bob@test.edu | GPA: 3.45
    Enrolled in 2 courses
```

### Confirmation Prompt
```
🗑️  DELETE STUDENT
----------------------------------------
About to delete: John Smith (john@test.edu)
Are you sure? (yes/no): _
```

---

## Color & Emoji Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Success / Confirmation |
| ❌ | Error / Failure |
| 📚 | List / Inventory |
| 🔍 | Search / View |
| ✏️ | Update / Edit |
| 🗑️ | Delete / Remove |
| 👥 | Enrollment / People |
| ⚠️ | Warning / Caution |
| 📝 | Create / Input |
| 📊 | Report / Analytics |
| 🔧 | Configuration / Setup |

---

## Quick Navigation Keys

| Input | Action |
|-------|--------|
| 1-8 | Select menu option |
| Enter | Confirm selection |
| Enter (blank) | Skip field (updates) |
| yes/y | Confirm deletion |
| no/n | Cancel operation |
| Ctrl+C | Force exit (emergency) |

---

## Complete Operation Reference

### TOTAL: 26 Operations

**Student (8)**: Create, View(ID), View(Email), View(All), Update, Delete, View(GPA), Back
**Course (8)**: Create, View(ID), View(Code), View(All), Update, Delete, Manage(EN), Back
**Enrollment (4)**: Enroll, Unenroll, View, Back
**System (2)**: View All Data, Reset DB
**Navigation (4)**: Main→Student, Main→Course, Course→Enrollment, All Back options

---

This visual guide helps understand the complete flow and structure of the interactive CLI! 🎯
