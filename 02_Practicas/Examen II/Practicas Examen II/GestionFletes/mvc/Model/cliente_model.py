class Cliente:
    def __init__(self, id:str, nombre:str, telefono:int)->None:
        self.id = id
        self.nombre = nombre
        self.telefono = telefono

    # ----------------------------------------------------------------------------------------
    def get_id(self):
        return self.id

    # ----------------------------------------------------------------------------------------
    def to_dict(self)->dict:
        return {
            'id': self.id,
            'nombre': self.nombre,
            'telefono': self.telefono
        }

    # ----------------------------------------------------------------------------------------
    @classmethod
    def from_dict(cls, dato)->Cliente:
        return cls(
            id=dato['id'],
            nombre=dato['nombre'],
            telefono=dato['telefono']
        )

    # ----------------------------------------------------------------------------------------
    def __str__(self)->str:
            return f'\n{self.id} - {self.nombre} - {self.telefono} '
