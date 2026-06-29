"""
Esta capa se encarga de comunicarse con la base de datos
Acá se realizan las consultas SQL:
INSERT
SELECT
UPDATE
DELETE

Aca no se piden datos ni se muestran menus
"""

from Temas.BaseDeDatos.Model.estudiante import Estudiante
from Temas.BaseDeDatos.database.conexion import obtener_conexion


class EstudianteRepository:
    def registrar(self, estudiante):
        """
        Registra un estudiante en la base de datos

        :param estudiante: Objeto de tipo estudiante
        :return: un boolean indicando verdadero
        si el registro es exitoso
        """

        # Se obtiene la conexion a la base de datos
        conexion = obtener_conexion()

        # El cursor permite ejecutar las instrucciones SQL
        cursor = conexion.cursor()

        # Consulta SQLO parametrizada
        # Se usa % para evitar concatenar
        # datos(nombres de variables) en SQL

        sql = """
            INSERT INTO estudiantes (nombre, correo, carrera)
             VALUES (%s, %s, %s)
        """

        # Tupla con los valores que remplazarán
        # los %s en la consulta
        valores = (estudiante.nombre, estudiante.correo, estudiante.carrera)

        # Ejecuta la consulta con sus valores
        cursor.execute(sql, valores)

        # Confirma los cambios en la base de datos
        conexion.commit()

        # Se cierra el cursor y la conexion para liberar recursos
        cursor.close()
        conexion.close()

        return True

    def consultar_todos(self):
        # Se obtiene la conexion a la base de datos
        conexion = obtener_conexion()

        # El cursor permite ejecutar las instrucciones SQL
        cursor = conexion.cursor()

        cursor.execute("SELECT id, nombre, correo, carrera FROM estudiantes")

        # El método fetchall obtiene todos los registros encontrados
        registros = cursor.fetchall()

        # Lista donde se almacenarán los objetos Estudiante
        estudiantes = []

        # Se recorre cada registro devuelto por la Base de Datos

        for registro in registros:
            # Cada registro es una tupla con el orden:
            # id, nombre, correo, carrera
            estudiante = Estudiante(
                id_estudiante=registro[0],
                nombre=registro[1],
                correo=registro[2],
                carrera=registro[3],
            )
            # Se agrega el objeto Estudiante a la lista
            estudiantes.append(estudiante)

            cursor.close()
            conexion.close()

            return estudiantes

    def buscar_por_id(self, id_estudiante):
        """
        Busca un estudiante por su ID

        :param id_estudiante: ID del estudiante que se buscará
        :return:
        Si existe el objeto con el id dado se retorna dicho objeto
        si no existe, se retorna None
        """

        # Se obtiene la conexion a la base de datos
        conexion = obtener_conexion()

        # El cursor permite ejecutar las instrucciones SQL
        cursor = conexion.cursor()

        # Consulta con Where
        sql = "SELECT id, nombre, correo, carrera FROM estudiantes WHERE id=%s"

        # Aunque sea solo un dato debe enviarse como una tupla
        cursor.execute(sql, (id_estudiante,))

        # Fetchone obtiene un solo registro
        registro = cursor.fetchone()

        cursor.close()
        conexion.close()

        # Si no se encuentra un estudiante con
        # el id dado se retorna None
        if registro is None:
            return None

        # Si se encontró, se convierte en un objeto
        # Estudiante y se devuelve
        return Estudiante(
            id_estudiante=registro[0],
            nombre=registro[1],
            correo=registro[2],
            carrera=registro[3])

    def actualizar(self, estudiante):
        """
        Actualiza los datos de un estudiante existente

        :param estudiante: Objeto Estudiante con el ID
        y los nuevos datos
        :return: True si se actualiza al menos un registro,

        """

        # Se obtiene la conexion a la base de datos
        conexion = obtener_conexion()

        cursor = conexion.cursor()

        # Consulta con WHERE para fliltrar por ID
        sql = """
        UPDATE estudiantes
        SET nombre=%s, 
            correo=%s, 
            carrera=%s
        WHERE id=%s
        """

        valores = (
            estudiante.nombre,
            estudiante.correo,
            estudiante.carrera,
            estudiante.id_estudiante
        )
        cursor.execute(sql, valores)
        conexion.commit()

        # RowCount indica cuántas filas fueron afectadas
        # por la consulta
        filas_afectadas = cursor.rowcount

        cursor.close()
        conexion.close()

        return filas_afectadas > 0

    def eliminar(self, id_estudiante):
        """
        Elimina un estudainte por su ID


        :Param id_Estudiantes: EL ID del estudiante
        que se va a eliminar
        :return: True si se actualiza al menos un registro,

        """

        # Se obtiene la conexión
        conexion = obtener_conexion()

        cursor = conexion.cursor()

        sql = "DELETE FROM ESTUDIANTES WHERE id=%s"
        cursor.execute(sql, (id_estudiante,))
        conexion.commit()

        # Rowcount indica cuántas filas fueron afecadas
        # por la consulta
        filas_afectadas = cursor.rowcount

        cursor.close()
        conexion.close()
        return filas_afectadas > 0

    def existe_correo(self, correo):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        # Consulta con WHERE para filtrar por ID
        sql = "SELECT id FROM estudiantes WHERE correo=%s"
        cursor.execute(sql, (correo,))
        registro = cursor.fetchone()

        cursor.close()
        conexion.close()
        return registro is not None
