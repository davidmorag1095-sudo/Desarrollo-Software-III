from database.conexion import obtener_conexion
from model.libro import Libro


class LibroRepository:
    def guardar(self, libro):
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            INSERT INTO libros (codigo, titulo, autor, categoria)
            VALUES (%s, %s, %s, %s)
        """

        valores = (
            libro.codigo,
            libro.titulo,
            libro.autor,
            libro.categoria
        )

        cursor.execute(sql, valores)
        conexion.commit()

        cursor.close()
        conexion.close()

        return True

    def listar(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT codigo, titulo, autor, categoria FROM libros")
        registros = cursor.fetchall()

        libros = []

        for registro in registros:
            libro = Libro(
                codigo=registro[0],
                titulo=registro[1],
                autor=registro[2],
                categoria=registro[3]
            )

            libros.append(libro)

        cursor.close()
        conexion.close()

        return libros

    def buscar_por_codigo(self, codigo):
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = "SELECT codigo, titulo, autor, categoria FROM libros WHERE codigo = %s"
        cursor.execute(sql, (codigo,))

        registro = cursor.fetchone()

        cursor.close()
        conexion.close()

        if registro is None:
            return None

        return Libro(
            codigo=registro[0],
            titulo=registro[1],
            autor=registro[2],
            categoria=registro[3]
        )

    def buscar_por_categoria(self, categoria):
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            SELECT codigo, titulo, autor, categoria
            FROM libros
            WHERE categoria LIKE %s
        """

        cursor.execute(sql, (f"%{categoria}%",))

        registros = cursor.fetchall()
        libros = []

        for registro in registros:
            libro = Libro(
                codigo=registro[0],
                titulo=registro[1],
                autor=registro[2],
                categoria=registro[3]
            )

            libros.append(libro)

        cursor.close()
        conexion.close()

        return libros

    def actualizar(self, libro):
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            UPDATE libros
            SET titulo = %s,
                autor = %s,
                categoria = %s
            WHERE codigo = %s
        """

        valores = (
            libro.titulo,
            libro.autor,
            libro.categoria,
            libro.codigo
        )

        cursor.execute(sql, valores)
        conexion.commit()

        filas_afectadas = cursor.rowcount

        cursor.close()
        conexion.close()

        return filas_afectadas > 0

    def eliminar(self, codigo):
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = "DELETE FROM libros WHERE codigo = %s"

        cursor.execute(sql, (codigo,))
        conexion.commit()

        filas_afectadas = cursor.rowcount

        cursor.close()
        conexion.close()

        return filas_afectadas > 0

