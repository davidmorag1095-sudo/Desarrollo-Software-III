from __future__ import annotations

from datetime import date

from hotel_exam_complete.hotel_exam.controller.controlador import Controlador
from hotel_exam_complete.hotel_exam.model.huesped import Huesped
from hotel_exam_complete.hotel_exam.model.habitacion import Habitacion
from hotel_exam_complete.hotel_exam.model.reserva import Reserva


def main() -> None:
    # Crear controlador
    controlador = Controlador()
    # Crear interfaz gráfica y pasar el controlador
    from hotel_exam_complete.hotel_exam.view.GUI import GUI  # Importar aquí para evitar dependencias circulares
    app = GUI(controlador)
    app.run()


if __name__ == "__main__":
    main()
