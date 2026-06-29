from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class CategoriaORM(Base):
    __tablename__ = 'categoria'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)


    def __repr__(self):
        return f"Categoria: {self.nombre} | ID: {self.id}"