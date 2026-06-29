"""
Módulo del modelo relacionado con los métodos de pago
Aquí se define:
-Una abstracción general para métodos de pago
-Implementaciones concretas de cada tipo de pago

Relación con SOLID
1. RSP(Responsabilidad única)
-Cada clase concreta tiene una única responsabilidad:
    ejecutar un tipo específico de pago.


2. OCP(Abierto y cerrado)
El sistema está abierto a extensión:
Se pueden agregar nuevos métodos de pago creando nuevas clases
sin modificar las existentes

3. LSP(Sustitución de Liskov)
    Cualquier clase hija puede sustituir a Metodo_pago sin romper
    el comportamiento esperado del sistema.

4. ISP(Segregación de interface)
    La abstracción Metodo_pago define una interface pequeña y especifica:
    Solo exige implementar el método pagar


5. DIP(Inversión de dependencia)
    El resto del depende de la abstracción método pago,
    no directamente de pago_tarjeta, pago_efectivo, etc.
"""
#---------------------------------------------------------------
from abc import ABC, abstractmethod


class MetodoPago(ABC):
    """
    Clase abstracta que representa el contrato general
    de cualquier método de pago

    SOLID:
    Isp: Interface pequeña y específica
    DIP: El sistema de esta abstracción
    """

    @abstractmethod
    def pagar(self, monto: float):
        """
        :Procesa un pago y retorna un mensaje descriptivo
        :return: mensaje del resultado del pago
        """
        pass


#---------------------------------------------------------------
class PagoTarjeta(MetodoPago):
    """
    Implementación concreta del pago con tarjeta.

    SOLID:
    -SRP: Esta clase solo permite
    -LSP: Puede usarse donde se espere un MetodoPago,
    """

    def pagar(self, monto: float) -> str:
        return f"Pagando{monto:.2f} con tarjeta"


#---------------------------------------------------------------
class PagoEfectivo(MetodoPago):
    """
    Implementación concreta del pago con tarjeta.

    SOLID:
    -SRP: Esta clase solo permite
    -LSP: Puede usarse donde se espere un MetodoPago,
    """

    def pagar(self, monto: float) -> str:
        return f"Pagando{monto:.2f} en efectivo"


#---------------------------------------------------------------
class PagoTrasferencia(MetodoPago):
    """
    Implementación concreta del pago con tarjeta.

    SOLID:
    -SRP: Esta clase solo permite
    -LSP: Puede usarse donde se espere un MetodoPago,
    """

    def pagar(self, monto: float) -> str:
        return f"Pagando{monto:.2f} por trasferencia"
