from ORM.app.config.database import SessionLocal
from ORM.app.entity.student import StudentORM

class StudentRepository:
    def __init__(self):
        self.db=SessionLocal()

    #creando un estudiante
    def create(self, carnet, name, age):
        #esta vinculado con el paquete
        student = StudentORM(carnet=carnet, name=name, age=age)
        #add el agregar de db
        self.db.add(student)
        #frozamos a la app a ingresar en la base de datos
        self.db.commit()
        return student
    #obtener un carnet
    def get(self, carnet):
        #consulta a la clase de estudiante
        return self.db.query(StudentORM).filter_by(carnet=carnet).first()
    #que traiga todos los estudiantes
    def get_all(self):
        return self.db.query(StudentORM).all()
    #actualizar
    def update(self, carnet, name, age):
        student=self.get(carnet)
        if student:
            student.name=name
            student.age=age
            self.db.commit()
        return student

    #eliminar
    def delete(self, carnet):
        student = self.get(carnet)
        if student:
            self.db.delete(student)
            self.db.commit()
        return student



