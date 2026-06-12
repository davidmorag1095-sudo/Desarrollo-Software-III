from app.service.student_service import StudentService

class StudentController:

    def __init__(self):
        self.service = StudentService()

    def create(self, carnet, name, age):
        student = self.service.create_student(carnet, name, age)
        print("Student created:", student)

    def get(self, carnet):
        student = self.service.get_student(carnet)
        print(student if student else "Student not found")

    def list(self):
        students = self.service.list_students()
        for s in students:
            print(s)

    def update(self, carnet, name, age):
        student = self.service.update_student(carnet, name, age)
        print("Student updated" if student else "Student not found")

    def delete(self, carnet):
        student = self.service.delete_student(carnet)
        print("Student deleted" if student else "Student not found")
