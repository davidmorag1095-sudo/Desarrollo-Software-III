class Cliente:
    def __init__(self, codigo, nombre, telefono):
        self.codigo = codigo
        self.nombre = nombre
        self.telefono = telefono

    #---------------------------------------------------
    #Set/Get
    def setCodigo(self, codigo):
        self.codigo = codigo

    def setNombre(self, nombre):
        self.nombre = nombre

    def setTelefono(self, telefono):
        self.telefono = telefono

    #---------------------------------------------------
    def getCodigo(self):
        return self.codigo

    def getNombre(self):
        return self.nombre

    def getTelefono(self):
        return self.telefono

    #---------------------------------------------------
    def __str__(self):
        return f"Cliente: {self.codigo}]| {self.nombre}, {self.telefono}"