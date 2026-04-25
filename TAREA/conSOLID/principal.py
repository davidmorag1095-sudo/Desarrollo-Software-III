from TAREA.conSOLID.Controller.gestor_notificaciones import GestorNotificaciones
from TAREA.conSOLID.Model.mensaje import Mensaje
from TAREA.conSOLID.View.consola import Consola


class Main:
    # Constructor
    def __init__(self):
        self.consolaSistema = Consola()
        self.gestorSistema = GestorNotificaciones()

    # Método iniciar sistema
    def iniciarSistema(self):
        while True:
            self.consolaSistema.mostrarMenu()
            opcionSeleccionada = self.consolaSistema.solicitarOpcion()

            if opcionSeleccionada == "5":
                self.consolaSistema.mostrarSalida()
                break

            mensajeEscrito = self.consolaSistema.solicitarMensaje()
            mensajeNuevo = Mensaje(mensajeEscrito)

            resultadoEnvio = self.gestorSistema.enviar_notificacion(opcionSeleccionada, mensajeNuevo)
            self.consolaSistema.mostrarResultado(resultadoEnvio)


sistemaPrincipal = Main()
sistemaPrincipal.iniciarSistema()

"""Pude agregar la opcion telegram con mayor facilidad simplemente se crea la clase
 en model en controller se agregar un elif View se agrega la opción y quedo listo"""