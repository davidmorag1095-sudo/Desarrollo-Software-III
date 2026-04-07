class Freight:
    """
    Entidad del dominio que representa un flete
    """
    #Contructor flete
    #router es una tupla que contiene el origen
    # y el destino

    def __init__ (self,number:str, amount :float,customer_id:str,route: tuple, weight : float):
        self.number=number
        self.amount=amount
        self.customer_id=customer_id
        self.route=route
        self.weight=weight

    #convierte el objeto Freight en un diccionario para guardarlo en el JSON
    def to_dict(self):
        return {
            "number":self.number,
            "amount": self.amount,
            "customer_id": self.customer_id,
            "route": {
                "origin":self.route[0],
                "destination": self.route[1]
            },
            "weight":self.weight
        }
    #reconstruye un objeto Freight a partir de un diccionario
    @classmethod
    def from_dict(cls,data:dict):
        return cls(
            data["number"],
            data["amount"],
            data["customer_id"],
            (data["route"]["origin"],data["route"]["detination"]),
            data ["weight"]
        )