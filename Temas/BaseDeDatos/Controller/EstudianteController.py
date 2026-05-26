"""
El controlador cordina la interacción entre
el usuario y el servicio
En este ejemplo el controller trabaja con un menú por consola
Más adelante, esta misma clase podría conectarse
 con una interfaz gráfica
"""
from Temas.BaseDeDatos.Service.EstudianteService import EstudianteService


class EstudianteController:
    def __init__(self):
        self.service=EstudianteService()

    def mostrar_menu(self):
        opcion=""

        while (opcion != "6"):
            print("\n================================")
            print("SISTEMA DE GESTION DE ESTUDIANTES")
            print("\n================================")
            print("1. Registrar estudiante")
            print("2. Consultar estudiante")
            print("3. Buscar estudiante")
            print("4. Actualizar estudiante")
            print("5. Eliminar estudiante")
            print("6. Salir")

            opcion = input("Seleccione una opcion")

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
                print("Saliendo del sistema....")

            else:
                print("Opción inválida, intente con valores menores que 1 y 6")
