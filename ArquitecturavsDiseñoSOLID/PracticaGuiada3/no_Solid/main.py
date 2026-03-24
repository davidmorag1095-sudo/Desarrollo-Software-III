"""

Archivo principal del sistema

Este proyecto se ha diseñado intencionalmente incorrecto
para mostrar violaciones de los principios SOLID.

Problemas:
-El flujo general depende de clases mal acopladas.
-Aunque el main es simple, el resto del sistema concentra
demasiadas responsabilidades
"""

from ArquitecturavsDiseñoSOLID.PracticaGuiada3.no_Solid.Controller.procesador_pago import ControladorPagos


def main():
    controlador = ControladorPagos()
    controlador.iniciar()

if __name__ == "__main__":
    main()