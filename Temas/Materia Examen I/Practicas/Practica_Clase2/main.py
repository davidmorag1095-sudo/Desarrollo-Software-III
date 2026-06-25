from Practicas.Practica_Clase2.Controller.controlador import Controlador
from Practicas.Practica_Clase2.View.vista import Vista

def main():
    controlador=Controlador()
    vista=Vista()

    while True:
        opcion =vista.menu()

        if opcion == 1:
            datos = vista.pedir_estudiante()
            controlador.agregar_estudiante(*datos)
        elif opcion == 2:
            datos = vista.pedir_libro()
            controlador.agregar_libro(*datos)
        elif opcion == 3:
            datos = vista.pedir_prestamo()
            controlador.agregar_prestamo(*datos)
        elif opcion == 4:
            vista.mostrar_estudiantes(controlador.consultar_estudiantes())
        elif opcion == 5:
            vista.mostrar_Libros(controlador.consultar_libros())
        elif opcion == 6:
            vista.mostrar_Prestamos(controlador.consultar_prestamos())
        elif opcion == 7:
            vista.mostrar_categorias(controlador.consultar_categorias())
        elif opcion == 8:
            print("Fin del programa")
            break


if __name__ == "__main__":
    main()
