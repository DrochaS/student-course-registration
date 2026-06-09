import os
from models.student import Student
from models.course import Course

class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.registrations = []

        if not os.path.exists('data'):
            os.makedirs('data')

    # VALIDATION & UTILITIES 
    def _find_student_by_id(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None

    def _find_course_by_id(self, course_id):
        for c in self.courses:
            if c.course_id == course_id:
                return c
        return None

    def _count_course_enrollment(self, course_id):
        count = 0
        for reg in self.registrations:
            if reg[1] == course_id:
                count += 1
        return count

    # CORE FEATURES 
    def add_student(self, student_id, name, email, phone):
        # Validations
        if not student_id or not name or not phone:
            print("Error: Student ID, Name, and Phone cannot be empty.")
            return False
        if "@" not in email:
            print("Error: Invalid Email format missing '@'.")
            return False
        if self._find_student_by_id(student_id):
            print(f"Error: A student with ID {student_id} already exists.")
            return False

        new_student = Student(student_id, name, email, phone)
        self.students.append(new_student)
        print(f"Student {name} added successfully.")
        return True

    def add_course(self, course_id, course_name, trainer_name, capacity_str):
        # Validations
        if not course_id or not course_name:
            print("Error: Course ID and Course Name cannot be empty.")
            return False
        try:
            capacity = int(capacity_str)
            if capacity <= 0:
                print("Error: Capacity must be greater than 0.")
                return False
        except ValueError:
            print("Error: Capacity must be a whole number.")
            return False

        if self._find_course_by_id(course_id):
            print(f"Error: A course with ID {course_id} already exists.")
            return False

        new_course = Course(course_id, course_name, trainer_name, capacity)
        self.courses.append(new_course)
        print(f"Course '{course_name}' added successfully.")
        return True

    def register_student(self, student_id, course_id):
        student = self._find_student_by_id(student_id)
        course = self._find_course_by_id(course_id)

        if not student:
            print("Error: Student not found.")
            return False
        if not course:
            print("Error: Course not found.")
            return False

        # Check Duplicate registration
        if [student_id, course_id] in self.registrations:
            print(f"{student.name} is already registered for this course.")
            return False

        # Check Course capacity
        current_enrollment = self._count_course_enrollment(course_id)
        if current_enrollment >= course.capacity:
            print("Registration failed. This course is already full.")
            return False

        self.registrations.append([student_id, course_id])
        print(f"Student {student.name} successfully registered for {course.course_name}.")
        return True

    def view_students(self):
        if not self.students:
            print("No students recorded in the system.")
            return
        print("\n--- List of Students ---")
        for s in self.students:
            print(s)

    def view_courses(self):
        if not self.courses:
            print("No courses recorded in the system.")
            return
        print("\n--- List of Courses ---")
        for c in self.courses:
            print(c)

    def search_student(self, search_term):
        found = False
        print(f"\n--- Search results for '{search_term}' ---")
        for s in self.students:
            if search_term.lower() in s.student_id.lower() or search_term.lower() in s.name.lower():
                print(s)
                found = True
        if not found:
            print("No matching student profiles located.")

    def view_students_in_course(self, course_id):
        course = self._find_course_by_id(course_id)
        if not course:
            print("Error: Course not found.")
            return

        print(f"\n--- Students Registered in {course.course_name} ({course_id}) ---")
        found = False
        for reg in self.registrations:
            if reg[1] == course_id:
                student = self._find_student_by_id(reg[0])
                if student:
                    print(f"- {student.name} (ID: {student.student_id})")
                    found = True
        if not found:
            print("No students are currently enrolled in this course.")

    def view_courses_for_student(self, student_id):
        student = self._find_student_by_id(student_id)
        if not student:
            print("Error: Student not found.")
            return

        print(f"\n--- Courses registered by {student.name} ({student_id}) ---")
        found = False
        for reg in self.registrations:
            if reg[0] == student_id:
                course = self._find_course_by_id(reg[1])
                if course:
                    print(f"- {course.course_name} (ID: {course.course_id})")
                    found = True
        if not found:
            print("This student is not enrolled in any courses.")

    #  FILE HANDLING (.TXT) 
    def save_data(self):
        try:
            # Save Students
            with open("data/students.txt", "w") as f:
                for s in self.students:
                    f.write(f"{s.student_id}|{s.name}|{s.email}|{s.phone_number}\n")

            # Save Courses
            with open("data/courses.txt", "w") as f:
                for c in self.courses:
                    f.write(f"{c.course_id}|{c.course_name}|{c.trainer_name}|{c.capacity}\n")

            # Save Registrations
            with open("data/registrations.txt", "w") as f:
                for reg in self.registrations:
                    f.write(f"{reg[0]}|{reg[1]}\n")

            print("Data saved successfully to flat text files.")
        except Exception as e:
            print(f"Critical error saving data: {e}")

    def load_data(self):
        try:
            # Clear running runtime lists to avoid duplicating lines if re-loaded
            self.students.clear()
            self.courses.clear()
            self.registrations.clear()

            # Load Students
            if os.path.exists("data/students.txt"):
                with open("data/students.txt", "r") as f:
                    for line in f:
                        line = line.strip()
                        if line:
                            sid, name, email, phone = line.split("|")
                            self.students.append(Student(sid, name, email, phone))

            # Load Courses
            if os.path.exists("data/courses.txt"):
                with open("data/courses.txt", "r") as f:
                    for line in f:
                        line = line.strip()
                        if line:
                            cid, cname, tname, cap = line.split("|")
                            self.courses.append(Course(cid, cname, tname, int(cap)))

            # Load Registrations
            if os.path.exists("data/registrations.txt"):
                with open("data/registrations.txt", "r") as f:
                    for line in f:
                        line = line.strip()
                        if line:
                            sid, cid = line.split("|")
                            self.registrations.append([sid, cid])

            print("Data loaded successfully from flat text files.")
        except Exception as e:
            print(f"Data initialization alert: {e} (Starting clean system data state)")
