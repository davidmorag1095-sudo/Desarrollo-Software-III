from config.database import Base
from sqlalchemy import Integer, Column, String, ForeignKey, Date


class PrestamoORM(Base):
    __tablename__ = "prestamos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    estudiante_id = Column(Integer, ForeignKey('estudiante.id'))
    equipo_codigo = Column(String(20), ForeignKey('equipos.codigo'))
    fecha_prestamo = Column(Date)
    fecha_devolucion = Column(Date)
    estado = Column(String(30))


    def __repr__(self):
        f" ID: {self.estudiante_id} | EstudianteID: {self.estudiante_id} | Codigo Equipo: {self.equipo_codigo} | Fecha Prestamo: {self.fecha_prestamo} | Fecha_devolucion: {self.fecha_devolucion} | Estado: {self.estado} "