class Consola:
    # Mostrar menú
    def mostrarMenu(self):
        print("===== SISTEMA DE NOTIFICACIONES =====")
        print("1. Enviar Email")
        print("2. Enviar SMS")
        print("3. Enviar WhatsApp")
        print("4. Enviar Telegram")
        print("5. Salir")

    # Solicitar opción
    def solicitarOpcion(self):
        return input("Seleccione una opción: ")

    # Solicitar mensaje
    def solicitarMensaje(self):
        return input("Ingrese el mensaje: ")

    # Mostrar resultado
    def mostrarResultado(self, resultadoEnvio):
        print("Resultado:", resultadoEnvio)

    # Mostrar salida
    def mostrarSalida(self):
        print("Saliendo del sistema...")