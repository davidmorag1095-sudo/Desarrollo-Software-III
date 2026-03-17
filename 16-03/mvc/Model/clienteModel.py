class Cliente:
    def __init__(self, codigo, nombre, telefono):
        self.codigo = codigo
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"[{self.codigo}] {self.nombre} - Tel: {self.telefono}"