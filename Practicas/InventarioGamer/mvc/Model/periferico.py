class Periferico:
    def __init__(self, modelo:str, tipo:str, precio:float) -> None:
        self.modelo = modelo
        self.tipo = tipo
        self.precio = precio

    def to_dict(self) -> dict:
        return {
            'Modelo': self.modelo,
            'Tipo': self.tipo,
            'Precio': self.precio
        }

    def __str__(self) -> str:
        return f'Modelo: {self.modelo}, \nTipo: {self.tipo}, \nPrecio: {self.precio}'