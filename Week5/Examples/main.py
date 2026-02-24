"""
Interactive CLI for Student and Course Management System using DAO pattern.

This module provides an interactive command-line interface for performing
CRUD operations on Students and Courses with clear prompts and instructions.

Run this file with: python main.py
"""

from typing import Optional
from database import db_manager
from student_dao import StudentDAO
from course_dao import CourseDAO
from models import Student, Course


class StudentManagementCLI:
    """Interactive CLI for managing students and courses."""
    
    def __init__(self):
        """Initialize the CLI and database."""
        self.initialize_database()
    
    def initialize_database(self) -> None:
        """Initialize database with tables and sample data."""
        print("\n🔧 Initializing database...")
        try:
            db_manager.drop_tables()
            db_manager.create_tables()
            db_manager.seed_sample_data()
            print("✓ Database initialized with sample data\n")
        except Exception as e:
            print(f"❌ Error initializing database: {e}")
            raise
    
    def print_header(self, title: str) -> None:
        """Print a formatted header."""
        print(f"\n{'='*60}")
        print(f"  {title}")
        print(f"{'='*60}\n")
    
    def print_menu(self) -> None:
        """Display the main menu."""
        self.print_header("MAIN MENU")
        print("Select what you want to manage:")
        print("  1. Student Management")
        print("  2. Course Management")
        print("  3. View All Data")
        print("  4. Reset Database")
        print("  5. Exit")
        print()
    
    def print_student_menu(self) -> None:
        """Display the student operations menu."""
        self.print_header("STUDENT OPERATIONS")
        print("Choose an operation:")
        print("  1. Create Student")
        print("  2. View Student by ID")
        print("  3. View Student by Email")
        print("  4. View All Students")
        print("  5. Update Student")
        print("  6. Delete Student")
        print("  7. View Students by GPA Range")
        print("  8. Back to Main Menu")
        print()
    
    def print_course_menu(self) -> None:
        """Display the course operations menu."""
        self.print_header("COURSE OPERATIONS")
        print("Choose an operation:")
        print("  1. Create Course")
        print("  2. View Course by ID")
        print("  3. View Course by Code")
        print("  4. View All Courses")
        print("  5. Update Course")
        print("  6. Delete Course")
        print("  7. Manage Enrollments")
        print("  8. Back to Main Menu")
        print()
    
    def print_enrollment_menu(self) -> None:
        """Display the enrollment operations menu."""
        self.print_header("ENROLLMENT OPERATIONS")
        print("Choose an operation:")
        print("  1. Enroll Student in Course")
        print("  2. Unenroll Student from Course")
        print("  3. View Students in Course")
        print("  4. Back to Course Menu")
        print()
    
    # ========== Student Operations ==========
    
    def create_student(self) -> None:
        """Create a new student."""
        print("\n📝 CREATE NEW STUDENT")
        print("-" * 40)
        try:
            name = input("Enter student name: ").strip()
            if not name:
                print("❌ Name cannot be empty")
                return
            
            email = input("Enter email address: ").strip()
            if not email:
                print("❌ Email cannot be empty")
                return
            
            gpa_input = input("Enter GPA (0.0-4.0, default 0.0): ").strip()
            gpa = 0.0 if not gpa_input else float(gpa_input)
            
            if not 0.0 <= gpa <= 4.0:
                print("❌ GPA must be between 0.0 and 4.0")
                return
            
            with StudentDAO(db_manager.get_session()) as dao:
                student = dao.create(name, email, gpa)
                print(f"\n✅ Student created successfully!")
                print(f"   ID: {student.id}")
                print(f"   Name: {student.name}")
                print(f"   Email: {student.email}")
                print(f"   GPA: {student.gpa}")
        
        except ValueError:
            print("❌ Invalid input format")
        except Exception as e:
            print(f"❌ Error creating student: {e}")
    
    def view_student_by_id(self) -> None:
        """View a student by ID."""
        print("\n🔍 VIEW STUDENT BY ID")
        print("-" * 40)
        try:
            student_id = int(input("Enter student ID: "))
            
            with StudentDAO(db_manager.get_session()) as dao:
                student = dao.read_by_id(student_id)
                if student:
                    self.display_student(student)
                else:
                    print(f"❌ Student with ID {student_id} not found")
        
        except ValueError:
            print("❌ ID must be a number")
        except Exception as e:
            print(f"❌ Error retrieving student: {e}")
    
    def view_student_by_email(self) -> None:
        """View a student by email."""
        print("\n🔍 VIEW STUDENT BY EMAIL")
        print("-" * 40)
        try:
            email = input("Enter email address: ").strip()
            
            with StudentDAO(db_manager.get_session()) as dao:
                student = dao.read_by_email(email)
                if student:
                    self.display_student(student)
                else:
                    print(f"❌ Student with email '{email}' not found")
        
        except Exception as e:
            print(f"❌ Error retrieving student: {e}")
    
    def view_all_students(self) -> None:
        """View all students."""
        print("\n📚 ALL STUDENTS")
        print("-" * 40)
        try:
            with StudentDAO(db_manager.get_session()) as dao:
                students = dao.read_all()
                if students:
                    for student in students:
                        print(f"  ID {student.id}: {student.name}")
                        print(f"    Email: {student.email} | GPA: {student.gpa}")
                        print(f"    Enrolled in {len(student.courses)} courses")
                        print()
                else:
                    print("❌ No students in database")
        
        except Exception as e:
            print(f"❌ Error retrieving students: {e}")
    
    def update_student(self) -> None:
        """Update a student."""
        print("\n✏️  UPDATE STUDENT")
        print("-" * 40)
        try:
            student_id = int(input("Enter student ID: "))
            
            with StudentDAO(db_manager.get_session()) as dao:
                student = dao.read_by_id(student_id)
                if not student:
                    print(f"❌ Student with ID {student_id} not found")
                    return
                
                print(f"\nCurrent Info: {student.name} | {student.email} | GPA: {student.gpa}")
                print("Leave field blank to skip (no change)")
                
                new_name = input("Enter new name (or press Enter to skip): ").strip() or None
                new_email = input("Enter new email (or press Enter to skip): ").strip() or None
                new_gpa_input = input("Enter new GPA (or press Enter to skip): ").strip()
                new_gpa = None if not new_gpa_input else float(new_gpa_input)
                
                if new_gpa is not None and not 0.0 <= new_gpa <= 4.0:
                    print("❌ GPA must be between 0.0 and 4.0")
                    return
                
                updated = dao.update(student_id, name=new_name, email=new_email, gpa=new_gpa)
                
                if updated:
                    print(f"\n✅ Student updated successfully!")
                    self.display_student(updated)
                else:
                    print("❌ Failed to update student")
        
        except ValueError:
            print("❌ Invalid input format")
        except Exception as e:
            print(f"❌ Error updating student: {e}")
    
    def delete_student(self) -> None:
        """Delete a student."""
        print("\n🗑️  DELETE STUDENT")
        print("-" * 40)
        try:
            student_id = int(input("Enter student ID: "))
            
            with StudentDAO(db_manager.get_session()) as dao:
                student = dao.read_by_id(student_id)
                if not student:
                    print(f"❌ Student with ID {student_id} not found")
                    return
                
                print(f"\nAbout to delete: {student.name} ({student.email})")
                confirm = input("Are you sure? (yes/no): ").strip().lower()
                
                if confirm in ['yes', 'y']:
                    if dao.delete(student_id):
                        print(f"✅ Student deleted successfully!")
                    else:
                        print("❌ Failed to delete student")
                else:
                    print("❌ Deletion cancelled")
        
        except ValueError:
            print("❌ ID must be a number")
        except Exception as e:
            print(f"❌ Error deleting student: {e}")
    
    def view_students_by_gpa_range(self) -> None:
        """View students within a GPA range."""
        print("\n📊 VIEW STUDENTS BY GPA RANGE")
        print("-" * 40)
        try:
            min_gpa = float(input("Enter minimum GPA: "))
            max_gpa = float(input("Enter maximum GPA: "))
            
            if not (0.0 <= min_gpa <= 4.0) or not (0.0 <= max_gpa <= 4.0):
                print("❌ GPA values must be between 0.0 and 4.0")
                return
            
            if min_gpa > max_gpa:
                print("❌ Minimum GPA cannot be greater than maximum GPA")
                return
            
            with StudentDAO(db_manager.get_session()) as dao:
                students = dao.read_by_gpa_range(min_gpa, max_gpa)
                if students:
                    print(f"\n✅ Found {len(students)} students with GPA between {min_gpa} and {max_gpa}:")
                    for student in students:
                        print(f"  • {student.name}: GPA {student.gpa} ({student.email})")
                else:
                    print(f"❌ No students found with GPA between {min_gpa} and {max_gpa}")
        
        except ValueError:
            print("❌ GPA must be a number")
        except Exception as e:
            print(f"❌ Error retrieving students: {e}")
    
    # ========== Course Operations ==========
    
    def create_course(self) -> None:
        """Create a new course."""
        print("\n📝 CREATE NEW COURSE")
        print("-" * 40)
        try:
            name = input("Enter course name: ").strip()
            if not name:
                print("❌ Course name cannot be empty")
                return
            
            code = input("Enter course code (e.g., CS101): ").strip()
            if not code:
                print("❌ Course code cannot be empty")
                return
            
            credits_input = input("Enter credits (default 3): ").strip()
            credits = 3 if not credits_input else int(credits_input)
            
            if credits <= 0:
                print("❌ Credits must be greater than 0")
                return
            
            with CourseDAO(db_manager.get_session()) as dao:
                course = dao.create(name, code, credits)
                print(f"\n✅ Course created successfully!")
                print(f"   ID: {course.id}")
                print(f"   Code: {course.code}")
                print(f"   Name: {course.name}")
                print(f"   Credits: {course.credits}")
        
        except ValueError:
            print("❌ Credits must be a number")
        except Exception as e:
            print(f"❌ Error creating course: {e}")
    
    def view_course_by_id(self) -> None:
        """View a course by ID."""
        print("\n🔍 VIEW COURSE BY ID")
        print("-" * 40)
        try:
            course_id = int(input("Enter course ID: "))
            
            with CourseDAO(db_manager.get_session()) as dao:
                course = dao.read_by_id(course_id)
                if course:
                    self.display_course(course)
                else:
                    print(f"❌ Course with ID {course_id} not found")
        
        except ValueError:
            print("❌ ID must be a number")
        except Exception as e:
            print(f"❌ Error retrieving course: {e}")
    
    def view_course_by_code(self) -> None:
        """View a course by code."""
        print("\n🔍 VIEW COURSE BY CODE")
        print("-" * 40)
        try:
            code = input("Enter course code: ").strip()
            
            with CourseDAO(db_manager.get_session()) as dao:
                course = dao.read_by_code(code)
                if course:
                    self.display_course(course)
                else:
                    print(f"❌ Course with code '{code}' not found")
        
        except Exception as e:
            print(f"❌ Error retrieving course: {e}")
    
    def view_all_courses(self) -> None:
        """View all courses."""
        print("\n📚 ALL COURSES")
        print("-" * 40)
        try:
            with CourseDAO(db_manager.get_session()) as dao:
                courses = dao.read_all()
                if courses:
                    for course in courses:
                        print(f"  ID {course.id}: {course.code} - {course.name}")
                        print(f"    Credits: {course.credits} | Students: {len(course.students)}")
                        print()
                else:
                    print("❌ No courses in database")
        
        except Exception as e:
            print(f"❌ Error retrieving courses: {e}")
    
    def update_course(self) -> None:
        """Update a course."""
        print("\n✏️  UPDATE COURSE")
        print("-" * 40)
        try:
            course_id = int(input("Enter course ID: "))
            
            with CourseDAO(db_manager.get_session()) as dao:
                course = dao.read_by_id(course_id)
                if not course:
                    print(f"❌ Course with ID {course_id} not found")
                    return
                
                print(f"\nCurrent Info: {course.code} - {course.name} | Credits: {course.credits}")
                print("Leave field blank to skip (no change)")
                
                new_name = input("Enter new name (or press Enter to skip): ").strip() or None
                new_code = input("Enter new code (or press Enter to skip): ").strip() or None
                new_credits_input = input("Enter new credits (or press Enter to skip): ").strip()
                new_credits = None if not new_credits_input else int(new_credits_input)
                
                if new_credits is not None and new_credits <= 0:
                    print("❌ Credits must be greater than 0")
                    return
                
                updated = dao.update(course_id, name=new_name, code=new_code, credits=new_credits)
                
                if updated:
                    print(f"\n✅ Course updated successfully!")
                    self.display_course(updated)
                else:
                    print("❌ Failed to update course")
        
        except ValueError:
            print("❌ Invalid input format")
        except Exception as e:
            print(f"❌ Error updating course: {e}")
    
    def delete_course(self) -> None:
        """Delete a course."""
        print("\n🗑️  DELETE COURSE")
        print("-" * 40)
        try:
            course_id = int(input("Enter course ID: "))
            
            with CourseDAO(db_manager.get_session()) as dao:
                course = dao.read_by_id(course_id)
                if not course:
                    print(f"❌ Course with ID {course_id} not found")
                    return
                
                print(f"\nAbout to delete: {course.code} - {course.name}")
                confirm = input("Are you sure? (yes/no): ").strip().lower()
                
                if confirm in ['yes', 'y']:
                    if dao.delete(course_id):
                        print(f"✅ Course deleted successfully!")
                    else:
                        print("❌ Failed to delete course")
                else:
                    print("❌ Deletion cancelled")
        
        except ValueError:
            print("❌ ID must be a number")
        except Exception as e:
            print(f"❌ Error deleting course: {e}")
    
    # ========== Enrollment Operations ==========
    
    def enroll_student(self) -> None:
        """Enroll a student in a course."""
        print("\n👥 ENROLL STUDENT IN COURSE")
        print("-" * 40)
        try:
            course_id = int(input("Enter course ID: "))
            student_id = int(input("Enter student ID: "))
            
            with CourseDAO(db_manager.get_session()) as course_dao:
                course = course_dao.read_by_id(course_id)
                if not course:
                    print(f"❌ Course with ID {course_id} not found")
                    return
                
                student_dao = StudentDAO(course_dao.session)
                student = student_dao.read_by_id(student_id)
                if not student:
                    print(f"❌ Student with ID {student_id} not found")
                    return
                
                if course_dao.enroll_student(course_id, student_id):
                    print(f"\n✅ {student.name} enrolled in {course.code} successfully!")
                else:
                    print("❌ Failed to enroll student")
        
        except ValueError:
            print("❌ IDs must be numbers")
        except Exception as e:
            print(f"❌ Error enrolling student: {e}")
    
    def unenroll_student(self) -> None:
        """Unenroll a student from a course."""
        print("\n👥 UNENROLL STUDENT FROM COURSE")
        print("-" * 40)
        try:
            course_id = int(input("Enter course ID: "))
            student_id = int(input("Enter student ID: "))
            
            with CourseDAO(db_manager.get_session()) as course_dao:
                course = course_dao.read_by_id(course_id)
                if not course:
                    print(f"❌ Course with ID {course_id} not found")
                    return
                
                student_dao = StudentDAO(course_dao.session)
                student = student_dao.read_by_id(student_id)
                if not student:
                    print(f"❌ Student with ID {student_id} not found")
                    return
                
                if course_dao.unenroll_student(course_id, student_id):
                    print(f"\n✅ {student.name} unenrolled from {course.code} successfully!")
                else:
                    print("❌ Failed to unenroll student")
        
        except ValueError:
            print("❌ IDs must be numbers")
        except Exception as e:
            print(f"❌ Error unenrolling student: {e}")
    
    def view_course_students(self) -> None:
        """View all students in a course."""
        print("\n📋 VIEW STUDENTS IN COURSE")
        print("-" * 40)
        try:
            course_id = int(input("Enter course ID: "))
            
            with CourseDAO(db_manager.get_session()) as dao:
                course = dao.read_by_id(course_id)
                if not course:
                    print(f"❌ Course with ID {course_id} not found")
                    return
                
                students = dao.get_enrolled_students(course_id)
                if students:
                    print(f"\n✅ Students in {course.code} - {course.name}:")
                    for student in students:
                        print(f"  • {student.name} (ID: {student.id}, GPA: {student.gpa})")
                else:
                    print(f"❌ No students enrolled in {course.code}")
        
        except ValueError:
            print("❌ ID must be a number")
        except Exception as e:
            print(f"❌ Error retrieving students: {e}")
    
    # ========== Utility Methods ==========
    
    def display_student(self, student: Student) -> None:
        """Display formatted student information."""
        print(f"\n✅ STUDENT DETAILS")
        print("-" * 40)
        print(f"ID:       {student.id}")
        print(f"Name:     {student.name}")
        print(f"Email:    {student.email}")
        print(f"GPA:      {student.gpa}")
        print(f"Courses:  {len(student.courses)}")
        if student.courses:
            print("  Enrolled in:")
            for course in student.courses:
                print(f"    • {course.code} - {course.name}")
    
    def display_course(self, course: Course) -> None:
        """Display formatted course information."""
        print(f"\n✅ COURSE DETAILS")
        print("-" * 40)
        print(f"ID:       {course.id}")
        print(f"Code:     {course.code}")
        print(f"Name:     {course.name}")
        print(f"Credits:  {course.credits}")
        print(f"Students: {len(course.students)}")
        if course.students:
            print("  Enrolled students:")
            for student in course.students:
                print(f"    • {student.name} (GPA: {student.gpa})")
    
    def view_all_data(self) -> None:
        """View all students and courses."""
        self.print_header("DATABASE OVERVIEW")
        
        with StudentDAO(db_manager.get_session()) as student_dao:
            with CourseDAO(student_dao.session) as course_dao:
                # Students
                students = student_dao.read_all()
                print(f"📚 STUDENTS ({len(students)} total)")
                print("-" * 40)
                if students:
                    for student in students:
                        print(f"  {student.id}. {student.name} | {student.email} | GPA: {student.gpa}")
                else:
                    print("  No students in database")
                
                # Courses
                courses = course_dao.read_all()
                print(f"\n📚 COURSES ({len(courses)} total)")
                print("-" * 40)
                if courses:
                    for course in courses:
                        print(f"  {course.id}. {course.code} - {course.name} ({course.credits} credits)")
                else:
                    print("  No courses in database")
    
    def reset_database(self) -> None:
        """Reset the database."""
        print("\n⚠️  RESET DATABASE")
        print("-" * 40)
        confirm = input("This will delete all data. Are you sure? (yes/no): ").strip().lower()
        
        if confirm in ['yes', 'y']:
            try:
                self.initialize_database()
                print("✅ Database reset successfully!")
            except Exception as e:
                print(f"❌ Error resetting database: {e}")
        else:
            print("❌ Reset cancelled")
    
    # ========== Main Loop ==========
    
    def student_menu(self) -> None:
        """Display student management menu loop."""
        while True:
            self.print_student_menu()
            choice = input("Enter your choice (1-8): ").strip()
            
            if choice == '1':
                self.create_student()
            elif choice == '2':
                self.view_student_by_id()
            elif choice == '3':
                self.view_student_by_email()
            elif choice == '4':
                self.view_all_students()
            elif choice == '5':
                self.update_student()
            elif choice == '6':
                self.delete_student()
            elif choice == '7':
                self.view_students_by_gpa_range()
            elif choice == '8':
                break
            else:
                print("❌ Invalid choice. Please enter 1-8")
            
            input("\nPress Enter to continue...")
    
    def course_menu(self) -> None:
        """Display course management menu loop."""
        while True:
            self.print_course_menu()
            choice = input("Enter your choice (1-8): ").strip()
            
            if choice == '1':
                self.create_course()
            elif choice == '2':
                self.view_course_by_id()
            elif choice == '3':
                self.view_course_by_code()
            elif choice == '4':
                self.view_all_courses()
            elif choice == '5':
                self.update_course()
            elif choice == '6':
                self.delete_course()
            elif choice == '7':
                self.enrollment_menu()
            elif choice == '8':
                break
            else:
                print("❌ Invalid choice. Please enter 1-8")
            
            input("\nPress Enter to continue...")
    
    def enrollment_menu(self) -> None:
        """Display enrollment management menu loop."""
        while True:
            self.print_enrollment_menu()
            choice = input("Enter your choice (1-4): ").strip()
            
            if choice == '1':
                self.enroll_student()
            elif choice == '2':
                self.unenroll_student()
            elif choice == '3':
                self.view_course_students()
            elif choice == '4':
                break
            else:
                print("❌ Invalid choice. Please enter 1-4")
            
            input("\nPress Enter to continue...")
    
    def run(self) -> None:
        """Run the main CLI loop."""
        print("\n" + "="*60)
        print("  STUDENT MANAGEMENT SYSTEM - INTERACTIVE CLI")
        print("="*60)
        
        while True:
            self.print_menu()
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == '1':
                self.student_menu()
            elif choice == '2':
                self.course_menu()
            elif choice == '3':
                self.view_all_data()
            elif choice == '4':
                self.reset_database()
            elif choice == '5':
                print("\n👋 Thank you for using Student Management System!")
                break
            else:
                print("❌ Invalid choice. Please enter 1-5")
            
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    cli = StudentManagementCLI()
    cli.run()
