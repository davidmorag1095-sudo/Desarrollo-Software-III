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
        return int(input("Seleccione una opcion: "))


    def pedir_Cliente(self):
        codigo = int(input("Digite el codigo del cliente: "))
        nombre = input("Digite el nombre del cliente: ")
        telefono = int(input("Digite el telefono del cliente: "))
        return codigo, nombre, telefono


    def pedir_Flete(self):
        numero = int(input("Digite el numero del flete: "))
        destino = input("Digite el destino: ")
        monto = int(input("Digite el monto del flete: "))
        indice_Cliente = int(input("Ingrese el indice del Cliente: "))

        return numero, destino, monto, indice_Cliente

    def mostrar_Lista(self, lista):
        if not lista:
            print("No hay datos")

        else:
            for indice, obj, in enumerate(lista):
                print(indice, "-", obj)