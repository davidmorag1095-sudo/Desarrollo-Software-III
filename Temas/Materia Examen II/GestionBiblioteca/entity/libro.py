from GestionBiblioteca.config.database import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class LibroORM(Base):
    __tablename__ = "libros"

    codigo = Column(String(20), primary_key=True)
    titulo = Column(String(100), nullable=False)
    categoria = Column(String(50))
    anio_publicacion = Column(Integer)
    autor_id = Column(Integer, ForeignKey("autores.id"))

    def __repr__(self):
        return f"Libro(codigo='{self.codigo}', titulo='{self.titulo}', categoria='{self.categoria}', anio_publicacion={self.anio_publicacion}, autor_id={self.autor_id})"
