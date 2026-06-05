"""
Archivo: cliente_repository.py

Responsabilidad:
Comunicarse directamente con la base de datos.
Aquí se escriben las consultas SQL.
"""

from database.conexion import obtener_conexion
from model.cliente import Cliente


class ClienteRepository:
    """Repositorio encargado de administrar clientes en MySQL."""

    def registrar(self, cliente):
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            INSERT INTO clientes (cedula, nombre, correo, telefono, direccion)
            VALUES (%s, %s, %s, %s, %s)
        """
        valores = (cliente.cedula, cliente.nombre, cliente.correo, cliente.telefono, cliente.direccion)

        cursor.execute(sql, valores)
        conexion.commit()
        cursor.close()
        conexion.close()
        return True

    def consultar_todos(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("""
            SELECT id, cedula, nombre, correo, telefono, direccion
            FROM clientes
            ORDER BY id ASC
        """)

        registros = cursor.fetchall()
        clientes = []

        for registro in registros:
            clientes.append(Cliente(
                id_cliente=registro[0],
                cedula=registro[1],
                nombre=registro[2],
                correo=registro[3],
                telefono=registro[4],
                direccion=registro[5]
            ))

        cursor.close()
        conexion.close()
        return clientes

    def buscar_por_id(self, id_cliente):
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            SELECT id, cedula, nombre, correo, telefono, direccion
            FROM clientes
            WHERE id = %s
        """
        cursor.execute(sql, (id_cliente,))
        registro = cursor.fetchone()

        cursor.close()
        conexion.close()

        if registro is None:
            return None

        return Cliente(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5])

    def buscar_por_cedula(self, cedula):
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            SELECT id, cedula, nombre, correo, telefono, direccion
            FROM clientes
            WHERE cedula = %s
        """
        cursor.execute(sql, (cedula,))
        registro = cursor.fetchone()

        cursor.close()
        conexion.close()

        if registro is None:
            return None

        return Cliente(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5])

    def buscar_por_correo(self, correo):
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            SELECT id, cedula, nombre, correo, telefono, direccion
            FROM clientes
            WHERE correo = %s
        """
        cursor.execute(sql, (correo,))
        registro = cursor.fetchone()

        cursor.close()
        conexion.close()

        if registro is None:
            return None

        return Cliente(registro[0], registro[1], registro[2], registro[3], registro[4], registro[5])

    def actualizar(self, cliente):
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            UPDATE clientes
            SET cedula = %s,
                nombre = %s,
                correo = %s,
                telefono = %s,
                direccion = %s
            WHERE id = %s
        """
        valores = (cliente.cedula, cliente.nombre, cliente.correo, cliente.telefono, cliente.direccion, cliente.id_cliente)

        cursor.execute(sql, valores)
        conexion.commit()
        filas_afectadas = cursor.rowcount

        cursor.close()
        conexion.close()
        return filas_afectadas > 0

    def eliminar(self, id_cliente):
        conexion = obtener_conexion()
        cursor = conexion.cursor()

        sql = "DELETE FROM clientes WHERE id = %s"
        cursor.execute(sql, (id_cliente,))
        conexion.commit()
        filas_afectadas = cursor.rowcount

        cursor.close()
        conexion.close()
        return filas_afectadas > 0

    def existe_cedula(self, cedula):
        return self.buscar_por_cedula(cedula) is not None

    def existe_correo(self, correo):
        return self.buscar_por_correo(correo) is not None
