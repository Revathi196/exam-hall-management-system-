class Student:
    def __init__(self, name, student_id, hall):
        self.name = name
        self.student_id = student_id
        self.hall = hall

    def __str__(self):
        return f"{self.name} (ID: {self.student_id}) - {self.hall}"
