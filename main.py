from services.school_system import SchoolSystem

def main():
    system = SchoolSystem()
    print("Student Course Registration System initialized.")
    system.load_data()
    print("System ready. Menu support will be added in later commits.")

if __name__ == "__main__":
    main()
