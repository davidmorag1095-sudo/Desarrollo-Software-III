from PracticaExamen.repository.repositorio import Repositorio
from PracticaExamen.service.beneficiario_service import BeneficiarioService
from PracticaExamen.service.recurso_service import RecursoService
from PracticaExamen.service.asignacion_service import AsignacionService
from PracticaExamen.service.reportes_service import ReportService
from PracticaExamen.controller.controlador import Controlador
from PracticaExamen.view.GUI import GUI

# repos
ben_repo = Repositorio()
rec_repo = Repositorio()
asig_repo = Repositorio()

# services
ben_service = BeneficiarioService(ben_repo)
rec_service = RecursoService(rec_repo)
asig_service = AsignacionService(ben_service, rec_service)
report_service = ReportService(asig_service, rec_service, ben_service)

# controller
controller = Controlador(ben_service, rec_service, asig_service,report_service)
controller.report_service = report_service

# GUI
GUI(controller)