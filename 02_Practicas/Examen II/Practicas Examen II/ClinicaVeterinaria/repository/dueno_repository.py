from config.database import SessionLocal
from entity.duenos import DuenosORM

class DuenoRepository():
    def __init__(self):
        self.db = SessionLocal()

    def save(self,id, nombre, telefono, email):
        duenosORM = DuenosORM(id= id, nombre = nombre, telefono = telefono, email = email)
        self.db.add(duenosORM)
        self.db.commit()
        return duenosORM
#---------------------------------------------------------------------------------------------------------
    def get_all(self):
        return self.db.query(DuenosORM).all()
#---------------------------------------------------------------------------------------------------------
    #def serch_name(self, nombre):
        #return self.db.query(DuenosORM).filter_by(nombre = nombre).first()

    def serch_id(self, id):
        return self.db.query(DuenosORM).filter_by(id = id).first()
#---------------------------------------------------------------------------------------------------------
    def update(self, id, nombre, telefono, email):
        duenos = self.serch_id(id)

        if duenos:
            duenos.nombre = nombre
            duenos.telefono = telefono
            duenos.email = email
            self.db.commit()
        return duenos
#---------------------------------------------------------------------------------------------------------
    def delete(self, id):
        dueno = self.serch_id(id)

        if dueno:
            self.db.delete(dueno)
            self.db.commit()
        return dueno
#---------------------------------------------------------------------------------------------------------