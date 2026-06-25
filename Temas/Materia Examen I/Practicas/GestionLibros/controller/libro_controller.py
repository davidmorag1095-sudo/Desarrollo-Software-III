from service.libro_service import LibroService

class LibroController:
    def __init__(self):
        self.service = LibroService()

    def mostrar_menu(self):
        opcion = ""

        while opcion != "7":
            print("\n================================")
            print(" SISTEMA DE GESTION DE LIBROS")
            print("================================")
            print("1. Registrar libro")
            print("2. Mostrar libros")
            print("3. Buscar libro por codigo")
            print("4. Buscar libros por categoria")
            print("5. Actualizar libro")
            print("6. Eliminar libro")
            print("7. Salir")

            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                self.registrar()

            elif opcion == "2":
                self.mostrar_libros()

            elif opcion == "3":
                self.buscar_por_codigo()

            elif opcion == "4":
                self.buscar_por_categoria()

            elif opcion == "5":
                self.actualizar()

            elif opcion == "6":
                self.eliminar()

            elif opcion == "7":
                print("Saliendo del sistema...")

            else:
                print("Opcion invalida. Intente de nuevo.")

    def registrar(self):
        print("\n--- Registrar libro ---")

        codigo = input("Codigo: ")
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        categoria = input("Categoria: ")

        mensaje = self.service.registrar_libro(
            codigo,
            titulo,
            autor,
            categoria
        )

        print(mensaje)

    def mostrar_libros(self):
        print("\n--- Lista de libros ---")

        libros = self.service.listar_libros()

        if len(libros) == 0:
            print("No hay libros registrados.")
            return

        for libro in libros:
            print(libro)

    def buscar_por_codigo(self):
        print("\n--- Buscar libro por codigo ---")

        codigo = input("Digite el codigo del libro: ")

        libro = self.service.buscar_libro_por_codigo(codigo)

        if libro is None:
            print("No se encontro un libro con ese codigo.")
        else:
            print(libro)

    def buscar_por_categoria(self):
        print("\n--- Buscar libros por categoria ---")

        categoria = input("Digite la categoria: ")

        resultado = self.service.buscar_libros_por_categoria(categoria)

        if isinstance(resultado, str):
            print(resultado)
            return

        if len(resultado) == 0:
            print("No se encontraron libros en esa categoria.")
            return

        for libro in resultado:
            print(libro)

    def actualizar(self):
        print("\n--- Actualizar libro ---")

        codigo = input("Digite el codigo del libro: ")
        libro = self.service.buscar_libro_por_codigo(codigo)

        if libro is None:
            print("No existe un libro con ese codigo.")
            return

        print("\nDatos actuales:")
        print(libro)

        print("\nDigite los nuevos datos:")
        titulo = input("Nuevo titulo: ")
        autor = input("Nuevo autor: ")
        categoria = input("Nueva categoria: ")

        mensaje = self.service.actualizar_libro(
            codigo,
            titulo,
            autor,
            categoria
        )

        print(mensaje)

    def eliminar(self):
        print("\n--- Eliminar libro ---")

        codigo = input("Digite el codigo del libro: ")
        libro = self.service.buscar_libro_por_codigo(codigo)

        if libro is None:
            print("No existe un libro con ese codigo.")
            return

        print("\nLibro encontrado:")
        print(libro)

        confirmacion = input("Esta seguro de eliminarlo? (s/n): ")

        if confirmacion.lower() == "s":
            mensaje = self.service.eliminar_libro(codigo)
            print(mensaje)
        else:
            print("Operacion cancelada.")

