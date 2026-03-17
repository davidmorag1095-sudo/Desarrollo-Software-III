class Vista:
    """
    Vista del sistema(MVC)
    Encargada unicamente de la interacion con el usuario
    """

    def menu(self):
        """Muestra el menu principal del sistema"""
        print("\n === SISTEMA DE FLETES ===")
        print("1. Agregar Cliente")
        print("2. Consultar Cliente")
        print("3. Agregar Flete")
        print("4. Consultar Flete")
        print("5. Salir")

        return int(input("Seleccione una opcion: "))

    def pedir_cliente(self):
        """Solicita datos del cliente"""
        codigo = input("Ingrese el codigo del cliente: ")
        nombre = input("Ingrese el nombre del cliente: ")
        telefono = input("Ingrese el telefono del cliente: ")
        return codigo, nombre, telefono

    def pedir_flete(self):
        """"Solicita datos del flete"""
        numero = int(input("Numero"))
        destino = input("Ingrese el destino: ")
        monto = int (input("Ingrese el monto del flete: "))
        clave_cliente = input("Ingrese el codigo del cliente: ")

        return numero, destino, monto, clave_cliente




