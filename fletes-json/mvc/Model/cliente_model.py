class Cliente:
    def __init__(self, id:str, nombre:str, telefono:int)->None:
        self.id = id
        self.nombre = nombre
        self.telefono = telefono

    def get_id(self):
        return self.id

    def to_dict(self)->dict:
        return {
            'id': self.id,
            'nombre': self.nombre,
            'telefono': self.telefono
        }
    
    @classmethod
    def from_dict(cls, dato)->Cliente:
        return cls(
            id=dato['id'],
            nombre=dato['nombre'],
            telefono=dato['telefono']
        )

    def __str__(self)->str:
            return f'\n{self.id} - {self.nombre} - {self.telefono} '

# Registro de clientes
# El sistema debe permitir registrar nuevos clientes. Para registrar un cliente se deben solicitar los siguientes datos:
# ●	identificador del cliente
# ●	nombre completo
# ●	número de teléfono
# El identificador del cliente debe ser único dentro del sistema. Si el usuario intenta registrar un cliente con un identificador que ya existe, el sistema debe impedir la operación y mostrar un mensaje de error.
# Una vez registrado el cliente, su información debe almacenarse de manera persistente en un archivo JSON destinado exclusivamente al almacenamiento de clientes.
