from config.database import SessionLocal, Base
from sqlalchemy import Integer, Column, String, ForeignKey

class EquipoORM(Base):
    __tablename__ = "equipos"
    codigo = Column(String(20),primary_key=True)
    nombre = Column(String(100), nullable=False)
    marca = Column(String(50))
    estado = Column(String(30))
    categoria_id = Column(Integer, ForeignKey("categorias.id"))

    def __repr__(self):
        return f"Codigo: {self.codigo}| Nombre: {self.nombre} | Marca: {self.marca} | Estado: {self.estado} | CategoriaID: {self.categoria_id}"
