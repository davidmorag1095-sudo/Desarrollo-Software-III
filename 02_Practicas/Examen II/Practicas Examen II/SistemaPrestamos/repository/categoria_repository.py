from config.database import SessionLocal
from entity.categoria_entity import CategoriaORM

class CategoriaRepository:
    def __init__(self):
        self.db = SessionLocal()

    def save(self, id, nombre):
        categoria = CategoriaORM(id=id, nombre=nombre)
        self.db.add(categoria)
        self.db.commit()

#---------------------------------------------------------------------------------------------------------
    def get_all(self):
        return self.db.query(CategoriaORM).all()

#---------------------------------------------------------------------------------------------------------
    def serch_by_id(self, id):
        return self.db.query(CategoriaORM).filter_by(id=id).first()

#---------------------------------------------------------------------------------------------------------
    def update(self, id, nombre):
        categoria = self.serch_by_id(id)

        if categoria:
            categoria.nombre = nombre
            self.db.commit()

        return categoria
#---------------------------------------------------------------------------------------------------------
    def delete(self, id):
        categoria = self.serch_by_id(id)

        if categoria:
            self.db.delete(categoria)
            self.db.commit()

        return categoria
#---------------------------------------------------------------------------------------------------------
