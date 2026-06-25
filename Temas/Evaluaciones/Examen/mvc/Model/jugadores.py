class Jugador:
    def __init__(self, iD, nombre, correo, pais) -> None:
        self.id = iD
        self.nombre = nombre
        self.correo = correo
        self.pais = pais

    def __str__(self) -> str:
        return f'{self.id} {self.nombre} {self.correo} {self.pais}'



