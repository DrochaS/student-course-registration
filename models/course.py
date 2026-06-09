class Course:
    def __init__(self, course_id, course_name, trainer_name, capacity):
        self.course_id = course_id
        self.course_name = course_name
        self.trainer_name = trainer_name
        self.capacity = int(capacity)

    def __str__(self):
        return (f"Course ID:   {self.course_id}\n"
                f"Course Name: {self.course_name}\n"
                f"Trainer:     {self.trainer_name}\n"
                f"Capacity:    {self.capacity} students\n"
                f"{'-'*30}")