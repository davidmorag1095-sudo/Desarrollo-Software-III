from app.config.database_conexion import SessionLocal
from app.entity.duenosORM import DuenosORM


class RepositoryDuenos:

    def __init__(self):
        self.db = SessionLocal()

    def save(self, nombre, telefono, email):
        dueno = DuenosORM(nombre=nombre, telefono=telefono, email=email)
        self.db.add(dueno)
        self.db.commit()
        self.db.refresh(dueno)
        return dueno

    def get(self, id):
        return self.db.query(DuenosORM).filter_by(id=id).first()

    def get_all(self):
        return self.db.query(DuenosORM).all()

    def search_name(self, nombre):
        return self.db.query(DuenosORM).filter(DuenosORM.nombre.like(f"%{nombre}%")).all()

    def update(self, id, nombre, telefono, email):
        dueno = self.get(id)
        if dueno:
            dueno.nombre = nombre
            dueno.telefono = telefono
            dueno.email = email
            self.db.commit()
            self.db.refresh(dueno)
        return dueno

    def delete(self, id):
        dueno = self.get(id)
        if dueno:
            self.db.delete(dueno)
            self.db.commit()
        return dueno

