from ORM.app.repository.student_repository import StudentRepository

class StudentService:

    def __init__(self):
        self.repo = StudentRepository()

    def create_student(self, carnet, name, age):
        return self.repo.create(carnet, name, age)

    def get_student(self, carnet):
        return self.repo.get(carnet)

    def list_students(self):
        return self.repo.get_all()

    def update_student(self, carnet, name, age):
        return self.repo.update(carnet, name, age)

    def delete_student(self, carnet):
        return self.repo.delete(carnet)
