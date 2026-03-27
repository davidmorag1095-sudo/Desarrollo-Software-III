"""
Módulo del controlador del sistema de pagos
Responsabilidad:
-Recibir la opción seleccionada
-Determinar qué método de pago usar
-Validar el monto
-Ejecutar el pago


Relación con SOLID


1. SRP
    -El controlador coordina el flujo del pago.
    -No imprime menús ni implementa directamente
    el algoritmo de cada pago

2. OCP
    -El diseño del sistema permite
    agregar nuevas clases de pago
    -En esta versión simple de MVC,
     si se agrega una opción en el menú.

3. LSP
    -El controlador trabaja con objetos
     que cumplen el contrato MetodoPago

4. DIP
    -El controlador depende de la abstracción MetodoPago
    a través del uso de las clases del modelo, do de la implementación
    interna de cada pago.
"""
from ArquitecturavsDiseñoSOLID.PracticaGuiada3.solid.model.metodo_pago import MetodoPago, PagoTarjeta, PagoEfectivo, \
    PagoTrasferencia


class ProcesadorPago:
    """

    Controlador principal del flujo de pagos
    """

    def crea_metodo_pago(self, opcion:str) -> MetodoPago:
        """
        Crea y retorna el método de pago correspondiente
        según la opción elegida por el usuario.

        :param opción: opción elegida por el usuario.
        :return: instancia de una clase que hereda de MetodoPago.
        :raise ValueError: Si la opción es inválida

        SOLID
        -LSP: Retorna cualquier subtipo de MetodoPago.
        -DIP: El método devuelve la abstracción MetodoPago.
        """
        if opcion == "1":
            return PagoTarjeta()
        if opcion == "2":
            return PagoEfectivo()
        if opcion == "3":
            return PagoTrasferencia()

        raise ValueError("Opción invalida. Debe seleccionar una opción del 1 al 4")
