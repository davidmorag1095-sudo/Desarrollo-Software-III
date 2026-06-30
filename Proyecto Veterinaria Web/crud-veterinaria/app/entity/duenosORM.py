from sqlalchemy import Column, Integer, String

from app.config.database_conexion import Base


class DuenosORM(Base):
    __tablename__ = "duenos"

    id = Column(Integer, autoincrement=True, primary_key=True)
    nombre = Column(String(100), nullable=False)
    telefono = Column(String(20), nullable=False)
    email = Column(String(100), nullable=False)

    def __repr__(self):
        return f"{self.id} - {self.nombre} - {self.telefono} - {self.email}"

