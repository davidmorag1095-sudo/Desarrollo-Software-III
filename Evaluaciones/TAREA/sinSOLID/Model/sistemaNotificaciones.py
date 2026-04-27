class SistemaNotificaciones:
    # Constructor
    def __init__(self):
        self.historial = []

    # Método mostrar menú
    def mostrarMenu(self):
        print("===== SISTEMA DE NOTIFICACIONES =====")
        print("1. Enviar Email")
        print("2. Enviar SMS")
        print("3. Enviar WhatsApp")
        print("4. Salir")

    # Método solicitar opción
    def solicitarOpcion(self):
        opcionSeleccionada = input("Seleccione una opción: ")
        return opcionSeleccionada

    # Método solicitar mensaje
    def solicitarMensaje(self):
        mensajeEscrito = input("Ingrese el mensaje: ")
        return mensajeEscrito

    # Método validar mensaje
    def validarMensaje(self, mensajeEscrito):
        if mensajeEscrito == "":
            print("El mensaje no puede estar vacío")
            return False
        return True

    # Método procesar notificación
    def procesarNotificacion(self, opcionSeleccionada, mensajeEscrito):
        resultadoEnvio = ""

        if opcionSeleccionada == "1":
            resultadoEnvio = "Email enviado: " + mensajeEscrito
            self.historial.append(resultadoEnvio)

        elif opcionSeleccionada == "2":
            resultadoEnvio = "SMS enviado: " + mensajeEscrito
            self.historial.append(resultadoEnvio)

        elif opcionSeleccionada == "3":
            resultadoEnvio = "WhatsApp enviado: " + mensajeEscrito
            self.historial.append(resultadoEnvio)

        else:
            resultadoEnvio = "Opción inválida"

        return resultadoEnvio

    # Método mostrar historial
    def mostrarHistorial(self):
        print("===== HISTORIAL DE NOTIFICACIONES =====")

        if len(self.historial) == 0:
            print("No hay notificaciones registradas")
        else:
            for notificacionRegistrada in self.historial:
                print(notificacionRegistrada)