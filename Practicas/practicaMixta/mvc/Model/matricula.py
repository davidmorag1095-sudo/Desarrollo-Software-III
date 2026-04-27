class Matricula:
    def __init__(self, numero_matricula, curso, creditos, carnet_Estudiante):
        self.numero_matricula = numero_matricula
        self.curso = curso
        self.creditos = creditos
        self.carnet_Estudiante = carnet_Estudiante

    def __str__(self):
        return f"Numero Matricula: {self.numero_matricula}, Curso: {self.curso}, Creditos: {self.creditos}, Estudiante: [{self.carnet_Estudiante}]"