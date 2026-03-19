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

    def mostrar_fletes(self, diccionario):
        """Muestra los fletes en el diccionario"""

        """La extraccion de los fletes se realiza por medio de valores 
        en el diccionario"""
        if not diccionario:
            print("No hay fletes almacenados")

        else:
            for valores in diccionario.values():
                print(valores)

    def mostrar_clientes(self, diccionario):
        """
        Imprime los valores del diccionario de clientes
        """
        if not diccionario:
            print("No hay clientes almacenados")
        else:
            """Dado que el codigo del cliente se guarda como llave, se extraen los valores. 
            Esto difiere de la firma de extraer los fletes
            """

        for clave, valor in diccionario.items():
            print(clave, "-", valor)






