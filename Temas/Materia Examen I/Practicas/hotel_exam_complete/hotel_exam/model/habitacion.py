from dataclasses import dataclass


@dataclass
class Habitacion:
    numero: str
    tipo: str
    piso: int
    precio: float
    disponible: bool = True

    def __post_init__(self) -> None:
        # Validar número no vacío.
        if not self.numero or not self.numero.strip():
            raise ValueError("El número de la habitación no puede estar vacío.")
        # Validar piso no negativo.
        if self.piso < 0:
            raise ValueError("El piso de la habitación no puede ser negativo.")
        # Validar precio positivo.
        if self.precio <= 0:
            raise ValueError("El precio de la habitación debe ser mayor que cero.")

    def __str__(self) -> str:
        estado = "Disponible" if self.disponible else "Ocupada"
        return f"Habitación {self.numero} - {self.tipo}, piso {self.piso} - {estado}"
