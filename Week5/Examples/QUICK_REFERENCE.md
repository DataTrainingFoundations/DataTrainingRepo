# Quick Reference Card - Interactive CLI

## Launch Program
```bash
python main.py
```

## Menu Navigation
- Type a number (1-8) to select an option
- Press Enter to confirm
- Follow the on-screen prompts

---

## Main Menu (Always Available)

```
1 → Student Management
2 → Course Management  
3 → View All Data
4 → Reset Database
5 → Exit
```

---

## Student Operations (Menu 1)

| # | Operation | Input | Purpose |
|---|-----------|-------|---------|
| 1 | Create | name, email, GPA | Add new student |
| 2 | View by ID | student ID | Get details |
| 3 | View by Email | email | Search student |
| 4 | View All | (none) | List all students |
| 5 | Update | ID + new values | Modify student |
| 6 | Delete | ID | Remove student |
| 7 | View by GPA | min GPA, max GPA | Filter students |
| 8 | Back | (none) | Return to main |

### Student Fields
- **ID**: Auto-generated (read-only)
- **Name**: Required text
- **Email**: Required, unique text
- **GPA**: 0.0-4.0 (decimal)

---

## Course Operations (Menu 2)

| # | Operation | Input | Purpose |
|---|-----------|-------|---------|
| 1 | Create | name, code, credits | Add new course |
| 2 | View by ID | course ID | Get details |
| 3 | View by Code | course code | Search course |
| 4 | View All | (none) | List all courses |
| 5 | Update | ID + new values | Modify course |
| 6 | Delete | ID | Remove course |
| 7 | Manage Enrollments | (submenu) | See menu below |
| 8 | Back | (none) | Return to main |

### Course Fields
- **ID**: Auto-generated (read-only)
- **Code**: Required, unique text (e.g., CS101)
- **Name**: Required text
- **Credits**: Integer > 0 (default: 3)

---

## Enrollment Operations (Menu 2→7)

| # | Operation | Input | Purpose |
|---|-----------|-------|---------|
| 1 | Enroll | course ID, student ID | Add to course |
| 2 | Unenroll | course ID, student ID | Remove from course |
| 3 | View Students | course ID | See enrolled |
| 4 | Back | (none) | Return to courses |

---

## Input Tips

### Required Fields
- Cannot be empty
- Must match specified format

### Optional Fields (Updates Only)
```
Enter new field (or press Enter to skip): [press Enter]
```

### Validation Rules

**Email**
- Must be unique
- Format: name@domain.edu

**GPA**
- Range: 0.0 - 4.0
- Must be a decimal number

**ID**
- Must be a positive integer
- Check "View All" to find IDs

**Credits**
- Must be > 0
- Default: 3

---

## Output Symbols

```
✅ Success indicator (green check)
❌ Error indicator (red X)
📚 Student/Course list
🔍 Search/View operation
✏️  Update operation
🗑️  Delete operation
👥 Enrollment operation
⚠️  Warning/Confirmation
```

---

## Common Workflows

### Create Student + Enroll
1. Menu 1 → 1: Create Student
2. Menu 2 → View All (note course ID)
3. Menu 2 → 7 → 1: Enroll (use IDs)

### Quick Lookup
1. Menu 1 → 4: View all (see all students)
2. Menu 2 → 4: View all (see all courses)

### Update & Delete
1. Menu → View All (find ID)
2. Menu → Update (ID + new values)
3. Menu → Delete (ID + confirm)

### Reset Everything
1. Menu 4: Reset Database
2. Confirm: yes
3. Done!

---

## Sample Data (On Startup)

**Students**: 5 total
- Alice Johnson - GPA 3.85
- Bob Smith - GPA 3.45
- Carol White - GPA 3.92
- David Brown - GPA 3.10
- Eve Davis - GPA 3.75

**Courses**: 4 total
- CS101: Intro to CS (3 cr)
- CS201: Data Structures (4 cr)
- CS301: Database Systems (3 cr)
- CS105: Web Dev (3 cr)

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "Email already exists" | Use unique email |
| "Not found" | Check ID with View All |
| "Invalid input" | Use correct format (number/text) |
| "GPA out of range" | Enter 0.0-4.0 |
| "Credits invalid" | Must be positive number |

---

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| 1-8 | Select menu |
| Enter | Confirm, Continue |
| Ctrl+C | Exit program (force) |

---

## File Reference

```
CLI_GUIDE.md             Full user guide
INTERACTIVE_DEMO.md      Step-by-step examples
CLI_IMPLEMENTATION.md    How it works
README.md                Project docs
```

---

## Testing

```bash
pytest                   # Run all 52 tests
pytest -v               # Verbose output
pytest test_student_dao.py  # Student tests only
pytest test_course_dao.py   # Course tests only
```

**Status**: ✅ All 52 tests pass

---

## Quick Start

```bash
# 1. Run program
python main.py

# 2. Create student
Menu: 1 → 1
Input: name, email, GPA

# 3. Create course
Menu: 2 → 1
Input: name, code, credits

# 4. Enroll student
Menu: 2 → 7 → 1
Input: course ID, student ID

# 5. View results
Menu: 1 → 2 (or 4)
Menu: 2 → 2 (or 4)
```

---

## Help

**In the program**: Follow on-screen prompts
**User Guide**: Read CLI_GUIDE.md
**Examples**: See INTERACTIVE_DEMO.md
**Errors**: Error message explains problem

---

**Ready to go!** 🚀 Type: `python main.py`
