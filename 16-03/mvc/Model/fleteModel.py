class Flete:
    def __init__(self, numero, destino, monto, cliente):
        self.numero = numero
        self.destino = destino
        self.monto = monto
        self.cliente = cliente

    def __str__(self):
        return (
            f"Flete[{self.numero}] "
            f"Destino:{self.destino} "
            f"Colones: {self.monto} "
            f"Cliente:{self.cliente.nombre}"
        )