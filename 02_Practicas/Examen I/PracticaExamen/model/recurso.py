class Recurso:
    def __init__(self,codigo,nombre,categoria,cantidad,costo):
        if cantidad <0:
            raise ValueError("Cantidad no puede ser negativa")
        if costo<=0:
            raise ValueError("Costo debe ser positivo")

        self.codigo=codigo
        self.nombre=nombre
        self.categoria=categoria
        self.cantidad=cantidad
        self.costo=costo



