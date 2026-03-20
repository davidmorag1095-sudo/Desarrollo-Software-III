from Practicas.sistema_matricula.mvc.controller.controlador import Controlador
from Practicas.sistema_matricula.mvc.view.vista import Vista

def main():

    controlador = Controlador()
    vista = Vista()

    while True:
        opcion = vista.menu()

        if opcion == "1":
            datos = vista.pedir_estudiante()
            controlador.agregar_estudiante(*datos)

        elif opcion == "2":
            datos = vista.pedir_curso()
            if datos:
                controlador.agregar_curso(*datos)

        elif opcion == "3":

            print("\nEstudiantes disponibles")
            vista.mostrar_lista(controlador.consultar_estudiantes())

            print("\nCursos disponibles")
            vista.mostrar_lista(controlador.consultar_cursos())

            datos = vista.pedir_matricula()

            if datos:
                controlador.matricular(*datos)

        elif opcion == "4":
            vista.mostrar_lista(controlador.consultar_estudiantes())

        elif opcion == "5":
            vista.mostrar_lista(controlador.consultar_cursos())

        elif opcion == "6":
            vista.mostrar_lista(controlador.consultar_matriculas())

        elif opcion == "7":
            print("Saliendo...")
            break


if __name__ == "__main__":
    main()