"""
Archivo: conexion.py

Responsabilidad:
Este archivo se encarga únicamente de crear y devolver la conexión
con la base de datos MySQL.

Importante:
Antes de ejecutar el proyecto, revise que el usuario, contraseña,
host y nombre de base de datos coincidan con su instalación de MySQL.
"""

import mysql.connector
from mysql.connector import Error


def obtener_conexion():
    """
    Crea una conexión con la base de datos MySQL.

    Returns:
        conexion: objeto de conexión a MySQL.

    Raises:
        Error: si ocurre algún problema al intentar conectarse.
    """

    try:
        # Se crea la conexión con el servidor MySQL.
        # host="localhost" indica que MySQL está instalado en la misma computadora.
        # user="root" es el usuario por defecto en muchas instalaciones.
        # password debe cambiarse por la contraseña real del MySQL del estudiante.
        # database indica la base de datos que se usará.
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345",
            database="universidad",
            port=3306
        )

        # Si la conexión fue exitosa, se devuelve al archivo que la solicitó.
        return conexion

    except Error as error:
        # Si ocurre un error, se muestra en pantalla.
        print("Error al conectar con la base de datos:", error)

        # Se vuelve a lanzar el error para que el programa sepa que la conexión falló.
        raise
