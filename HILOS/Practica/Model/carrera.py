"""Model principal del juego guarda:
-La distancia
-La lista de corredores
-El ganador
-El ganador"""

class Carrera:
    def __init__(self,meta:int =650):
        self.meta=meta
        self.corredores=[]
        self.ganador=None
        self.en_curso=False

    def agregar_corredor(self,corredor):
        """Agrega un corredor a la carrera"""
        self.corredores.append(corredor)

    def reiniciar(self):
        """Reinicia el estado de la carrera para una nueva partida"""
        self.ganador=None
        self.en_curso=False
        for corredor in self.corredores:
            corredor.reiniciar()