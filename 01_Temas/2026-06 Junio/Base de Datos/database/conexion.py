import mysql.connector
from mysql.connector import Error


def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="universidad",
            port=3306,
        )
        return conexion
    except Error as error:
        print("Error al conectar la base de datos")

        raise
