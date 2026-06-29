from config.database import Base
from sqlalchemy import Column, Integer, String


class AutorORM(Base):
    __tablename__ = "autores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    nacionalidad = Column(String(50))

    def __repr__(self):
        return f"Autor(id={self.id}, nombre='{self.nombre}', nacionalidad='{self.nacionalidad}')"
