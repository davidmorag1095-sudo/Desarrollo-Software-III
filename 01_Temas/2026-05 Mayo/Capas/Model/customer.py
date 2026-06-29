class Customer:
    """
    Representa el cliente
    """

    """
    Constructor de la clase, recibé el identificador, el nombre y el telefono del cliente
    """

    def __init__(self, identifier:str, name:str, phone:str):
        self.identifier = identifier
        self.name = name
        self.phone = phone
    """
    Convierte el objeto en un diccionario
    Esto es útil para guardarlo en un JSON
    """

    def to_dict(self)->dict:
        return {
            "Identifier": self.identifier,
            "Name": self.name,
            "Phone": self.phone
        }

    """
    Permite reconstruir un objeto cliente,
    a partir de un diccionario leído desde un JSON
    """

    @classmethod
    def from_dict(cls,data:dict):
        return cls(
            data["Identifier"],
            data["Name"],
            data["Phone"])

    #Define cómo se mostrará eñ pbketp ciamdp se o,prima
    def __str__(self)-> str:
        return f"ID: {self.identifier} | Nombre: {self.name} | Telefono: {self.phone}"