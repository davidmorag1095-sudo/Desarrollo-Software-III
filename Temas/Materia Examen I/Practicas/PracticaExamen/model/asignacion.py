class Asignacion:
    def __init__(self, codigo: str, beneficiario, recurso, cantidad: int,
                 fecha: str, responsable: str) -> None:
        if cantidad <= 0:
            raise ValueError("Cantidad debe ser mayor a 0")
        self.codigo = codigo
        self.beneficiario = beneficiario
        self.recurso = recurso
        self.cantidad = cantidad
        self.fecha = fecha
        self.responsable = responsable

    def costo_total(self) -> float:
        return self.cantidad * self.recurso.costo

    def __repr__(self) -> str:
        return (f"Asignacion(codigo={self.codigo!r}, beneficiario={self.beneficiario!r}, "
                f"recurso={self.recurso!r}, cantidad={self.cantidad!r}, "
                f"fecha={self.fecha!r}, responsable={self.responsable!r})")