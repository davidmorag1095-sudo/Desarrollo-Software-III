class Usos:
    def __init__(self, codigo, iD_Jugador,codigo_VideoJuego, fecha, cantidad_Licencias):
        self.codigo = codigo
        self.iD_Jugador = iD_Jugador
        self.codigo_VideoJuego = codigo_VideoJuego
        self.fecha = fecha
        self.cantidad_Licencias = cantidad_Licencias

    def __str__(self) -> str:
        return f'{self.codigo} {self.iD_Jugador} {self.codigo_VideoJuego} {self.fecha} {self.cantidad_Licencias}'

