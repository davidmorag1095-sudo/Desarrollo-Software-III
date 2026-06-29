from repository.dueno_repository import DuenoRepository
from repository.mascota_repository import MascotaRepository

class Dueno_service:
    def __init__(self):
        self.repo_dueno = DuenoRepository()
        self.repo_mascota = MascotaRepository()
#---------------------------------------------------------------------------------------------------------
    def registrar_dueno(self,id, nombre, telefono, email):
        if not id.strip() or not nombre.strip() or not telefono.strip() or not email.strip():
            raise ValueError ("Debe ingresar un dato")

        if self.repo_dueno.serch_id(id):
            raise ValueError ("Ya existe un dueño con ese id")

        return self.repo_dueno.save(id, nombre, telefono, email)
#---------------------------------------------------------------------------------------------------------
    def get_all(self):
        if self.repo_dueno.get_all() is None:
            raise ValueError ("No hay datos en la base de datos")

        return self.repo_dueno.get_all()
#---------------------------------------------------------------------------------------------------------
    def serch_id(self, id):
        if not id.strip():
            raise ValueError ("Debe ingresar un dato")

        if self.repo_dueno.serch_id(id) is None:
            raise ValueError("No se encontro dueño con ese id")

        return self.repo_dueno.serch_id(id)
#---------------------------------------------------------------------------------------------------------
    def update(self, id, nombre, telefono, email):
        if not id.strip() or not nombre or not telefono or not email.strip():
            raise ValueError ("Debe ingresar un dato")

        if self.repo_dueno.serch_id(id) is None:
            raise ValueError ("No hay datos en la base de datos con ese id")

        return self.repo_dueno.update(id, nombre, telefono, email)
#---------------------------------------------------------------------------------------------------------
    def delete(self, id):
        if not id.strip():
            raise ValueError ("Debe ingresar un dato")

        if self.repo_dueno.serch_id(id) is None:
            raise ValueError ("No hay datos en la base de datos con ese id")

        if self.repo_mascota.existe_dueno_con_mascota(id):
            raise ValueError ("No puede eliminar un dueño porque tiene mascota asociada")

        return self.repo_dueno.delete(id)
#---------------------------------------------------------------------------------------------------------