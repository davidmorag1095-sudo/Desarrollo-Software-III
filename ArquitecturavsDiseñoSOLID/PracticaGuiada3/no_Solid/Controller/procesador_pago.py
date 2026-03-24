"""
Controlador con diseño deficiente

Problemas:
El controlador depende completamente de una clase concreta: Sistema_pagos
No usa abstracciones
El controlador aporta poco valor arquitectónico porque casi toda la lógica
está dentro del modelo


Violación:
-DIP: Depende directamente de Sistema_pagos, una implementación concreta

"""
from ArquitecturavsDiseñoSOLID.PracticaGuiada3.no_Solid.Model.metodo_pago import Sistemas_pagos


class ControladorPagos:
    """
    Controlador que delega casi todo en una clase del modelo
    """

    def __init__(self):
        """
            Violación de DIP:
            Se instáncia directamente una clase concreta
        """
        self.sistema = Sistemas_pagos()

    def iniciar(self):
        """
        Ejecuta el sistema en bucle
        Aunque aquí hay ciclo funcional, el diseño general sigue siendo malo
        pues todo se apoya en una clase demasiado acoplada.
        """
        while True:
            try:
                self.sistema.mostrar_menu()
                opcion = self.sistema.solicitar_opcion()

                if opcion == "4":
                    print("\n Saliendo del sistema")
                    self.sistema.mostrar_historial()
                    break
                monto = self.sistema.solicitar_monto()
                resultado = self.sistema.procesar_pago(opcion, monto)
                print("Resultado", resultado)

            except ValueError as error:
                print("Error: ", error)

            except Exception as error:
                print("Ocurrió un error inesperado: ", error)

