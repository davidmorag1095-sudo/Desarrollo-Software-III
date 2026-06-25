from GestionBiblioteca.config.database import init_db
from GestionBiblioteca.controller.autor_controller import AutorController
from GestionBiblioteca.controller.libro_controller import LibroController

from GestionBiblioteca.entity.autor import AutorORM
from GestionBiblioteca.entity.libro import LibroORM


def menu():
    print("\n===================================")
    print(" SISTEMA DE GESTION DE BIBLIOTECA")
    print("===================================")
    print("1. Gestion de autores")
    print("2. Gestion de libros")
    print("3. Reporte autores por nacionalidad")
    print("4. Salir")


def main():
    init_db()

    autor_controller = AutorController()
    libro_controller = LibroController()

    opcion = ""
    while opcion != "4":
        menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            autor_controller.mostrar_menu()
        elif opcion == "2":
            libro_controller.mostrar_menu()
        elif opcion == "3":
            autor_controller.reporte_por_nacionalidad()
        elif opcion == "4":
            print("Saliendo del sistema")
        else:
            print("Debe seleccionar una opcion valida")


if __name__ == "__main__":
    main()
