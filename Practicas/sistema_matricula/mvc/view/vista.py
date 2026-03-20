class Vista:
    """
    Vista del sistema
    Encargada de la interacción con el usuario
    """

    def menu(self):
        print("\n------- SISTEMA DE MATRÍCULA ------")
        print("1. Agregar estudiante")
        print("2. Agregar curso")
        print("3. Matricular estudiante")
        print("4. Consultar estudiantes")
        print("5. Consultar cursos")
        print("6. Consultar matrículas")
        print("7. Salir")
        return input("Seleccione una opción: ")

    def pedir_estudiante(self):
        carnet = input("Carnet: ")
        nombre = input("Nombre: ")
        carrera = input("Carrera: ")
        return carnet, nombre, carrera

    def pedir_curso(self):
        sigla = input("Sigla: ")
        nombre = input("Nombre del curso: ")

        try:
            creditos = int(input("Créditos: "))
        except ValueError:
            print("Dato inválido")
            return None
        return sigla, nombre, creditos

    def pedir_matricula(self):
        try:
            indice_estudiante = int(input("Indice del estudiante: "))
            indice_curso = int(input("Indice del curso: "))
        except ValueError:
            print("Dato inválido")
            return None
        return indice_estudiante, indice_curso

    def mostrar_lista(self, lista):
        if not lista:
            print("No hay datos")
        else:
            for i, obj in enumerate(lista):
                print(i+1, "-", obj)