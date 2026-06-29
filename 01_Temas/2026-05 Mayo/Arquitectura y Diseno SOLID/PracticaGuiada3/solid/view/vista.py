"""
Módulo de la vista del sistema

Responsabilidad:
- Mostrar información por consola
- Solicitar datos al usuario
- Presentar resultados y errores

Relación con SOLID
    SRP: La vista solo se encarga de interactuar con el usuario.
    No contiene lófica de negocio o validación
"""


class VistaConsola:
    """
    Clase de interfaz por consola
    """

    @staticmethod
    def mostrar_menu() -> None:
        """
        Muestra el menú principal del sistema
        """
        print("===SISTEMA DE PAGOS===")
        print("1.Pago con tarjeta")
        print("2.Pago con efectivo")
        print("3.Pago por transferencia")
        print("4.Salir")

    @staticmethod
    def solicitar_opcion() -> str:
        """
        Solicita al usuario una opción del menú
        :return: Opción ingresada por el usuario
        """
        return input('Seleccione una opción: ')

    @staticmethod
    def solicitar_monto() -> float:
        """
        Solicita al usuario el monto del pago
        :return: Monto ingresado por el usuario convertido a float
        """
        return float(input('Ingrese el monto del pago: '))

    @staticmethod
    def mostrar_resultado(mensaje: str) -> None:
        """
        Muestra mensaje de resultado
        :param mensaje: Mensaje a mostrar
        """
        print(f'\nResultado {mensaje}')

    @staticmethod
    def mostrar_error(error: str) -> None:
        """
        Muestra mensaje de error
        :param error: Descripción del error
        """
        print(f'\n[ERROR] {error}')