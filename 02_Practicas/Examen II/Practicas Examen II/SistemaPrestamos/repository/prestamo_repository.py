from config.database import SessionLocal
from entity.equipo_entity import EquipoORM
from entity.prestamo_entity import PrestamoORM

class PrestamoRepository():
    def __init__(self):
        self.db = SessionLocal()

    def save(self,id, estudiante_id, equipo_codigo, fecha_prestamo, fecha_devolucion, estado):
        prestamo = EquipoORM(id = id, estudiante_id = estudiante_id, equipo_codigo = equipo_codigo, fecha_prestamo = fecha_prestamo,
                            fecha_devolucion = fecha_devolucion, estado = estado)
        self.db.add(prestamo)
        self.db.commit()
#---------------------------------------------------------------------------------------------------------
    def get_all(self):
        return self.db.query(EquipoORM).all()
#---------------------------------------------------------------------------------------------------------
    def serch_by_id(self,id):
        return self.db.query(EquipoORM).filter_by(id = id).first()
#---------------------------------------------------------------------------------------------------------
    def update(self,id, estudiante_id, equipo_codigo, fecha_prestamo, fecha_devolucion, estado):
        prestamo = self.serch_by_id(id)

        if prestamo:
            prestamo.estudiante_id = estudiante_id
            prestamo.equipo_codigo = equipo_codigo
            prestamo.fecha_prestamo = fecha_prestamo
            prestamo.fecha_devolucion = fecha_devolucion
            prestamo.estado = estado
            self.db.commit()
        return prestamo
#---------------------------------------------------------------------------------------------------------
    def delete(self, id):
        prestamo = self.serch_by_id(id)

        if prestamo:
            self.db.delete(prestamo)
            self.db.commit()

        return prestamo