"""
Archivo: main.py

Este es el punto de entrada del programa.

Para ejecutar el sistema desde PyCharm:
1. Abrir este archivo.
2. Dar clic derecho.
3. Seleccionar Run 'main'.
"""

from controller.estudiante_controller import EstudianteController


def main():
    """
    Función principal del programa.

    Crea el controlador y muestra el menú del sistema.
    """

    controller = EstudianteController()
    controller.mostrar_menu()


# Esta condición permite que el programa inicie solo cuando se ejecuta este archivo.
# Si este archivo fuera importado desde otro módulo, main() no se ejecutaría automáticamente.
if __name__ == "__main__":
    main()
