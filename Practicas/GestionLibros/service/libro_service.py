from model.libro import Libro
from repository.libro_repository import LibroRepository


class LibroService:
    def __init__(self):
        self.repository = LibroRepository()

    def registrar_libro(self, codigo, titulo, autor, categoria):
        codigo = codigo.strip()
        titulo = titulo.strip()
        autor = autor.strip()
        categoria = categoria.strip()

        # Validaciones principales
        if codigo == "" or titulo == "" or autor == "" or categoria == "":
            return "Error: todos los campos son obligatorios."

        if len(codigo) > 10:
            return "Error: el codigo no puede tener mas de 10 caracteres."

        if len(titulo) < 3:
            return "Error: el titulo debe tener minimo 3 caracteres."

        if len(categoria) < 3:
            return "Error: la categoria debe tener minimo 3 caracteres."

        if self.repository.buscar_por_codigo(codigo) is not None:
            return "Error: ya existe un libro con ese codigo."

        libro = Libro(
            codigo=codigo,
            titulo=titulo,
            autor=autor,
            categoria=categoria
        )

        self.repository.guardar(libro)

        return "Libro registrado correctamente."

    def listar_libros(self):
        return self.repository.listar()

    def buscar_libro_por_codigo(self, codigo):
        codigo = codigo.strip()

        if codigo == "":
            return None

        return self.repository.buscar_por_codigo(codigo)

    def buscar_libros_por_categoria(self, categoria):
        categoria = categoria.strip()

        if categoria == "":
            return "Error: la categoria es obligatoria."

        if len(categoria) < 3:
            return "Error: la categoria debe tener minimo 3 caracteres."

        return self.repository.buscar_por_categoria(categoria)

    def actualizar_libro(self, codigo, titulo, autor, categoria):
        codigo = codigo.strip()
        titulo = titulo.strip()
        autor = autor.strip()
        categoria = categoria.strip()

        # Validaciones principales
        if codigo == "" or titulo == "" or autor == "" or categoria == "":
            return "Error: todos los campos son obligatorios."

        if len(codigo) > 10:
            return "Error: el codigo no puede tener mas de 10 caracteres."

        if len(titulo) < 3:
            return "Error: el titulo debe tener minimo 3 caracteres."

        if len(categoria) < 3:
            return "Error: la categoria debe tener minimo 3 caracteres."

        libro_existente = self.repository.buscar_por_codigo(codigo)

        if libro_existente is None:
            return "Error: no existe un libro con ese codigo."

        libro_actualizado = Libro(
            codigo=codigo,
            titulo=titulo,
            autor=autor,
            categoria=categoria
        )

        actualizado = self.repository.actualizar(libro_actualizado)

        if actualizado:
            return "Libro actualizado correctamente."

        return "Error: no se pudo actualizar el libro."

    def eliminar_libro(self, codigo):
        codigo = codigo.strip()

        if codigo == "":
            return "Error: el codigo es obligatorio."

        libro = self.repository.buscar_por_codigo(codigo)

        if libro is None:
            return "Error: no existe un libro con ese codigo."

        eliminado = self.repository.eliminar(codigo)

        if eliminado:
            return "Libro eliminado correctamente."

        return "Error: no se pudo eliminar el libro."

