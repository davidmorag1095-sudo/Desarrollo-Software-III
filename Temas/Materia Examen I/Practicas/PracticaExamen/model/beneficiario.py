class Beneficiario:
    def __init__(self, identificacion: str, nombre: str, comunidad: str,
                 integrantes: int, prioridad: str) -> None:
        if integrantes <= 0:
            raise ValueError("Integrantes debe ser mayor a 0")
        self.identificacion = identificacion
        self.nombre = nombre
        self.comunidad = comunidad
        # persistimos la cantidad de integrantes como atributo de instancia
        self.integrantes = integrantes
        self.prioridad = prioridad

    def __repr__(self) -> str:
        return (f"Beneficiario(identificacion={self.identificacion!r}, "
                f"nombre={self.nombre!r}, comunidad={self.comunidad!r}, "
                f"integrantes={self.integrantes!r}, prioridad={self.prioridad!r})")

