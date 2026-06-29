from __future__ import annotations

from typing import List

from ..model.reserva import Reserva
from ..repository.repositorio import Repositorio
from .huesped_service import HuespedService
from .habitacion_service import HabitacionService


class ReservaService:
    def __init__(self, huesped_service: HuespedService, habitacion_service: HabitacionService) -> None:
        self.repositorio = Repositorio[Reserva]()
        self.huesped_service = huesped_service
        self.habitacion_service = habitacion_service

    def registrar(self, reserva: Reserva) -> None:
        huesped = self.huesped_service.buscar(reserva.huesped.identificacion)
        if huesped is None:
            raise ValueError("El huésped asociado a la reserva no existe.")
        habitacion = self.habitacion_service.buscar(reserva.habitacion.numero)
        if habitacion is None:
            raise ValueError("La habitación asociada a la reserva no existe.")
        if not habitacion.disponible:
            raise ValueError("La habitación no está disponible para reservar.")
        # Marcar habitación como ocupada
        habitacion.disponible = False
        # Almacenar la reserva
        self.repositorio.agregar(reserva.codigo, reserva)

    def buscar(self, codigo: str) -> Reserva | None:
        return self.repositorio.buscar(codigo)

    def listar(self) -> List[Reserva]:
        return self.repositorio.listar()

    def eliminar(self, codigo: str) -> None:
        reserva = self.repositorio.buscar(codigo)
        if reserva:
            # Liberar la habitación asociada
            habitacion = self.habitacion_service.buscar(reserva.habitacion.numero)
            if habitacion:
                habitacion.disponible = True
            self.repositorio.eliminar(codigo)

    def listar_por_huesped(self, identificacion: str) -> List[Reserva]:
        return [r for r in self.repositorio.listar() if r.huesped.identificacion == identificacion]

    def listar_por_fecha(self, fecha: str) -> List[Reserva]:
        return [r for r in self.repositorio.listar() if r.fecha == fecha]
