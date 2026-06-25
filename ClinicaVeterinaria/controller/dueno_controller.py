import View.vista as vista
from service.dueno_service import Dueno_service

class Dueno_controller():
    def __init__(self):
        self.dueno_service = Dueno_service()
#---------------------------------------------------------------------------------------------------------
    def registrar(self, id, nombre, telefono, email):
        try:
            exito = self.dueno_service.registrar_dueno(id, nombre, telefono, email)
            if exito:
                vista.mostrar_mensajes("Dueño registrado correctamente")

        except Exception as Error:
            vista.mostrar_mensajes(Error)
#---------------------------------------------------------------------------------------------------------
    def listar(self):
        try:
            datos = self.dueno_service.get_all()
            vista.mostrar_datos(datos)
        except Exception as Error:
            vista.mostrar_mensajes(Error)
#---------------------------------------------------------------------------------------------------------
    def serch_id(self,id):
        try:
            datos =  self.dueno_service.serch_id(id)
            vista.mostrar_datos(datos)
        except Exception as Error:
            vista.mostrar_mensajes(Error)
#---------------------------------------------------------------------------------------------------------
    def update(self, id, nombre, telefono, email):
        try:
            encontrado = self.dueno_service.update(id, nombre, telefono, email)

            if encontrado:
                vista.mostrar_mensajes("Modificado correctamente")

        except Exception as Error:
            vista.mostrar_mensajes(Error)
#---------------------------------------------------------------------------------------------------------
    def eliminar(self, id):
        try:
            eliminado = self.dueno_service.delete(id)
            if eliminado:
                vista.mostrar_mensajes("Eliminado correctamente")

        except Exception as Error:
            vista.mostrar_mensajes(Error)
#---------------------------------------------------------------------------------------------------------