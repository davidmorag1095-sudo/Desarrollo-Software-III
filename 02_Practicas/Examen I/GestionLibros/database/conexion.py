import mysql.connector
from mysql.connector import Error


def obtener_conexion():
    try:
        # Datos de conexion a MySQL
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345",
            database="biblioteca",
            port=3306
        )

        return conexion

    except Error as error:
        print("Error al conectar con la base de datos:", error)
        raise
