"""
Archivo: conexion.py

Responsabilidad:
Crear y devolver la conexión con MySQL.
Este archivo es usado tanto por la versión de consola como por la versión web.
"""

import mysql.connector
from mysql.connector import Error


def obtener_conexion():
    """
    Crea una conexión con la base de datos MySQL.

    Returns:
        Objeto de conexión a MySQL.
    """

    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="empresa_clientes",
            port=3306
        )
        return conexion
    except Error as error:
        print("Error al conectar con la base de datos:", error)
        raise
