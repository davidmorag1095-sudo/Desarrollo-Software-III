from sqlalchemy import Column, ForeignKey, Integer, String

from app.config.database_conexion import Base


class MascotasORM(Base):
    __tablename__ = "mascotas"

    codigo = Column(String(100), primary_key=True)
    nombre = Column(String(100), nullable=False)
    especie = Column(String(50), nullable=False)
    edad = Column(Integer, nullable=False)
    dueno_id = Column(Integer, ForeignKey("duenos.id"), nullable=False)

    def __repr__(self):
        return f"{self.codigo} - {self.nombre} - {self.especie} - {self.edad} - {self.dueno_id}"

