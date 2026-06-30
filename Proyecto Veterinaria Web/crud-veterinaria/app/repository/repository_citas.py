from app.config.database_conexion import SessionLocal
from app.entity.citasORM import CitasORM


class RepositoryCitas:

    def __init__(self):
        self.db = SessionLocal()

    def save(self, codigo_mascota, fecha, hora, motivo, estado):
        cita = CitasORM(
            codigo_mascota=codigo_mascota,
            fecha=fecha,
            hora=hora,
            motivo=motivo,
            estado=estado
        )
        self.db.add(cita)
        self.db.commit()
        self.db.refresh(cita)
        return cita

    def get(self, id):
        return self.db.query(CitasORM).filter_by(id=id).first()

    def get_all(self):
        return self.db.query(CitasORM).all()

    def update(self, id, codigo_mascota, fecha, hora, motivo, estado):
        cita = self.get(id)
        if cita:
            cita.codigo_mascota = codigo_mascota
            cita.fecha = fecha
            cita.hora = hora
            cita.motivo = motivo
            cita.estado = estado
            self.db.commit()
            self.db.refresh(cita)
        return cita

    def delete(self, id):
        cita = self.get(id)
        if cita:
            self.db.delete(cita)
            self.db.commit()
        return cita

    def existe_horario(self, fecha, hora, id=None):
        consulta = self.db.query(CitasORM).filter_by(fecha=fecha, hora=hora)
        if id:
            consulta = consulta.filter(CitasORM.id != id)
        return consulta.first() is not None

    def count_by_estado(self):
        from sqlalchemy import func

        return self.db.query(
            CitasORM.estado,
            func.count(CitasORM.id)
        ).group_by(CitasORM.estado).all()

