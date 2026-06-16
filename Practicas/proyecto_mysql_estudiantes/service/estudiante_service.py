"""
Archivo: estudiante_service.py

Responsabilidad:
Esta capa contiene las reglas de negocio y validaciones.

El service usa al repository para guardar, consultar, actualizar o eliminar,
pero antes valida que los datos sean correctos.
"""

from model.estudiante import Estudiante
from repository.estudiante_repository import EstudianteRepository


class EstudianteService:
    """
    Servicio que contiene la lógica de negocio de estudiantes.
    """

    def __init__(self):
        """
        Constructor del servicio.

        Se crea una instancia del repositorio para poder acceder a la base de datos.
        """

        self.repository = EstudianteRepository()

    def registrar_estudiante(self, nombre, correo, carrera):
        """
        Valida y registra un estudiante.

        Args:
            nombre: nombre completo.
            correo: correo electrónico.
            carrera: carrera del estudiante.

        Returns:
            Mensaje con el resultado de la operación.
        """

        # strip elimina espacios en blanco al inicio y al final.
        nombre = nombre.strip()
        correo = correo.strip()
        carrera = carrera.strip()

        # Validación: ningún campo debe quedar vacío.
        if nombre == "" or correo == "" or carrera == "":
            return "Error: todos los campos son obligatorios."

        # Validación básica del correo.
        if "@" not in correo or "." not in correo:
            return "Error: el correo no tiene un formato válido."

        # Validación: el correo no debe repetirse.
        if self.repository.existe_correo(correo):
            return "Error: ya existe un estudiante con ese correo."

        # Se crea el objeto Estudiante.
        estudiante = Estudiante(
            nombre=nombre,
            correo=correo,
            carrera=carrera
        )

        # Se envía el objeto al repositorio para guardarlo en MySQL.
        self.repository.registrar(estudiante)

        return "Estudiante registrado correctamente."

    def consultar_estudiantes(self):
        """
        Consulta todos los estudiantes.

        Returns:
            Lista de estudiantes.
        """

        return self.repository.consultar_todos()

    def buscar_estudiante(self, id_estudiante):
        """
        Busca un estudiante por ID.

        Args:
            id_estudiante: ID del estudiante.

        Returns:
            Objeto Estudiante o None.
        """

        return self.repository.buscar_por_id(id_estudiante)

    def actualizar_estudiante(self, id_estudiante, nombre, correo, carrera):
        """
        Actualiza un estudiante después de validar los datos.

        Args:
            id_estudiante: ID del estudiante.
            nombre: nuevo nombre.
            correo: nuevo correo.
            carrera: nueva carrera.

        Returns:
            Mensaje con el resultado.
        """

        nombre = nombre.strip()
        correo = correo.strip()
        carrera = carrera.strip()

        if nombre == "" or correo == "" or carrera == "":
            return "Error: todos los campos son obligatorios."

        if "@" not in correo or "." not in correo:
            return "Error: el correo no tiene un formato válido."

        # Antes de actualizar, se verifica que el estudiante exista.
        estudiante_existente = self.repository.buscar_por_id(id_estudiante)

        if estudiante_existente is None:
            return "Error: no existe un estudiante con ese ID."

        # Se crea un objeto con los nuevos datos.
        estudiante_actualizado = Estudiante(
            id_estudiante=id_estudiante,
            nombre=nombre,
            correo=correo,
            carrera=carrera
        )

        actualizado = self.repository.actualizar(estudiante_actualizado)

        if actualizado:
            return "Estudiante actualizado correctamente."

        return "Error: no se pudo actualizar el estudiante."

    def eliminar_estudiante(self, id_estudiante):
        """
        Elimina un estudiante por ID.

        Args:
            id_estudiante: ID del estudiante.

        Returns:
            Mensaje con el resultado.
        """

        estudiante = self.repository.buscar_por_id(id_estudiante)

        if estudiante is None:
            return "Error: no existe un estudiante con ese ID."

        eliminado = self.repository.eliminar(id_estudiante)

        if eliminado:
            return "Estudiante eliminado correctamente."

        return "Error: no se pudo eliminar el estudiante."
