from GestionBiblioteca.repository.autor_repository import AutorRepository


class AutorService:
    def __init__(self):
        self.repository = AutorRepository()

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def registrar_autor(self, nombre, nacionalidad):
        nombre = nombre.strip()
        nacionalidad = nacionalidad.strip()

        if nombre == "":
            return "Error: el nombre del autor es obligatorio"

        self.repository.registrar_autor(nombre, nacionalidad)
        return "Autor registrado correctamente"

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def consultar_autores(self):
        return self.repository.consultar_todos()

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def buscar_autor(self, id_autor):
        return self.repository.buscar_por_id(id_autor)

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def buscar_autor_por_nombre(self, nombre):
        nombre = nombre.strip()

        if nombre == "":
            return None

        return self.repository.buscar_por_nombre(nombre)

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def actualizar_autor(self, id_autor, nombre, nacionalidad):
        nombre = nombre.strip()
        nacionalidad = nacionalidad.strip()

        if nombre == "":
            return "Error: el nombre del autor es obligatorio"

        autor = self.repository.buscar_por_id(id_autor)
        if autor is None:
            return "Error: no existe un autor con ese ID"

        self.repository.actualizar(id_autor, nombre, nacionalidad)
        return "Autor actualizado correctamente"

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def eliminar_autor(self, id_autor):
        autor = self.repository.buscar_por_id(id_autor)
        if autor is None:
            return "Error: no existe un autor con ese ID"

        if self.repository.tiene_libros(id_autor):
            return "Error: no se puede eliminar un autor con libros registrados"

        self.repository.eliminar(id_autor)
        return "Autor eliminado correctamente"

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def autores_por_nacionalidad(self, nacionalidad):
        nacionalidad = nacionalidad.strip()

        if nacionalidad == "":
            return []

        return self.repository.autores_por_nacionalidad(nacionalidad)
