class Matricula:
    def __init__(self, curso, estudiante):
        self.curso = curso
        self.estudiante = estudiante

    def __str__(self):
        return f"Matricula -> Estudiante: {self.estudiante.nombre} | Curso: {self.curso.nombre}"