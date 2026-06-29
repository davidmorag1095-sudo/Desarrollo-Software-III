import view.view as view
from service.prestamo_service import Prestamo_service

class PrestamoController:
    def __init__(self):
        self.service_prestamo = Prestamo_service()

    def save_prestamo(self, id, estudiante_id, equipo_codigo, fecha_prestamo, fecha_devolucion, estado):
        try:
            prestamo = self.service_prestamo.save_prestamo(id, estudiante_id, equipo_codigo, fecha_prestamo, fecha_devolucion, estado)
            if prestamo:
                view.mostrar_mensaje("Agregado correctamente")
            return prestamo

        except Exception as Error:
            return view.mostrar_mensaje(Error)
#---------------------------------------------------------------------------------------------------------
    def get_all_prestamo(self):
        try:
            prestamo = self.service_prestamo.get_all_prestamo()
            if prestamo:
                view.mostrar_dato(prestamo)

        except Exception as Error:
            return view.mostrar_mensaje(Error)
#---------------------------------------------------------------------------------------------------------
    def serch_by_codigo(self, id):
        try:
            encontrado = self.service_prestamo.serch_by_id(id)
            if encontrado:
                view.mostrar_dato(encontrado)

        except Exception as Error:
            return view.mostrar_mensaje(Error)
#---------------------------------------------------------------------------------------------------------
    def update_prestamo(self, id, estudiante_id, equipo_codigo, fecha_prestamo, fecha_devolucion, estado):
        try:
            encontrado = self.update_prestamo(id, estudiante_id, equipo_codigo, fecha_prestamo, fecha_devolucion, estado)
            if encontrado:
                view.mostrar_mensaje("Modificado correctamente")

        except Exception as Error:
            return view.mostrar_mensaje(Error)
#---------------------------------------------------------------------------------------------------------
    def delete_prestamo(self, id):
        try:
            encontrado = self.service_prestamo.delete_prestamo(id)
            if encontrado:
                view.mostrar_mensaje("Eliminado correctamente")

        except Exception as Error:
            return view.mostrar_mensaje(Error)
#---------------------------------------------------------------------------------------------------------
