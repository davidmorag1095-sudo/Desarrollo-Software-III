class FleteModel:
    def __init__(self,numero_flete, nombre_cliente, ciudad_origen, ciudad_destino, peso_transportado, monto_flete):
        self.numero_flete = numero_flete
        self.nombre_cliente = nombre_cliente
        self.ciudad_origen = ciudad_origen
        self.ciudad_destino = ciudad_destino
        self.peso_transportado = peso_transportado
        self.monto_flete = monto_flete

    def to_dict(self):
        return {
            "numero_flete": self.numero_flete,
            "nombre_cliente": self.nombre_cliente,
            "ciudad_origen": self.ciudad_origen,
            "ciudad_destino": self.ciudad_destino,
            "peso_transportado": self.peso_transportado,
            "monto_flete": self.monto_flete
        }

    @classmethod
    def from_dict(cls, dicto):
        return cls(
            numero_flete = dicto["numero_flete"],
            nombre_cliente = dicto["nombre_cliente"],
            ciudad_origen = dicto["ciudad_origen"],
            ciudad_destino = dicto["ciudad_destino"],
            peso_transportado = dicto["peso_transportado"],
            monto_flete = dicto["monto_flete"]
        )

    def get_id(self):
        return self.numero_flete