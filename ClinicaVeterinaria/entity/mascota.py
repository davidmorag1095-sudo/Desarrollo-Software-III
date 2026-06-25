from sqlalchemy import Column, Integer, String, column, ForeignKey

from config.database import Base

class MascotaORM(Base):
    __tablename__ = 'mascotas'
    codigo = Column(String(20), primary_key=True)
    nombre = Column(String(100), nullable =False)
    especie = Column(String(100))
    edad = Column(Integer)
    dueno_id = Column(Integer, ForeignKey('duenos.id'))

    def __repr__(self):
        return f"Codigo: {self.codigo} Nombre: {self.nombre} Especie: {self.especie} Edad: {self.edad} IdDueño: {self.dueno_id}"