class Matricula:
    def __init__(self, numero, estudiante_id, curso_codigo, periodo):
        self.numero = numero
        self.estudiante_id = estudiante_id
        self.curso_codigo = curso_codigo
        self.periodo = periodo

    def to_dict(self):
        return {
            "numero": self.numero,
            "estudiante_id": self.estudiante_id,
            "curso_codigo": self.curso_codigo,
            "periodo": self.periodo
        }