class Usuario:
    def __init__(self, id, Nombre):
        self.id = id
        self.Nombre = Nombre

    #----------------------------------------------------------------
    #Metodo To String()
    def __str__(self):
        return f"{self.id} | {self.Nombre}"
    #----------------------------------------------------------------