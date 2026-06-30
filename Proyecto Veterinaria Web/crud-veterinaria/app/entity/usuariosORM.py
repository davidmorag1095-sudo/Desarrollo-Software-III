from sqlalchemy import Column, Integer, String

from app.config.database_conexion import Base


class UsuariosORM(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, autoincrement=True, primary_key=True)
    usuario = Column(String(50), unique=True, nullable=False)
    clave = Column(String(100), nullable=False)

