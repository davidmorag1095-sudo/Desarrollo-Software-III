from app.repository.repository_duenos import RepositoryDuenos
from app.repository.repository_mascotas import RepositoryMascotas


class ServiceDuenos:

    def __init__(self):
        self.repo_duenos = RepositoryDuenos()
        self.repo_mascotas = RepositoryMascotas()

    def registrar_dueno(self, nombre, telefono, email):
        if not nombre.strip() or not telefono.strip() or not email.strip():
            raise ValueError("Debe completar todos los campos")
        return self.repo_duenos.save(nombre, telefono, email)

    def buscar_dueno(self, id):
        return self.repo_duenos.get(id)

    def listar_duenos(self):
        return self.repo_duenos.get_all()

    def filtrar_duenos(self, nombre):
        return self.repo_duenos.search_name(nombre)

    def actualizar_dueno(self, id, nombre, telefono, email):
        if not nombre.strip() or not telefono.strip() or not email.strip():
            raise ValueError("Debe completar todos los campos")
        return self.repo_duenos.update(id, nombre, telefono, email)

    def eliminar_dueno(self, id):
        if self.repo_mascotas.existe_dueno_con_mascota(id):
            raise ValueError("No se puede eliminar el dueño porque tiene mascotas asociadas")
        return self.repo_duenos.delete(id)

