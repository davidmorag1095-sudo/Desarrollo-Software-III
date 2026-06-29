"""
Archivo: cliente_controller.py

Responsabilidad:
Coordinar la interacción por consola entre el usuario y el service.
"""

from service.cliente_service import ClienteService


class ClienteController:
    """Controlador del módulo de clientes para consola."""

    def __init__(self):
        self.service = ClienteService()

    def mostrar_menu(self):
        opcion = ""
        while opcion != "7":
            print("================================")
            print(" SISTEMA DE GESTIÓN DE CLIENTES")
            print("================================")
            print("1. Registrar cliente")
            print("2. Consultar clientes")
            print("3. Buscar cliente por ID")
            print("4. Buscar cliente por cédula")
            print("5. Actualizar cliente")
            print("6. Eliminar cliente")
            print("7. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1": self.registrar()
            elif opcion == "2": self.consultar()
            elif opcion == "3": self.buscar_por_id()
            elif opcion == "4": self.buscar_por_cedula()
            elif opcion == "5": self.actualizar()
            elif opcion == "6": self.eliminar()
            elif opcion == "7": print("Saliendo del sistema...")
            else: print("Opción inválida. Intente de nuevo.")

    def registrar(self):
        print("--- Registrar cliente ---")
        cedula = input("Cédula: ")
        nombre = input("Nombre completo: ")
        correo = input("Correo electrónico: ")
        telefono = input("Teléfono: ")
        direccion = input("Dirección: ")
        exito, mensaje = self.service.registrar_cliente(cedula, nombre, correo, telefono, direccion)
        print(mensaje)

    def consultar(self):
        print("--- Lista de clientes ---")
        clientes = self.service.consultar_clientes()
        if len(clientes) == 0:
            print("No hay clientes registrados.")
            return
        for cliente in clientes:
            print(cliente)

    def buscar_por_id(self):
        print("--- Buscar cliente por ID ---")
        try:
            id_cliente = int(input("Digite el ID del cliente: "))
        except ValueError:
            print("Error: el ID debe ser un número entero.")
            return
        cliente = self.service.buscar_cliente_por_id(id_cliente)
        print("No se encontró un cliente con ese ID." if cliente is None else cliente)

    def buscar_por_cedula(self):
        print("--- Buscar cliente por cédula ---")
        cedula = input("Digite la cédula del cliente: ")
        cliente = self.service.buscar_cliente_por_cedula(cedula)
        print("No se encontró un cliente con esa cédula." if cliente is None else cliente)

    def actualizar(self):
        print("--- Actualizar cliente ---")
        try:
            id_cliente = int(input("Digite el ID del cliente: "))
        except ValueError:
            print("Error: el ID debe ser un número entero.")
            return
        cliente = self.service.buscar_cliente_por_id(id_cliente)
        if cliente is None:
            print("No existe un cliente con ese ID.")
            return
        print("Datos actuales:")
        print(cliente)
        cedula = input("Nueva cédula: ")
        nombre = input("Nuevo nombre: ")
        correo = input("Nuevo correo: ")
        telefono = input("Nuevo teléfono: ")
        direccion = input("Nueva dirección: ")
        exito, mensaje = self.service.actualizar_cliente(id_cliente, cedula, nombre, correo, telefono, direccion)
        print(mensaje)

    def eliminar(self):
        print("--- Eliminar cliente ---")
        try:
            id_cliente = int(input("Digite el ID del cliente: "))
        except ValueError:
            print("Error: el ID debe ser un número entero.")
            return
        cliente = self.service.buscar_cliente_por_id(id_cliente)
        if cliente is None:
            print("No existe un cliente con ese ID.")
            return
        print("Cliente encontrado:")
        print(cliente)
        confirmacion = input("¿Está seguro de eliminarlo? (s/n): ")
        if confirmacion.lower() == "s":
            exito, mensaje = self.service.eliminar_cliente(id_cliente)
            print(mensaje)
        else:
            print("Operación cancelada.")
