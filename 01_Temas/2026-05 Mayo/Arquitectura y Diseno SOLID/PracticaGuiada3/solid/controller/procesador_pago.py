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
from ArquitecturavsDiseñoSOLID.PracticaGuiada3.solid.model.validaciones import validar_monto


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

    def procesar_pago(self, opcion: str, monto: float) -> str:
        """
        Procesa el pago seleccionado por el usuario.


            :param opcion: opción del método de pago
            :param monto:  monto a pagar
            :return: mensaje resultante del pago

            flujo:
            1. Validar monto:
            2. Crear método pago
            3. Ejecutar mensaje resaltante

            SOLID:
            SRP: Coordina el proceso, no hace UI ni define
            algoritmos concretos

            DIP: Usa el contrato MetodoPago
        """
        validar_monto(monto)
        metodo_pago = self.crea_metodo_pago(opcion)
        return metodo_pago.pagar(monto)
