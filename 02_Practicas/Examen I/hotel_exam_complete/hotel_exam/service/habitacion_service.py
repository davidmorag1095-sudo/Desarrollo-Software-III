from __future__ import annotations

from typing import List

from ..model.habitacion import Habitacion
from ..repository.repositorio import Repositorio


class HabitacionService:
    def __init__(self) -> None:
        self.repositorio = Repositorio[Habitacion]()

    def registrar(self, habitacion: Habitacion) -> None:
        self.repositorio.agregar(habitacion.numero, habitacion)

    def buscar(self, numero: str) -> Habitacion | None:
        return self.repositorio.buscar(numero)

    def listar(self) -> List[Habitacion]:
        return self.repositorio.listar()

    def eliminar(self, numero: str) -> None:
        self.repositorio.eliminar(numero)

    def listar_por_tipo(self, tipo: str) -> List[Habitacion]:
        return [h for h in self.repositorio.listar() if h.tipo == tipo]

    def marcar_disponible(self, numero: str, disponible: bool) -> None:
        habitacion = self.repositorio.buscar(numero)
        if habitacion:
            habitacion.disponible = disponible
