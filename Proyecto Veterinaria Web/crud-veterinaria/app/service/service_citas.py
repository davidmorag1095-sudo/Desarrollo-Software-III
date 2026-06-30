from app.repository.repository_citas import RepositoryCitas
from app.repository.repository_mascotas import RepositoryMascotas


class ServiceCitas:

    def __init__(self):
        self.repo = RepositoryCitas()
        self.repo_mascotas = RepositoryMascotas()

    def registrar_cita(self, codigo_mascota, fecha, hora, motivo, estado):
        self.validar_datos(codigo_mascota, fecha, hora, motivo, estado)
        if self.repo.existe_horario(fecha, hora):
            raise ValueError("Ya existe una cita en esa fecha y hora")
        return self.repo.save(codigo_mascota, fecha, hora, motivo, estado)

    def buscar_cita(self, id):
        return self.repo.get(id)

    def listar_citas(self):
        return self.repo.get_all()

    def actualizar_cita(self, id, codigo_mascota, fecha, hora, motivo, estado):
        self.validar_datos(codigo_mascota, fecha, hora, motivo, estado)
        if self.repo.existe_horario(fecha, hora, id):
            raise ValueError("Ya existe una cita en esa fecha y hora")
        return self.repo.update(id, codigo_mascota, fecha, hora, motivo, estado)

    def eliminar_cita(self, id):
        return self.repo.delete(id)

    def reporte_por_estado(self):
        return [{"estado": dato[0], "cantidad": dato[1]} for dato in self.repo.count_by_estado()]

    def validar_datos(self, codigo_mascota, fecha, hora, motivo, estado):
        if not codigo_mascota.strip() or not fecha.strip() or not hora.strip() or not motivo.strip():
            raise ValueError("Debe completar todos los campos")
        if estado not in ["Pendiente", "Atendida", "Cancelada"]:
            raise ValueError("El estado de la cita no es válido")
        if self.repo_mascotas.get(codigo_mascota) is None:
            raise ValueError("No se encontró la mascota indicada")

