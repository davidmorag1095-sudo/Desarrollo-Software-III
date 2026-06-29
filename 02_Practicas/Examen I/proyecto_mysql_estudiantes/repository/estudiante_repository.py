"""
Archivo: estudiante_repository.py

Responsabilidad:
Esta capa se encarga de comunicarse directamente con la base de datos.

Aquí se escriben las consultas SQL:
- INSERT
- SELECT
- UPDATE
- DELETE

El repository no debe pedir datos por teclado ni mostrar menús.
Solo debe ejecutar operaciones contra la base de datos.
"""

from database.conexion import obtener_conexion
from model.estudiante import Estudiante


class EstudianteRepository:
    """
    Repositorio encargado de administrar los estudiantes en MySQL.
    """

    def registrar(self, estudiante):
        """
        Registra un estudiante en la base de datos.

        Args:
            estudiante: objeto de tipo Estudiante.

        Returns:
            True si el registro fue exitoso.
        """

        # Se obtiene una conexión con la base de datos.
        conexion = obtener_conexion()

        # El cursor permite ejecutar instrucciones SQL.
        cursor = conexion.cursor()

        # Consulta SQL parametrizada.
        # Se usa %s para evitar concatenar datos directamente en el SQL.
        sql = """
            INSERT INTO estudiantes (nombre, correo, carrera)
            VALUES (%s, %s, %s)
        """

        # Tupla con los valores que reemplazarán los %s de la consulta.
        valores = (estudiante.nombre, estudiante.correo, estudiante.carrera)

        # Ejecuta la consulta con sus valores.
        cursor.execute(sql, valores)

        # Confirma los cambios en la base de datos.
        conexion.commit()

        # Se cierran cursor y conexión para liberar recursos.
        cursor.close()
        conexion.close()

        return True

    def consultar_todos(self):
        """
        Consulta todos los estudiantes registrados.

        Returns:
            Lista de objetos Estudiante.
        """

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        # Consulta para obtener todos los estudiantes.
        cursor.execute("SELECT id, nombre, correo, carrera FROM estudiantes")

        # fetchall obtiene todos los registros encontrados.
        registros = cursor.fetchall()

        # Lista donde se almacenarán los objetos Estudiante.
        estudiantes = []

        # Se recorre cada registro devuelto por la base de datos.
        for registro in registros:
            # Cada registro es una tupla con el orden:
            # id, nombre, correo, carrera
            estudiante = Estudiante(
                id_estudiante=registro[0],
                nombre=registro[1],
                correo=registro[2],
                carrera=registro[3]
            )

            # Se agrega el objeto Estudiante a la lista.
            estudiantes.append(estudiante)

        cursor.close()
        conexion.close()

        return estudiantes

    def buscar_por_id(self, id_estudiante):
        """
        Busca un estudiante por su ID.

        Args:
            id_estudiante: ID del estudiante.

        Returns:
            Objeto Estudiante si existe, o None si no se encuentra.
        """

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        # Consulta con WHERE para filtrar por ID.
        sql = "SELECT id, nombre, correo, carrera FROM estudiantes WHERE id = %s"

        # Aunque sea un solo dato, debe enviarse como tupla.
        cursor.execute(sql, (id_estudiante,))

        # fetchone obtiene un solo registro.
        registro = cursor.fetchone()

        cursor.close()
        conexion.close()

        # Si no se encontró ningún estudiante, registro será None.
        if registro is None:
            return None

        # Si se encontró, se convierte en un objeto Estudiante.
        return Estudiante(
            id_estudiante=registro[0],
            nombre=registro[1],
            correo=registro[2],
            carrera=registro[3]
        )

    def actualizar(self, estudiante):
        """
        Actualiza los datos de un estudiante existente.

        Args:
            estudiante: objeto Estudiante con el ID y los nuevos datos.

        Returns:
            True si se actualizó al menos un registro, False en caso contrario.
        """

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            UPDATE estudiantes
            SET nombre = %s,
                correo = %s,
                carrera = %s
            WHERE id = %s
        """

        valores = (
            estudiante.nombre,
            estudiante.correo,
            estudiante.carrera,
            estudiante.id_estudiante
        )

        cursor.execute(sql, valores)
        conexion.commit()

        # rowcount indica cuántas filas fueron afectadas por la consulta.
        filas_afectadas = cursor.rowcount

        cursor.close()
        conexion.close()

        return filas_afectadas > 0

    def eliminar(self, id_estudiante):
        """
        Elimina un estudiante por su ID.

        Args:
            id_estudiante: ID del estudiante que se desea eliminar.

        Returns:
            True si se eliminó al menos un registro, False en caso contrario.
        """

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = "DELETE FROM estudiantes WHERE id = %s"

        cursor.execute(sql, (id_estudiante,))
        conexion.commit()

        filas_afectadas = cursor.rowcount

        cursor.close()
        conexion.close()

        return filas_afectadas > 0

    def existe_correo(self, correo):
        """
        Verifica si ya existe un estudiante con el correo indicado.

        Args:
            correo: correo que se desea validar.

        Returns:
            True si el correo ya existe, False si no existe.
        """

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = "SELECT id FROM estudiantes WHERE correo = %s"

        cursor.execute(sql, (correo,))

        registro = cursor.fetchone()

        cursor.close()
        conexion.close()

        return registro is not None
