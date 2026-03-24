
"""Clase con mal diseño intencionalmente

Este archivo viola multiples principios solid

1. SRP(Responsabilidad única)
La clase tiene muchas responsabilidades, entre ellas:
    muestra mensajes
    valida datos
    procesa pagos
    decide qué tipo de pagos usar
    genera historial


2. OCP(Cerrado a modificaciones, abierto a extensión)
Cada vez que se agrega un nuevo método de pago,
hay que modificar el método procesar_pago()

3. ISP(Segregación de interfaces)
No existen interfaces pequeñas ni especializadas

4. DIP(Inyección de dependencias)
La clase depende directamente de detalles concretos
no de abstracciones

También viola:
DRY: Repite lógica y mensajes
kiss: La clase hace demasiado
Demeter: Mezcla responsabilidades y accede a demasiados detalles
"""

