class Flete:
    def __init__(self, numeroFlete, destino, monto, clienteAsociado):
        self.numeroFlete = numeroFlete
        self.destino = destino
        self.monto = monto
        self.clienteAsociado = clienteAsociado
    #---------------------------------------------------
    #Set/Get
    def setNumeroFlete(self, numeroFlete):
        self.numeroFlete = numeroFlete

    def setDestino(self, destino):
        self.destino = destino

    def setMonto(self, monto):
        self.monto = monto

    def setClienteAsociado(self, clienteAsociado):
        self.clienteAsociado = clienteAsociado
    # ---------------------------------------------------
    def getNumeroFlete(self):
        return self.numeroFlete

    def getDestion(self):
        return self.destino

    def getMonto(self):
        return self.monto

    def getClienteAsociado(self):
        return self.clienteAsociado
    # ---------------------------------------------------
    def __str__(self):
        return (
            f"Flete: [{self.numeroFlete}]"
            f"Destino: {self.destino}]"
            f"Colones: {self.monto}]"
            f"Cliente: {self.clienteAsociado}]"
        )
