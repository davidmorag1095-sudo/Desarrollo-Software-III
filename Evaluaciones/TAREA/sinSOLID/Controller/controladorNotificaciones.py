from TAREA.sinSOLID.Model.sistemaNotificaciones import SistemaNotificaciones


class ControladorNotificaciones:
    # Constructor
    def __init__(self):
        self.sistema = SistemaNotificaciones()

    # Método iniciar sistema
    def iniciar(self):
        while True:
            try:
                self.sistema.mostrarMenu()
                opcion = self.sistema.solicitarOpcion()

                if opcion == "4":
                    print("\nSaliendo del sistema")
                    self.sistema.mostrarHistorial()
                    break

                mensaje = self.sistema.solicitarMensaje()

                if self.sistema.validarMensaje(mensaje):
                    resultado = self.sistema.procesarNotificacion(opcion, mensaje)
                    print("Resultado:", resultado)

            except ValueError as error:
                print("Error:", error)

            except Exception as error:
                print("Ocurrió un error inesperado:", error)