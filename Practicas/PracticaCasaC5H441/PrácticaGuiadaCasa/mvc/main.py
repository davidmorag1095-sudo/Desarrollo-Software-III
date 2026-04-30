from mvc.model.repo_estudiante import RepoEstudiantes
from mvc.model.repo_cursos import RepoCursos
from mvc.model.repo_matricula import RepoMatriculas
from mvc.service.servicio_academico import ServicioAcademico
from mvc.controller.controlador import Controlador
from mvc.view.main_window import MainWindow

repo_estudiantes = RepoEstudiantes()
repo_cursos = RepoCursos()
repo_matriculas = RepoMatriculas()

servicio = ServicioAcademico(repo_estudiantes, repo_cursos, repo_matriculas)
controlador = Controlador(servicio)

MainWindow(controlador)