from repository.mascota_repository import MascotaRepository
from service.dueno_service import Dueno_service

class MascotaService:
    def __init__(self):
        self.repository = MascotaRepository()
        self.service = Dueno_service()
#---------------------------------------------------------------------------------------------------------
    def registrar_mascota(self, codigo, nombre, especie, edad, dueno_id):
        if not codigo.strip() or not nombre.strip() or not especie.strip() or not edad.strip():
            raise ValueError ("Ingrese todos los datos")

        if self.repository.get_by_codigo(codigo):
            raise ValueError ("Ya se encuentra un cliente registrado")

        if self.service.serch_id(dueno_id) is None:
            raise ValueError ("El id del dueño debe existir")

        if int(edad) < 1:
            raise ValueError ("El edad debe ser positivo")

        mascotaRegistrada = self.repository.registar_mascota(codigo, nombre, especie, edad, dueno_id)

        return mascotaRegistrada
#---------------------------------------------------------------------------------------------------------
    def get_all(self):
        datosEncontrados = self.repository.get_all()
        if not datosEncontrados:
            raise ValueError ("No se encontraron mascotas registradas")

        return datosEncontrados
#---------------------------------------------------------------------------------------------------------
    def get_by_codigo(self, codigo):
        if  not codigo.strip():
            raise ValueError("Debe ingresar el codigo")

        mascota = self.repository.get_by_codigo(codigo)
        if mascota is None:
            raise ValueError ("No se encuentra ninguna mascota registrada con ese codigo")

        return mascota
#---------------------------------------------------------------------------------------------------------
    def update(self,codigo, nombre, especie, edad, dueno_id):
        if not codigo.strip():
            raise ValueError ("Debe ingresar el codigo")

        mascota = self.repository.get_by_codigo(codigo)

        if mascota is None:
            raise ValueError("No se encuentra ninguna mascota registrada con ese codigo")

        return self.repository.update(codigo, nombre, especie, edad, dueno_id)
#---------------------------------------------------------------------------------------------------------
    def delete(self, codigo):
        if not codigo.strip():
            raise ValueError ("Debe ingresar el codigo")

        mascota = self.repository.get_by_codigo(codigo)

        if mascota is None:
            raise ValueError("No se encuentra ninguna mascota registrada con ese codigo")

        return self.repository.delete_pet(codigo)

#---------------------------------------------------------------------------------------------------------

