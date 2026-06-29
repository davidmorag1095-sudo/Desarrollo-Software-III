from GestionBiblioteca.repository.libro_repository import LibroRepository
from GestionBiblioteca.repository.autor_repository import AutorRepository


class LibroService:
    def __init__(self):
        self.libro_repository = LibroRepository()
        self.autor_repository = AutorRepository()

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def registrar_libro(self, codigo, titulo, categoria, anio_publicacion, autor_id):
        codigo = codigo.strip()
        titulo = titulo.strip()
        categoria = categoria.strip()

        if codigo == "" or titulo == "":
            return "Error: el codigo y el titulo son obligatorios"

        libro_existente = self.libro_repository.buscar_por_codigo(codigo)
        if libro_existente:
            return "Error: ya existe un libro con ese codigo"

        autor = self.autor_repository.buscar_por_id(autor_id)
        if autor is None:
            return "Error: el autor indicado no existe"

        if anio_publicacion <= 0:
            return "Error: el anio de publicacion no es valido"

        self.libro_repository.registrar_libro(
            codigo,
            titulo,
            categoria,
            anio_publicacion,
            autor_id
        )

        return "Libro registrado correctamente"

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def consultar_libros(self):
        return self.libro_repository.consultar_libros()

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def buscar_libro(self, codigo):
        codigo = codigo.strip()

        if codigo == "":
            return None

        return self.libro_repository.buscar_por_codigo(codigo)

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def actualizar_libro(self, codigo, titulo, categoria, anio_publicacion, autor_id):
        codigo = codigo.strip()
        titulo = titulo.strip()
        categoria = categoria.strip()

        if codigo == "" or titulo == "":
            return "Error: el codigo y el titulo son obligatorios"

        libro = self.libro_repository.buscar_por_codigo(codigo)
        if libro is None:
            return "Error: no existe un libro con ese codigo"

        autor = self.autor_repository.buscar_por_id(autor_id)
        if autor is None:
            return "Error: el autor indicado no existe"

        if anio_publicacion <= 0:
            return "Error: el anio de publicacion no es valido"

        self.libro_repository.actualizar_libro(
            codigo,
            titulo,
            categoria,
            anio_publicacion,
            autor_id
        )

        return "Libro actualizado correctamente"

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def eliminar_libro(self, codigo):
        codigo = codigo.strip()

        libro = self.libro_repository.buscar_por_codigo(codigo)
        if libro is None:
            return "Error: no existe un libro con ese codigo"

        self.libro_repository.eliminar_libro(codigo)
        return "Libro eliminado correctamente"

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def libros_ordenados_por_titulo(self):
        return self.libro_repository.libros_ordenados_por_titulo()

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def libros_por_categoria(self, categoria):
        categoria = categoria.strip()

        if categoria == "":
            return []

        return self.libro_repository.libros_por_categoria(categoria)

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def libros_por_autor(self, nombre_autor):
        nombre_autor = nombre_autor.strip()

        if nombre_autor == "":
            return []

        autor = self.autor_repository.buscar_por_nombre(nombre_autor)
        if autor is None:
            return []

        return self.libro_repository.libros_por_autor(autor.id)
