"""Controlador para orquestar las operaciones del sistema de hotel.

Esta clase expone métodos de alto nivel que delegan en los servicios
subyacentes. De esta forma se mantiene una separación clara entre
interacción del usuario y la lógica de negocio.
"""

from __future__ import annotations

from typing import List

from ..model.huesped import Huesped
from ..model.habitacion import Habitacion
from ..model.reserva import Reserva
from ..service.huesped_service import HuespedService
from ..service.habitacion_service import HabitacionService
from ..service.reserva_service import ReservaService


class Controlador:
    """Controlador que coordina los distintos servicios del sistema."""

    def __init__(self) -> None:
        self.huesped_service = HuespedService()
        self.habitacion_service = HabitacionService()
        self.reserva_service = ReservaService(self.huesped_service, self.habitacion_service)

    # Métodos para huéspedes
    def registrar_huesped(self, huesped: Huesped) -> None:
        self.huesped_service.registrar(huesped)

    def buscar_huesped(self, identificacion: str) -> Huesped | None:
        return self.huesped_service.buscar(identificacion)

    def listar_huespedes(self) -> List[Huesped]:
        return self.huesped_service.listar()

    def eliminar_huesped(self, identificacion: str) -> None:
        self.huesped_service.eliminar(identificacion)

    def listar_huespedes_por_pais(self, pais: str) -> List[Huesped]:
        return self.huesped_service.listar_por_pais(pais)

    # Métodos para habitaciones
    def registrar_habitacion(self, habitacion: Habitacion) -> None:
        self.habitacion_service.registrar(habitacion)

    def buscar_habitacion(self, numero: str) -> Habitacion | None:
        return self.habitacion_service.buscar(numero)

    def listar_habitaciones(self) -> List[Habitacion]:
        return self.habitacion_service.listar()

    def eliminar_habitacion(self, numero: str) -> None:
        self.habitacion_service.eliminar(numero)

    def listar_habitaciones_por_tipo(self, tipo: str) -> List[Habitacion]:
        return self.habitacion_service.listar_por_tipo(tipo)

    def cambiar_estado_habitacion(self, numero: str, disponible: bool) -> None:
        self.habitacion_service.marcar_disponible(numero, disponible)

    # Métodos para reservas
    def registrar_reserva(self, reserva: Reserva) -> None:
        self.reserva_service.registrar(reserva)

    def buscar_reserva(self, codigo: str) -> Reserva | None:
        return self.reserva_service.buscar(codigo)

    def listar_reservas(self) -> List[Reserva]:
        return self.reserva_service.listar()

    def eliminar_reserva(self, codigo: str) -> None:
        self.reserva_service.eliminar(codigo)

    def listar_reservas_por_huesped(self, identificacion: str) -> List[Reserva]:
        return self.reserva_service.listar_por_huesped(identificacion)

    def listar_reservas_por_fecha(self, fecha: str) -> List[Reserva]:
        return self.reserva_service.listar_por_fecha(fecha)
