from config.database import SessionLocal
from entity.equipo_entity import EquipoORM

class EquipoRepository():
    def __init__(self):
        self.db = SessionLocal()

    def save_team(self, codigo, nombre, marca, estado, categoria_id):
        equipo = EquipoORM(codigo = codigo, nombre = nombre, marca = marca, estado = estado, categoria_id = categoria_id)
        self.db.add(equipo)
        self.db.commit()
#---------------------------------------------------------------------------------------------------------
    def get_all(self):
        return self.db.query(EquipoORM).all()
#---------------------------------------------------------------------------------------------------------
    def serch_by_codigo(self, codigo):
        return self.db.query(EquipoORM).filter_by(codigo = codigo).first()
#---------------------------------------------------------------------------------------------------------
    def update(self, codigo, nombre, marca, estado, categoria_id):
        equipo = self.serch_by_codigo(codigo)

        if equipo:
            equipo.codigo = codigo
            equipo.nombre = nombre
            equipo.marca = marca
            equipo.estado = estado
            equipo.categoria_id = categoria_id
            self.db.commit()
        return equipo
#---------------------------------------------------------------------------------------------------------
    def delete(self, codigo):
        equipo = self.serch_by_codigo(codigo)

        if equipo:
            self.db.delete(equipo)
            self.db.commit()

        return equipo
#---------------------------------------------------------------------------------------------------------