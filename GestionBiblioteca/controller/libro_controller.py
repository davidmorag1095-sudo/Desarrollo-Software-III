from GestionBiblioteca.service.libro_service import LibroService


class LibroController:
    def __init__(self):
        self.service = LibroService()

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def mostrar_menu(self):
        opcion = ""
        while opcion != "9":
            print("\n===============================")
            print(" SISTEMA DE GESTION DE LIBROS")
            print("===============================")
            print("1. Registrar libro")
            print("2. Consultar libros")
            print("3. Buscar libro por codigo")
            print("4. Actualizar libro")
            print("5. Eliminar libro")
            print("6. Reporte libros ordenados por titulo")
            print("7. Reporte libros por categoria")
            print("8. Reporte libros por autor")
            print("9. Salir")

            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                self.registrar()
            elif opcion == "2":
                self.consultar()
            elif opcion == "3":
                self.buscar()
            elif opcion == "4":
                self.actualizar()
            elif opcion == "5":
                self.eliminar()
            elif opcion == "6":
                self.reporte_ordenados_por_titulo()
            elif opcion == "7":
                self.reporte_por_categoria()
            elif opcion == "8":
                self.reporte_por_autor()
            elif opcion == "9":
                print("Regresando al menu principal")
            else:
                print("Debe seleccionar una opcion valida")

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def registrar(self):
        print("\n----- Registrar libro -----")
        codigo = input("Codigo: ")
        titulo = input("Titulo: ")
        categoria = input("Categoria: ")

        try:
            anio_publicacion = int(input("Anio de publicacion: "))
            autor_id = int(input("ID del autor: "))
        except ValueError:
            print("Error: el anio y el ID del autor deben ser numeros enteros")
            return

        mensaje = self.service.registrar_libro(codigo, titulo, categoria, anio_publicacion, autor_id)
        print(mensaje)

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def consultar(self):
        print("\n----- Lista de libros -----")
        libros = self.service.consultar_libros()

        if len(libros) == 0:
            print("No hay libros registrados")
            return

        for libro in libros:
            print(libro)

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def buscar(self):
        print("\n----- Buscar libro por codigo -----")
        codigo = input("Digite el codigo del libro: ")

        libro = self.service.buscar_libro(codigo)
        print("No se encontro un libro con ese codigo" if libro is None else libro)

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def actualizar(self):
        print("\n----- Actualizar libro -----")
        codigo = input("Digite el codigo del libro: ")

        libro = self.service.buscar_libro(codigo)
        if libro is None:
            print("No existe un libro con ese codigo")
            return

        print("Datos actuales")
        print(libro)

        titulo = input("Nuevo titulo: ")
        categoria = input("Nueva categoria: ")

        try:
            anio_publicacion = int(input("Nuevo anio de publicacion: "))
            autor_id = int(input("Nuevo ID del autor: "))
        except ValueError:
            print("Error: el anio y el ID del autor deben ser numeros enteros")
            return

        mensaje = self.service.actualizar_libro(codigo, titulo, categoria, anio_publicacion, autor_id)
        print(mensaje)

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def eliminar(self):
        print("\n----- Eliminar libro -----")
        codigo = input("Digite el codigo del libro: ")

        libro = self.service.buscar_libro(codigo)
        if libro is None:
            print("No existe un libro con ese codigo")
            return

        print("Libro encontrado")
        print(libro)

        confirmacion = input("Esta seguro de eliminarlo? (s/n): ")
        if confirmacion.lower() == "s":
            mensaje = self.service.eliminar_libro(codigo)
            print(mensaje)
        else:
            print("Operacion cancelada")

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def reporte_ordenados_por_titulo(self):
        print("\n----- Libros ordenados por titulo -----")
        libros = self.service.libros_ordenados_por_titulo()

        if len(libros) == 0:
            print("No hay libros registrados")
            return

        for libro in libros:
            print(libro)

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def reporte_por_categoria(self):
        print("\n----- Libros por categoria -----")
        categoria = input("Digite la categoria: ")

        libros = self.service.libros_por_categoria(categoria)
        if len(libros) == 0:
            print("No hay libros en esa categoria")
            return

        for libro in libros:
            print(libro)

#----------------------------------------------------------------------------------------------------------------------------------------------------
    def reporte_por_autor(self):
        print("\n----- Libros por autor -----")
        nombre_autor = input("Digite el nombre del autor: ")

        libros = self.service.libros_por_autor(nombre_autor)
        if len(libros) == 0:
            print("No hay libros registrados para ese autor")
            return

        for libro in libros:
            print(libro)
