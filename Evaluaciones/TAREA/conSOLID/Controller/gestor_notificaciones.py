from TAREA.conSOLID.Model.notificador import NotificadorEmail, NotificadorSMS, NotificadorWhatsApp, NotificadorTelegram

class GestorNotificaciones:

    def __init__(self):
        self.notificador = None

    def seleccionar_notificador(self,opcion):
        if opcion =="1":
            self.notificador=NotificadorEmail()
        elif opcion=="2":
            self.notificador=NotificadorSMS()
        elif opcion=="3":
            self.notificador=NotificadorWhatsApp()

        elif opcion=="4":
            self.notificador=NotificadorTelegram()
        else:
            self.notificador=None


    def enviar_notificacion(self,opcion, mensaje):
        self.seleccionar_notificador(opcion)
        if self.notificador is None:
            return "No se pudo seleccionar un canal valido"
        return self.notificador.enviar(mensaje)

