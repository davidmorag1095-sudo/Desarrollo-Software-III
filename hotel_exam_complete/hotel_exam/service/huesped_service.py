from __future__ import annotations

from typing import List

from ..model.huesped import Huesped
from ..repository.repositorio import Repositorio


class HuespedService:
    def __init__(self) -> None:
        # Cada servicio mantiene su propio repositorio en memoria.
        self.repositorio = Repositorio[Huesped]()

    def registrar(self, huesped: Huesped) -> None:
        self.repositorio.agregar(huesped.identificacion, huesped)

    def buscar(self, identificacion: str) -> Huesped | None:
        return self.repositorio.buscar(identificacion)

    def listar(self) -> List[Huesped]:
        return self.repositorio.listar()

    def eliminar(self, identificacion: str) -> None:
        self.repositorio.eliminar(identificacion)

    def listar_por_pais(self, pais: str) -> List[Huesped]:
        return [h for h in self.repositorio.listar() if h.pais == pais]
