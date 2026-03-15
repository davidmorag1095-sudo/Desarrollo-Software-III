class Vista:
    """vista del sistema"""
    def menu(self):
        print("/n === SISTEMA DE FLETES ===")
        print("1. Agregar Cliente")
        print("2. Agregar Flete")
        print("3. Modificar Cliente")
        print("4. Modificar Flete")
        print("5. Consultar Cliente")
        print("6. Consultar Flete")
        print('0. Salir')
        return input('Seleccione una opcion: ')

    def pedir_cliente(self):
        codigo=input('Ingrese el codigo del cliente: ')
        nombre=input('Ingrese el nombre del cliente: ')
        telefono=input('Ingrese el telefono del cliente: ')
        return codigo, nombre, telefono

    def pedir_flete(self):
        numero=input('Ingrese el numero del flete: ')
        destino=input('Ingrese el destino: ')
        monto=input('Ingrese el monto: ')
        indice_cliente=input('Ingrese el indice_cliente: ')

        return numero, destino, monto, indice_cliente

    def mostrar_lista(self):
        if not lista:
            print("no hay datos")
        else:
            for i, obj, in enumerate(lista):
                print(i, '-', obj)
