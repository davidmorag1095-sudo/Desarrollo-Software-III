class Vista:
    def menu(self):
        print("\n ===SISTEMA DE BIBLIOTECA ===\n")
        print(" 1.Agregar estudiante")
        print(" 2. Agregar libro")
        print(" 3. Registrar préstamo")
        print(" 4. Consultar estudiantes")
        print(" 5. Consultar libros")
        print(" 6. Consultar préstamos")
        print(" 7. Consultar categorías")
        print(" 8. Salir")
        return int(input("Seleccione una opcion: "))

    def pedir_estudiante(self):
        carnet = input("Ingrese el carnet del estudiante: ")
        nombre = input("Ingrese el nombre del estudiante: ")
        carrera = input("Ingrese la carrera a la que pertenece el estudiante: ")
        print("----------------------------------------------------")
        print("AGREGADO CON EXITO")
        print("----------------------------------------------------")
        return carnet,nombre,carrera


    def pedir_libro(self):
        codigoLibro = input("Ingrese el codigo del libro: ")
        titulo = input("Ingrese el titulo del libro: ")
        autor = input("Ingrese el autor del libro: ")
        categoria = input("Ingrese la categoria del libro: ")
        print("----------------------------------------------------")
        print("AGREGADO CON EXITO")
        print("----------------------------------------------------")
        return codigoLibro, titulo, autor, categoria



    def pedir_prestamo(self):
        numeroPrestamo = input("Ingrese el numero del prestamo: ")
        estudianteAsociado = input("Ingrese el estudiante asociado: ")
        libroAsociado = input("Ingrese el libro asociado: ")
        fecha = input("Ingrese la fecha del prestamo: ")
        print("----------------------------------------------------")
        print("AGREGADO CON EXITO")
        print("----------------------------------------------------")
        return numeroPrestamo,estudianteAsociado,libroAsociado,fecha

    def mostrar_estudiantes(self,diccionarioEstudiantes):
        if not diccionarioEstudiantes:
            print("No hay estudiantes en el diccionario")
        else:
            for clave,valor in diccionarioEstudiantes.items():
                print (clave, "-", valor)

    def mostrar_Libros(self,diccionarioLibros):
        if not diccionarioLibros:
            print("No hay libros en el diccionario")
        else:
            for clave,valor in diccionarioLibros.items():
                print (clave, "-", valor)

    def mostrar_Prestamos(self, diccionarioPrestamos):
        if not diccionarioPrestamos:
            print("No hay prestamos en el diccionario")
        else:
            for clave, valor in diccionarioPrestamos.items():
                print(clave, "-", valor)

    def pedir_carnet(self):
        return input("Ingrese el carnet a buscar: ")

    def pedir_codigo_libro(self):
        return input("Ingrese el código del libro a buscar: ")

    def mostrar_categorias(self, categorias):
        if not categorias:
            print("No hay categorías registradas")
        else:
            for categoria in categorias:
                print(categoria)

    def mostrar_estudiantes_iter(self, diccionarioEstudiantes):
        it = iter(diccionarioEstudiantes.items())
        try:
            while True:
                clave, valor = next(it)
                print(clave, "-", valor)
        except StopIteration:
            pass