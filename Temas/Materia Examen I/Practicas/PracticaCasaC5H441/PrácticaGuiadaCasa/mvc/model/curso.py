class Curso:
    def __init__(self, codigo, nombre, creditos):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "creditos": self.creditos
        }