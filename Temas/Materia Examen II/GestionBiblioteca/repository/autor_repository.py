from GestionBiblioteca.config.database import SessionLocal
from GestionBiblioteca.entity.autor import AutorORM
from GestionBiblioteca.entity.libro import LibroORM


class AutorRepository:
    def __init__(self):
        self.db = SessionLocal()

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def registrar_autor(self, nombre, nacionalidad):
        autor = AutorORM(nombre=nombre, nacionalidad=nacionalidad)
        self.db.add(autor)
        self.db.commit()
        return autor

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def consultar_todos(self):
        return self.db.query(AutorORM).all()

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def buscar_por_id(self, id_autor):
        return self.db.query(AutorORM).filter_by(id=id_autor).first()

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def buscar_por_nombre(self, nombre):
        return self.db.query(AutorORM).filter_by(nombre=nombre).first()

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def actualizar(self, id_autor, nombre, nacionalidad):
        autor = self.buscar_por_id(id_autor)

        if autor:
            autor.nombre = nombre
            autor.nacionalidad = nacionalidad
            self.db.commit()

        return autor

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def eliminar(self, id_autor):
        autor = self.buscar_por_id(id_autor)

        if autor:
            self.db.delete(autor)
            self.db.commit()

        return autor

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def tiene_libros(self, id_autor):
        libro = self.db.query(LibroORM).filter_by(autor_id=id_autor).first()
        return libro is not None

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def autores_por_nacionalidad(self, nacionalidad):
        return self.db.query(AutorORM).filter_by(nacionalidad=nacionalidad).all()
