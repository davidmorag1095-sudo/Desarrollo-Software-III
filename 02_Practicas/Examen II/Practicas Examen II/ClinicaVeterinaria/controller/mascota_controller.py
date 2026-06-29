from View import vista
from service.mascotas_service import MascotaService

class Mascota_controller():
    def __init__(self):
        self.mascota_service = MascotaService()
#---------------------------------------------------------------------------------------------------------

    def registrar_mascota(self,codigo, nombre, especie, edad, dueno_id):
        try:
            exito = self.mascota_service.registrar_mascota(codigo, nombre, especie, edad, dueno_id)
            if exito:
                vista.mostrar_mensajes("Registrado correctamente")

        except Exception as Error:
            vista.mostrar_mensajes(Error)
#---------------------------------------------------------------------------------------------------------
    def get_all(self):
        try:
            mascota = self.mascota_service.get_all()
            if mascota:
                 vista.mostrar_datos(mascota)

        except Exception as Error:
            vista.mostrar_mensajes(Error)
#---------------------------------------------------------------------------------------------------------
    def buscar_codigo(self,codigo):
        try:
            exito = self.mascota_service.get_by_codigo(codigo)
            if exito:
                vista.mostrar_datos(exito)

        except Exception as Error:
            vista.mostrar_mensajes(Error)
#---------------------------------------------------------------------------------------------------------
    def update(self,codigo, nombre, especie, edad, dueno_id):
        try:
            actualizado = self.mascota_service.update(codigo, nombre, especie, edad, dueno_id)

            if actualizado:
                vista.mostrar_datos(actualizado)

        except Exception as Error:
            vista.mostrar_mensajes(Error)
#---------------------------------------------------------------------------------------------------------
    def eliminar(self,codigo):
        try:
            eliminado = self.mascota_service.delete(codigo)

            if eliminado:
                vista.mostrar_mensajes("Eliminado correctamente")

        except Exception as Error:
            vista.mostrar_mensajes(Error)
#---------------------------------------------------------------------------------------------------------