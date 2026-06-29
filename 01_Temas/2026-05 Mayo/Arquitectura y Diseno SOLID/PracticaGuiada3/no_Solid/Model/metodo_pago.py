
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


class Sistemas_pagos:
    """
    Clase monolítica que centraliza toda la lógica del sistema
    Este es un ejemplo de cómo no se debe diseñar el sistema
    """

    def __init__(self):
        """
        Guarda el historial y estado interno
        """
        self.historial = []

    def mostrar_menu(self):
        """
        Violación de SRP:
        Esta clase en el modelo no debe mostrar interfaz
        """
        print("\==== SISTEMA DE PAGOS")
        print("1. Pago con tarjeta")
        print("2. Pago con efectivo")
        print("3. Pago por transferencia")
        print("4. Salir")

    def solicitar_opcion(self):
        """
            Violación de SRP
            Desde el modelo no se deben pedir datos
        """
        return input("Seleccione una opción: ")

    def solicitar_monto(self):
        """
            Violación de SRP
            Desde el modelo no se deben manejar interacción
        """
        return float(input("Ingrese el monto a pagar: " ))

    def validar_monto(self, monto):
        """
            Violación de SRP
            La validación debe estar separada
        """
        if monto <= 0:
            raise ValueError("El monto debe ser mayor que cero")

    def procesar_pago(self, opcion, monto):
        """
        Método altamente acopado y poco extensible
        Violaciones:
            OCP: Para agregar un nuevo método de pago hay que modificar este método.
            DIP: Depende directamente de condicionales concretas
            DRY: Repite estructura lógica
        """
        self.validar_monto(monto)

        if opcion == "1":
            mensaje = f"Pagando {monto: .2f} con tarjeta"
            print(mensaje)
            self.historial.append(mensaje)
            return mensaje

        elif opcion == "2":
            mensaje = f"Pagando {monto: .2f} en efectivo"
            print(mensaje)
            self.historial.append(mensaje)
            return mensaje

        elif opcion == "3":
            mensaje = f"Pagando {monto: .2f} por transferencia"
            print(mensaje)
            self.historial.append(mensaje)
            return mensaje

        elif opcion == "4":
            return "Salir"
        else:
            raise ValueError("Opción inválida")

    def mostrar_historial(self):
        """
        Violación de SRP:
        Además de procesar pagos la clase también administra
        y muestra el historial
        """

        print("\n ======== HISTORIAL DE PAGOS ========")
        if len(self.historial) == 0:
            print("No hay pagos")
        else:
            for pago in self.historial:
                print(pago)




