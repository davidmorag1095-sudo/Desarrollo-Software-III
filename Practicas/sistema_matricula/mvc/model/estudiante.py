class Estudiante:
    def __init__(self, carnet, nombre, carrera):
        self.carnet = carnet
        self.nombre = nombre
        self.carrera = carrera

    def __str__(self):
        return f"Carnet del estudiante: {self.carnet} | nombre: {self.nombre} | carrera: {self.carrera}"