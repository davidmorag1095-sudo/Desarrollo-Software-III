class Estudiante:
    def __init__(self, identificador, nombre, carrera):
        self.identificador = identificador
        self.nombre = nombre
        self.carrera = carrera

    def to_dict(self):
        return {
            "identificador": self.identificador,
            "nombre": self.nombre,
            "carrera": self.carrera
        }