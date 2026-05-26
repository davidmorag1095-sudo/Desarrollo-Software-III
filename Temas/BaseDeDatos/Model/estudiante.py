class Estudiante:
    def __init__(self, id_estudiante = None, nombre = "", correo = "", carrera= ""):
        self.id_estudiante = id_estudiante
        self.nombre = nombre
        self.correo = correo
        self.carrera = carrera

    def __str__(self):
        return (f"Id: {self.id_estudiante} Nombre: {self.nombre}"
                f"Correo: {self.correo} Carrera{self.carrera}")
