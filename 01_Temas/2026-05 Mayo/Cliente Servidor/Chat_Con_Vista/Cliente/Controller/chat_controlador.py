class ChatControlador:
    def __init__(self,vista,conexion,nombre):
        self.vista=vista
        self.conexion=conexion
        self.nombre=nombre

        self.vista.on_enviar(self.enviar)
        self.conexion.iniciar(self.recibir)