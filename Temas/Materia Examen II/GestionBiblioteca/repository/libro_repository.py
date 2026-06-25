from GestionBiblioteca.config.database import SessionLocal
from GestionBiblioteca.entity.libro import LibroORM


class LibroRepository:
    def __init__(self):
        self.db = SessionLocal()

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def registrar_libro(self, codigo, titulo, categoria, anio_publicacion, autor_id):
        libro = LibroORM(
            codigo=codigo,
            titulo=titulo,
            categoria=categoria,
            anio_publicacion=anio_publicacion,
            autor_id=autor_id
        )
        self.db.add(libro)
        self.db.commit()

        return libro

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def consultar_libros(self):
        return self.db.query(LibroORM).all()

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def buscar_por_codigo(self, codigo):
        return self.db.query(LibroORM).filter_by(codigo=codigo).first()

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def actualizar_libro(self, codigo, titulo, categoria, anio_publicacion, autor_id):
        libro = self.buscar_por_codigo(codigo)

        if libro:
            libro.titulo = titulo
            libro.categoria = categoria
            libro.anio_publicacion = anio_publicacion
            libro.autor_id = autor_id
            self.db.commit()

        return libro

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def eliminar_libro(self, codigo):
        libro = self.buscar_por_codigo(codigo)

        if libro:
            self.db.delete(libro)
            self.db.commit()

        return libro

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def libros_ordenados_por_titulo(self):
        return self.db.query(LibroORM).order_by(LibroORM.titulo).all()

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def libros_por_categoria(self, categoria):
        return self.db.query(LibroORM).filter_by(categoria=categoria).all()

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def libros_por_autor(self, autor_id):
        return self.db.query(LibroORM).filter_by(autor_id=autor_id).all()
