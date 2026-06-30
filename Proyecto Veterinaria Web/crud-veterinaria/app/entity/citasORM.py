from sqlalchemy import Column, ForeignKey, Integer, String

from app.config.database_conexion import Base


class CitasORM(Base):
    __tablename__ = "citas"

    id = Column(Integer, autoincrement=True, primary_key=True)
    codigo_mascota = Column(String(100), ForeignKey("mascotas.codigo"), nullable=False)
    fecha = Column(String(10), nullable=False)
    hora = Column(String(5), nullable=False)
    motivo = Column(String(150), nullable=False)
    estado = Column(String(20), nullable=False)

    def __repr__(self):
        return f"{self.id} - {self.codigo_mascota} - {self.fecha} - {self.hora} - {self.estado}"

