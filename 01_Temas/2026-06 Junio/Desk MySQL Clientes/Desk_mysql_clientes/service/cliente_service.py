"""
Archivo: cliente_service.py

Responsabilidad:
Contener reglas de negocio y validaciones.
Este service lo usa tanto la consola como Flask.
"""

from Desk_mysql_clientes.Desk_mysql_clientes.model.cliente import Cliente
from Desk_mysql_clientes.Desk_mysql_clientes.repository.cliente_repository import ClienteRepository


class ClienteService:
    """Servicio que contiene la lógica de negocio de clientes."""

    def __init__(self):
        self.repository = ClienteRepository()

    def registrar_cliente(self, cedula, nombre, correo, telefono, direccion):
        cedula = cedula.strip()
        nombre = nombre.strip()
        correo = correo.strip()
        telefono = telefono.strip()
        direccion = direccion.strip()

        if cedula == "" or nombre == "" or correo == "" or telefono == "" or direccion == "":
            return False, "Error: todos los campos son obligatorios."

        if not cedula.isdigit():
            return False, "Error: la cédula debe contener solo números."

        if "@" not in correo or "." not in correo:
            return False, "Error: el correo no tiene un formato válido."

        if self.repository.existe_cedula(cedula):
            return False, "Error: ya existe un cliente con esa cédula."

        if self.repository.existe_correo(correo):
            return False, "Error: ya existe un cliente con ese correo."

        cliente = Cliente(cedula=cedula, nombre=nombre, correo=correo, telefono=telefono, direccion=direccion)
        self.repository.registrar(cliente)
        return True, "Cliente registrado correctamente."

    def consultar_clientes(self):
        return self.repository.consultar_todos()

    def buscar_cliente_por_id(self, id_cliente):
        return self.repository.buscar_por_id(id_cliente)

    def buscar_cliente_por_cedula(self, cedula):
        cedula = cedula.strip()
        if cedula == "":
            return None
        return self.repository.buscar_por_cedula(cedula)

    def actualizar_cliente(self, id_cliente, cedula, nombre, correo, telefono, direccion):
        cedula = cedula.strip()
        nombre = nombre.strip()
        correo = correo.strip()
        telefono = telefono.strip()
        direccion = direccion.strip()

        if cedula == "" or nombre == "" or correo == "" or telefono == "" or direccion == "":
            return False, "Error: todos los campos son obligatorios."

        if not cedula.isdigit():
            return False, "Error: la cédula debe contener solo números."

        if "@" not in correo or "." not in correo:
            return False, "Error: el correo no tiene un formato válido."

        cliente_existente = self.repository.buscar_por_id(id_cliente)
        if cliente_existente is None:
            return False, "Error: no existe un cliente con ese ID."

        cliente_con_cedula = self.repository.buscar_por_cedula(cedula)
        if cliente_con_cedula is not None and cliente_con_cedula.id_cliente != id_cliente:
            return False, "Error: ya existe otro cliente con esa cédula."

        cliente_con_correo = self.repository.buscar_por_correo(correo)
        if cliente_con_correo is not None and cliente_con_correo.id_cliente != id_cliente:
            return False, "Error: ya existe otro cliente con ese correo."

        cliente_actualizado = Cliente(
            id_cliente=id_cliente,
            cedula=cedula,
            nombre=nombre,
            correo=correo,
            telefono=telefono,
            direccion=direccion
        )

        actualizado = self.repository.actualizar(cliente_actualizado)
        if actualizado:
            return True, "Cliente actualizado correctamente."

        return False, "Error: no se pudo actualizar el cliente."

    def eliminar_cliente(self, id_cliente):
        cliente = self.repository.buscar_por_id(id_cliente)
        if cliente is None:
            return False, "Error: no existe un cliente con ese ID."

        eliminado = self.repository.eliminar(id_cliente)
        if eliminado:
            return True, "Cliente eliminado correctamente."

        return False, "Error: no se pudo eliminar el cliente."
