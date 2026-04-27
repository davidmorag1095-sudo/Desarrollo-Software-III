from PracticaExamen.repository.repositorio import Repositorio
class AsignacionService:
    """Capa de servicio para operaciones relacionadas con asignaciones de ayuda."""

    def __init__(self, ben_service, rec_service) -> None:
        """
        Servicio encargado de manejar operaciones sobre asignaciones.

        Cada instancia de AsignacionService posee su propio repositorio para almacenar asignaciones.

        Args:
            ben_service: Servicio para operaciones sobre beneficiarios.
            rec_service: Servicio para operaciones sobre recursos.
        """
        # Repositorio propio para almacenar asignaciones
        self.repositorio: Repositorio = Repositorio()
        self.ben_service = ben_service
        self.rec_service = rec_service

    def registrar(self, asignacion):
        #Verificamos la existencia del beneficiario y del recurso utilizando sus identificadores
        beneficiario_existente = self.ben_service.buscar(asignacion.beneficiario.identificacion)
        recurso_existente = self.rec_service.buscar(asignacion.recurso.codigo)

        if not beneficiario_existente:
            raise ValueError("Beneficiario no existe")
        if not recurso_existente:
            raise ValueError("Recurso no existe")
        #Validar cantidad positiva ya fue verificado en el constructor de Asignacion
        if asignacion.cantidad > recurso_existente.cantidad:
            raise ValueError("Inventario insuficiente")

        #Descontar inventario del recurso existente
        recurso_existente.cantidad -= asignacion.cantidad

        # Almacenar la asignación en el repositorio propio
        self.repositorio.add(asignacion.codigo, asignacion)

    def listar(self):
        """Devuelve todas las asignaciones registradas."""
        return self.repositorio.get_all()

    def listar_por_beneficiario(self, identificacion: str):
        """Obtiene las asignaciones asociadas a un beneficiario específico."""
        # Filtramos las asignaciones donde el identificador del beneficiario coincida
        return [asignacion for asignacion in self.repositorio.get_all() if asignacion.beneficiario.identificacion == identificacion]

    def listar_por_fecha(self, fecha: str):
        """Obtiene las asignaciones realizadas en una fecha específica."""
        #Filtramos por fecha exacta de la asignación
        return [asignacion for asignacion in self.repositorio.get_all() if asignacion.fecha == fecha]