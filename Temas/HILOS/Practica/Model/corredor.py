"""
Modelo que representa a un corredor dentro del juego
Guarda su nombre, color y posición actual
"""


class Corredor:
    def __init__(self, nombre: str, color:str):
        self.nombre = nombre
        self.color = color
        self.posicion = 0

    def reiniciar(self):
        """Vuelve la posicion del corredor a cero"""
        self.posicion = 0
