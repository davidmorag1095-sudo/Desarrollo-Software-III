from abc import ABC, abstractmethod


class Notificador(ABC):
    # Método abstracto enviar
    @abstractmethod
    def enviar(self, mensaje):
        pass

class NotificadorEmail(Notificador):
    def enviar(self, mensaje):
        return "Email enviado: " + mensaje.mostrarDatos()


class NotificadorSMS(Notificador):
    def enviar(self, mensaje):
        return "SMS enviado: " + mensaje.mostrarDatos()


class NotificadorWhatsApp(Notificador):
    def enviar(self, mensaje):
        return "WhatsApp enviado: " + mensaje.mostrarDatos()

#Agrego una clase extra sin necesidad de modificar codigo(aplicando los principios del SOLID)
class NotificadorTelegram(Notificador):
    def enviar(self, mensaje):
        return "Telegram enviado: " + mensaje.mostrarDatos()