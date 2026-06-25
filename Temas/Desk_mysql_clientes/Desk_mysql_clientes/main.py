"""
Archivo: main.py

Punto de entrada para ejecutar la versión de consola.
"""

from controller.cliente_controller import ClienteController


def main():
    controller = ClienteController()
    controller.mostrar_menu()


if __name__ == "__main__":
    main()
