class Estudiante:
    def __init__(self, carnet, nombre, carrera):
        self.carnet = carnet
        self.nombre = nombre
        self.carrera = carrera

    def motrarInfo(self):
        return f"Carnet: {self.carnet} \n Nombre: {self.nombre} \n Carrera:{self.carrera} "