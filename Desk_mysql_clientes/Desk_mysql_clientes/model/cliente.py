"""
Archivo: cliente.py

Responsabilidad:
Representar la entidad Cliente del sistema.
"""


class Cliente:
    """Clase que representa un cliente."""

    def __init__(self, id_cliente=None, cedula="", nombre="", correo="", telefono="", direccion=""):
        self.id_cliente = id_cliente
        self.cedula = cedula
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion

    def __str__(self):
        return (
            f"ID: {self.id_cliente} | "
            f"Cédula: {self.cedula} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo} | "
            f"Teléfono: {self.telefono} | "
            f"Dirección: {self.direccion}"
        )
