"""
Módulo de validaciones del dominio

Responsabilidad:
-Validar reglas simples relacionadas con el monto

Relaciones con SOLID;
-SRP: este módulo solo contiene validaciones.
      No mezcla lógica de negocío con presentación
      ni con control
"""

def validar_monto(monto: float):
    """
    Valída que el monto sea mayor que cero

    :param monto:
    :raise Value Error: Si el monto es menor o igual que cero
    """
    if monto <= 0:
        raise ValueError("El monto debe ser mayor que 0")