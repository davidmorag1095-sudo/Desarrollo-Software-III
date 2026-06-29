from dataclasses import dataclass


@dataclass
class Huesped:

    identificacion: str
    nombre: str
    pais: str

    def __post_init__(self) -> None:
        # Validar que identificación y nombre no estén vacíos.
        if not self.identificacion or not self.identificacion.strip():
            raise ValueError("La identificación del huésped no puede estar vacía.")
        if not self.nombre or not self.nombre.strip():
            raise ValueError("El nombre del huésped no puede estar vacío.")

    def __str__(self) -> str:
        """Representación de cadena legible del huésped."""
        return f"{self.identificacion} - {self.nombre} ({self.pais})"
