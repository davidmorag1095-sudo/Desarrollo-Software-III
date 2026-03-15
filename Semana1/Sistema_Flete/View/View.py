class View:
    def menu(self):
        print("/n === SISTEMA DE FLETES ===")
        print("1. Agregar Cliente")
        print("2. Agregar Flete")
        print("3. Modificar Cliente")
        print("4. Modificar Flete")
        print("5. Consultar Cliente")
        print("6. Consultar Flete")
        print("0. Salir")
        return input("Seleccione una opcion: ")


    def pedir_Cliente(self):
        codigo = input("Digite el codigo del cliente: ")
        nombre = input("Digite el nombre del cliente: ")
        telefono = input("Digite el telefono del cliente: ")
        return codigo, nombre, telefono


    def pedir_Flete(self):
        numero = input("Digite el numero del flete: ")
        destino = input("Digite el destino: ")
        monto = input("Digite el monto del flete: ")
        indice_Cliente = input("Ingrese el indice del Cliente: ")

        return numero, destino, monto, indice_Cliente


    def mostrar_Lista(self, lista):
        if not lista:
            print("No hay datos")

        else:
            for indice, obj, in enumerate(lista):
                print(indice, "-", obj)