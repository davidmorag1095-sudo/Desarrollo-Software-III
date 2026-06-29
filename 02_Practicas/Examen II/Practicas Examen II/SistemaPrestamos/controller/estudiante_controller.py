import view.view as view
from service.estudiante_service import Estudiante_service

class EstudianteController:
    def __init__(self):
        self.service_estudiante = Estudiante_service()

    def save_prestamo(self, id, nombre, correo, carrera):
        try:
            estudiante = self.service_estudiante.save_estudiante(id, nombre, correo, carrera)
            if estudiante:
                view.mostrar_mensaje("Agregado correctamente")
            return estudiante

        except Exception as Error:
            return view.mostrar_mensaje(Error)
#---------------------------------------------------------------------------------------------------------
    def get_all_estudiantes(self):
        try:
            estudiante = self.service_estudiante.get_all_estudiante()
            if estudiante:
                view.mostrar_dato(estudiante)

        except Exception as Error:
            return view.mostrar_mensaje(Error)
#---------------------------------------------------------------------------------------------------------
    def serch_by_codigo(self, id):
        try:
            encontrado = self.service_estudiante.serch_by_id(id)
            if encontrado:
                view.mostrar_dato(encontrado)

        except Exception as Error:
            return view.mostrar_mensaje(Error)
#---------------------------------------------------------------------------------------------------------
    def update_estudiante(self, id, nombre, correo, carrera):
        try:
            encontrado = self.service_estudiante.update_estudiante(id, nombre, correo, carrera)
            if encontrado:
                view.mostrar_mensaje("Modificado correctamente")

        except Exception as Error:
            return view.mostrar_mensaje(Error)
#---------------------------------------------------------------------------------------------------------
    def delete_estudiante(self, id):
        try:
            encontrado = self.service_estudiante.delete_estudiante(id)
            if encontrado:
                view.mostrar_mensaje("Eliminado correctamente")

        except Exception as Error:
            return view.mostrar_mensaje(Error)
#---------------------------------------------------------------------------------------------------------
