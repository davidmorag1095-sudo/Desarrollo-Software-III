from PracticaExamen.repository.repositorio import Repositorio
from PracticaExamen.service.beneficiario_service import BeneficiarioService
from PracticaExamen.service.recurso_service import RecursoService
from PracticaExamen.service.asignacion_service import AsignacionService
from PracticaExamen.service.reportes_service import ReportService
from PracticaExamen.controller.controlador import Controlador
from PracticaExamen.view.GUI import GUI

# Repositorios genéricos para cada tipo de entidad
repositorio_beneficiarios = Repositorio()
repositorio_recursos = Repositorio()
repositorio_asignaciones = Repositorio()

# Servicios que encapsulan la lógica de negocio
servicio_beneficiarios = BeneficiarioService(repositorio_beneficiarios)
servicio_recursos = RecursoService(repositorio_recursos)
servicio_asignaciones = AsignacionService(servicio_beneficiarios, servicio_recursos)
servicio_reportes = ReportService(servicio_asignaciones, servicio_recursos, servicio_beneficiarios)

# Controlador que coordina los servicios con la interfaz
controlador = Controlador(servicio_beneficiarios, servicio_recursos, servicio_asignaciones, servicio_reportes)
controlador.report_service = servicio_reportes

# Interfaz gráfica
GUI(controlador)