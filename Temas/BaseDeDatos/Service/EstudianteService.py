from Temas.BaseDeDatos.Repository.estudiante_repository import EstudianteRepository
from Temas.BaseDeDatos.Model.estudiante import Estudiante

class EstudianteService:
    def __init__(self, repository: EstudianteRepository):
        self.repository = EstudianteRepository()

    def registrar_estudiante(self, nombre, correo, carrera):
        """
        Valída y registra un estudiante
        :param nombre: nombre completo del estudiante
        :param correo: correo del estudiante
        :param carrera: carrera en la que esta el estudiante

        :return:
        Mensaje con el resultado de la operación
        """

        #Strip elimina los espacios en blanco al inicio y al final
        nombre = nombre.strip()
        correo = correo.strip()
        carrera = carrera.strip()

        #Validacion: ningún campo debe estar vacío
        if nombre == "" or correo == "" or carrera == "":
            return "Error: todos los campos deben estar"

        #Validacion básica del correo
        if "@" not in correo or "." not in correo:
            return "Error: Formato del correo inválido"

        #Validación: El correo no debe repetirse
        if self.repository.existe_correo(correo):
            return "Error: El correo ya existe un estudiante con ese correo"

        #Se crea el objeto Estudiante
        estudiante = Estudiante(
            nombre=nombre,
            correo=correo,
            carrera=carrera)
        #Se envía el objeto al repositorio para guardarlo
        #En la base de datos
        self.repository.registrar(estudiante)
        return "Estudiante registrado correctamente"

    def consultar_estudiante(self):
        """Consultar todos los estudiantes
        return
        lista de estudiantes"""

        return self.repository.consultar_todos()

    def buscar_estudiante(self, id_estudiante):
        """Buscar un estudiantepor ID
        :args
        id_estudiante:  ID del estudiante
        return
        lista de estudiantes"""

        return self.repository.buscar_por_id(id_estudiante)

    def actualiar_estudiante(self, id_estudiante, nombre, correo, carrera):
        """Actualiza un estudiante despúes de validar los datos"""

        nombre = nombre.strip()
        correo = correo.strip()
        carrera = carrera.strip()

        if "@" not in correo or "." not in correo:
            return "Error: Formato del correo invalido"

        #Antes de actualizar, se verifica que el estudiante exista
        estudiante_existente = self.repository.buscar_por_id(id_estudiante)

        if estudiante_existente is None:
            return "Error: El estudiante no existe con ese ID: ", id_estudiante

        #Se crea un objeto estudiante con nuevos datos
        estudiante_actualizado = Estudiante(
            id_estudiante=id_estudiante,
            nombre=nombre,
            correo=correo,
            carrera=carrera)

        actualizado = self.repository.actualizar(estudiante_actualizado)

        if actualizado:
            return "Estudiante actualizado correctamente"
        return "Error: No se pudo actualizar el estudiante"

    def eliminar_estudiante(self, id_estudiante):
        """Elimina un estudiante por ID.
        :param id_estudiante: ID del estudiante
        eliminar
        :return:
        Mensaje con el resultado
        """
        estudiante_eliminado=self.repository.eliminar(id_estudiante)

        if estudiante_eliminado:
            return "Estudiante eliminado correctamente"
        return "Error: No se pudo eliminar el estudiante"
