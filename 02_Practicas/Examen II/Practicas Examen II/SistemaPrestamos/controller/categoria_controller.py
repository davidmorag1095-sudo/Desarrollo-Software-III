import view.view as view
from service.equipo_service import Equipo_service

class EquipoController:
    def __init__(self):
        self.service_equipo = Equipo_service()

    def save_team(self, codigo, nombre, marca, estado, categoria_id):
        try:
            team = self.service_equipo.save_equipo(codigo, nombre, marca, estado, categoria_id)
            if team:
                view.mostrar_mensaje("Agregado correctamente")
            return team

        except Exception as Error:
            return view.mostrar_mensaje(Error)
#---------------------------------------------------------------------------------------------------------
    def get_all_team(self):
        try:
            equipo = self.service_equipo.get_all_equipo()
            if equipo:
                view.mostrar_dato(equipo)

        except Exception as Error:
            return view.mostrar_mensaje(Error)
#---------------------------------------------------------------------------------------------------------
    def serch_by_codigo(self, codigo):
        try:
            encontrado = self.service_equipo.serch_by_codigo(codigo)
            if encontrado:
                view.mostrar_dato(encontrado)

        except Exception as Error:
            return view.mostrar_mensaje(Error)
#---------------------------------------------------------------------------------------------------------
    def update_team(self, codigo, nombre, marca, estado, categoria_id):
        try:
            encontrado = self.update_team(codigo,nombre, marca, estado, categoria_id)
            if encontrado:
                view.mostrar_mensaje("Modificado correctamente")

        except Exception as Error:
            return view.mostrar_mensaje(Error)
#---------------------------------------------------------------------------------------------------------
    def delete_team(self, codigo):
        try:
            encontrado = self.service_equipo.delete_by_codigo(codigo)
            if encontrado:
                view.mostrar_mensaje("Eliminado correctamente")

        except Exception as Error:
            return view.mostrar_mensaje(Error)
#---------------------------------------------------------------------------------------------------------
