from app.config.database import SessionLocal
from app.entity.student import StudentORM

class StudentRepository:

    def __init__(self):
        self.db = SessionLocal()

    def create(self, carnet, name, age):
        student = StudentORM(carnet=carnet, name=name, age=age)
        self.db.add(student)
        self.db.commit()
        return student

    def get(self, carnet):
        return self.db.query(StudentORM).filter_by(carnet=carnet).first()

    def get_all(self):
        return self.db.query(StudentORM).all()

    def update(self, carnet, name, age):
        student = self.get(carnet)
        if student:
            student.name = name
            student.age = age
            self.db.commit()
        return student

    def delete(self, carnet):
        student = self.get(carnet)
        if student:
            self.db.delete(student)
            self.db.commit()
        return student
