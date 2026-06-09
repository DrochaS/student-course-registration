import os

class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.registrations = []

        if not os.path.exists('data'):
            os.makedirs('data')

    def load_data(self):
        print("Data loading is enabled in a later commit.")
        return False
