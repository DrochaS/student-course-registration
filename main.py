from services.school_system import SchoolSystem

def main():
    system = SchoolSystem()
    # Auto load database files at startup
    system.load_data()

    while True:
        print("\n===== Student Course Registration System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Add Course")
        print("5. View Courses")
        print("6. Register Student to Course")
        print("7. View Students in a Course")
        print("8. View Courses for a Student")
        print("9. Save Data")
        print("10. Load Data")
        print("0. Exit")
        print("==============================================")
        
        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                sid = input("Enter Student ID: ").strip()
                name = input("Enter Full Name: ").strip()
                email = input("Enter Email Address: ").strip()
                phone = input("Enter Phone Number: ").strip()
                system.add_student(sid, name, email, phone)

            elif choice == "2":
                system.view_students()

            elif choice == "3":
                term = input("Enter Student ID or Name to search: ").strip()
                system.search_student(term)

            elif choice == "4":
                cid = input("Enter Course ID: ").strip()
                cname = input("Enter Course Name: ").strip()
                trainer = input("Enter Trainer Name: ").strip()
                capacity = input("Enter Course Max Capacity: ").strip()
                system.add_course(cid, cname, trainer, capacity)

            elif choice == "5":
                system.view_courses()

            elif choice == "6":
                sid = input("Enter Student ID: ").strip()
                cid = input("Enter Course ID: ").strip()
                system.register_student(sid, cid)

            elif choice == "7":
                cid = input("Enter Course ID: ").strip()
                system.view_students_in_course(cid)

            elif choice == "8":
                sid = input("Enter Student ID: ").strip()
                system.view_courses_for_student(sid)

            elif choice == "9":
                system.save_data()

            elif choice == "10":
                system.load_data()

            elif choice == "0":
                print("Saving all registration modifications before quitting...")
                system.save_data()
                print("Goodbye!")
                break
            else:
                print("Invalid operational request. Select an options from 0-10.")

        except Exception as error:
            print(f"An unexpected loop exception was mitigated cleanly: {error}")

if __name__ == "__main__":
    main()
