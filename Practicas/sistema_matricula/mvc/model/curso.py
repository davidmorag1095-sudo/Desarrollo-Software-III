class Curso:
    def __init__(self, sigla, nombre, creditos):
        self.sigla = sigla
        self.nombre = nombre
        self.creditos = creditos

    def __str__(self):
        return f"Sigla del curso: {self.sigla} | nombre: {self.nombre} | creditos: {self.creditos}"