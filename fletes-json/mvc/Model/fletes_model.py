class Fletes:
    def __init__(self, id_flete:str, id_cliente:str, ciudad:str, destino:str, peso:int)-> None:
        self.id_flete = id_flete
        self.id_cliente = id_cliente
        self.ciudad = ciudad
        self.destino = destino
        self.peso = peso

    def get_id(self):
            return self.id_flete


    def to_dict(self)->dict:
        return {
            'flete': self.id_flete,
            'cliente': self.id_cliente,
            'ciudad': self.ciudad,
            'destino': self.destino,
            'peso': self.peso
        }
    
    @classmethod
    def from_dict(cls, data)->Fletes:
        return cls(
            id_flete=data['flete'],
            id_cliente=data['cliente'],
            ciudad=data['ciudad'],
            destino=data['destino'],
            peso=data['peso']
        )
    

    def mostrar_dato(self)->str:
        return f'\n{self.id_flete} - {self.id_cliente} - {self.ciudad} - {self.destino} - {self.peso}kg '


# Registro de fletes
# El sistema debe permitir registrar nuevos fletes asociados a clientes existentes.
# Para registrar un flete se deben solicitar los siguientes datos:
# ●	número de flete
# ●	identificador del cliente
# ●	ciudad de origen
# ●	ciudad de destino
# ●	peso de la carga
