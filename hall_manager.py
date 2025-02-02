class HallManager:
    def __init__(self):
        self.students = []

    def assign_student(self, student):
        self.students.append(student)

    def get_all_students(self):
        return self.students
