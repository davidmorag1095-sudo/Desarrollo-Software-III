from GestionBiblioteca.service.autor_service import AutorService


class AutorController:
    def __init__(self):
        self.service = AutorService()

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def mostrar_menu(self):
        opcion = ""
        while opcion != "7":
            print("\n===============================")
            print(" SISTEMA DE GESTION DE AUTORES")
            print("===============================")
            print("1. Registrar autor")
            print("2. Consultar autores")
            print("3. Buscar autor por ID")
            print("4. Buscar autor por nombre")
            print("5. Actualizar autor")
            print("6. Eliminar autor")
            print("7. Salir")

            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                self.registrar()
            elif opcion == "2":
                self.consultar()
            elif opcion == "3":
                self.buscar_por_id()
            elif opcion == "4":
                self.buscar_por_nombre()
            elif opcion == "5":
                self.actualizar()
            elif opcion == "6":
                self.eliminar()
            elif opcion == "7":
                print("Regresando al menu principal")
            else:
                print("Debe seleccionar una opcion valida")

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def registrar(self):
        print("\n----- Registrar autor -----")
        nombre = input("Nombre: ")
        nacionalidad = input("Nacionalidad: ")

        mensaje = self.service.registrar_autor(nombre, nacionalidad)
        print(mensaje)

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def consultar(self):
        print("\n----- Lista de autores -----")
        autores = self.service.consultar_autores()

        if len(autores) == 0:
            print("No hay autores registrados")
            return

        for autor in autores:
            print(autor)

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def buscar_por_id(self):
        print("\n----- Buscar autor por ID -----")
        try:
            id_autor = int(input("Digite el ID del autor: "))
        except ValueError:
            print("Error: el ID debe ser un numero entero")
            return

        autor = self.service.buscar_autor(id_autor)
        print("No se encontro un autor con ese ID" if autor is None else autor)

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def buscar_por_nombre(self):
        print("\n----- Buscar autor por nombre -----")
        nombre = input("Digite el nombre del autor: ")

        autor = self.service.buscar_autor_por_nombre(nombre)
        print("No se encontro un autor con ese nombre" if autor is None else autor)

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def actualizar(self):
        print("\n----- Actualizar autor -----")
        try:
            id_autor = int(input("Digite el ID del autor: "))
        except ValueError:
            print("Error: el ID debe ser un numero entero")
            return

        autor = self.service.buscar_autor(id_autor)
        if autor is None:
            print("No existe un autor con ese ID")
            return

        print("Datos actuales")
        print(autor)

        nombre = input("Nuevo nombre: ")
        nacionalidad = input("Nueva nacionalidad: ")

        mensaje = self.service.actualizar_autor(id_autor, nombre, nacionalidad)
        print(mensaje)

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def eliminar(self):
        print("\n----- Eliminar autor -----")
        try:
            id_autor = int(input("Digite el ID del autor: "))
        except ValueError:
            print("Error: el ID debe ser un numero entero")
            return

        autor = self.service.buscar_autor(id_autor)
        if autor is None:
            print("No existe un autor con ese ID")
            return

        print("Autor encontrado")
        print(autor)

        confirmacion = input("Esta seguro de eliminarlo? (s/n): ")
        if confirmacion.lower() == "s":
            mensaje = self.service.eliminar_autor(id_autor)
            print(mensaje)
        else:
            print("Operacion cancelada")

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def reporte_por_nacionalidad(self):
        print("\n----- Autores por nacionalidad -----")
        nacionalidad = input("Digite la nacionalidad: ")

        autores = self.service.autores_por_nacionalidad(nacionalidad)
        if len(autores) == 0:
            print("No hay autores con esa nacionalidad")
            return

        for autor in autores:
            print(autor)
