class ClienteModel:
    def __init__(self, id, nombre, telefono):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"\n ID: {self.id} Nombre: {self.nombre} Telefono: {self.telefono}"

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "telefono": self.telefono
        }

    @classmethod
    def from_dict(cls, dicto):
        return cls(
            id = dicto["id"],
            nombre = dicto["nombre"],
            telefono = dicto["telefono"]
        )

    def get_id(self):
        return self.id

