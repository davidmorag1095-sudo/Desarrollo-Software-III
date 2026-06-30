from app.repository.repository_duenos import RepositoryDuenos
from app.repository.repository_mascotas import RepositoryMascotas


class ServiceMascotas:

    def __init__(self):
        self.repo = RepositoryMascotas()
        self.repo_duenos = RepositoryDuenos()

    def registrar_mascota(self, codigo, nombre, especie, edad, dueno_id):
        self.validar_datos(codigo, nombre, especie, edad, dueno_id)
        if self.repo.get(codigo):
            raise ValueError("Ya existe una mascota con ese código")
        return self.repo.save(codigo, nombre, especie, edad, dueno_id)

    def buscar_mascota(self, codigo):
        return self.repo.get(codigo)

    def listar_mascotas(self):
        return self.repo.get_all()

    def actualizar_mascota(self, codigo, nombre, especie, edad, dueno_id):
        self.validar_datos(codigo, nombre, especie, edad, dueno_id)
        return self.repo.update(codigo, nombre, especie, edad, dueno_id)

    def eliminar_mascota(self, codigo):
        return self.repo.delete(codigo)

    def reporte_por_especie(self):
        return [{"especie": dato[0], "cantidad": dato[1]} for dato in self.repo.count_by_especie()]

    def validar_datos(self, codigo, nombre, especie, edad, dueno_id):
        if not codigo.strip() or not nombre.strip() or not especie.strip():
            raise ValueError("Debe completar todos los campos")
        if edad < 0:
            raise ValueError("La edad no puede ser negativa")
        if self.repo_duenos.get(dueno_id) is None:
            raise ValueError("No se encontró el dueño indicado")

