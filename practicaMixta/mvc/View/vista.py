class Vista:

    def menu(self):
        print("---MENU PRINCIPAL---")
        print("1.Agregar estudiante")
        print("2.Consultar estudiante")
        print("3.Modifcar estudiante")
        print("4.Eliminar estudiante")
        print("5.Agregar matricula")
        print("6.Consultar matricula")
        print("7.Modificar matricula")
        print("8.Eliminar matricula")
        print("9.Salir")
        return int(input("Digite una opcion: "))


    def pedir_datos_Estudiantes(self):
        carnet