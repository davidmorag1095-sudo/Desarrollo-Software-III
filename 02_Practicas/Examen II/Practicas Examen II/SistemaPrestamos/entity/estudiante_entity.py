from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
class EstudianteORM(Base):
    __tablename__ = 'estudiante'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(100))
    carrera = Column(String(100))

def __repr__(self):
    return f"ID: {self.id}| Nombre: {self.nombre} | Correo: {self.correo} | Carrera: {self.carrera} | CategoriaID: {self.categoria_id}"