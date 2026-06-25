
from dataclasses import dataclass
from .huesped import Huesped
from .habitacion import Habitacion


@dataclass
class Reserva:
    codigo: str
    huesped: Huesped
    habitacion: Habitacion
    noches: int
    fecha: str
    responsable: str

    def __post_init__(self) -> None:
        if self.noches <= 0:
            raise ValueError("La cantidad de noches debe ser mayor que cero.")

    def costo_total(self) -> float:
        """Calcula el monto total de la reserva.

        Retorna:
            El costo total calculado como ``noches * habitacion.precio``.
        """
        return self.noches * self.habitacion.precio

    def __str__(self) -> str:
        """Representación legible de la reserva."""
        return (
            f"Reserva {self.codigo}: {self.huesped.nombre} en habitación "
            f"{self.habitacion.numero} por {self.noches} noches a partir de {self.fecha}"
        )
