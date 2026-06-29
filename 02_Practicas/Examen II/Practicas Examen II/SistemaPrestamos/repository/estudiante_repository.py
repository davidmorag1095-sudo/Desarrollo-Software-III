from config.database import SessionLocal
from entity.estudiante_entity import EstudianteORM

class EstudianteRepository():
    def __init__(self):
        self.db = SessionLocal()

    def save(self, id, nombre, correo, carrera):
        estudiante = EstudianteORM(id = id, nombre = nombre, correo = correo, carrera = carrera)
        self.db.add(estudiante)
        self.db.commit()
#---------------------------------------------------------------------------------------------------------
    def get_all(self):
        return self.db.query(EstudianteORM).all()
#---------------------------------------------------------------------------------------------------------
    def serch_by_id(self,id):
        return self.db.query(EstudianteORM).filter_by (id = id).first()
#---------------------------------------------------------------------------------------------------------
    def update(self, id, nombre, correo, carrera):
        estudiante = self.serch_by_id(id)

        if estudiante:
            estudiante.nombre = nombre
            estudiante.correo = correo
            estudiante.carrera = carrera
            self.db.commit()
        return estudiante
#---------------------------------------------------------------------------------------------------------
    def delete(self, id):
        estudiante = self.serch_by_id(id)

        if estudiante:
            self.db.delete(estudiante)
            self.db.commit()

        return estudiante
#---------------------------------------------------------------------------------------------------------