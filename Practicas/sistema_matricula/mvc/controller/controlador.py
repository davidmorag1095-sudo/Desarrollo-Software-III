from Practicas.sistema_matricula.mvc.model.estudiante import Estudiante
from Practicas.sistema_matricula.mvc.model.curso import Curso
from Practicas.sistema_matricula.mvc.model.matricula import Matricula
from Practicas.sistema_matricula.mvc.model.repositorio import Repositorio

class Controlador:
    """
    Clase Controlador
    Coordina la comunicación entre vista y modelo
    """
    def __init__(self):
        self.repo_estudiantes = Repositorio[Estudiante]()
        self.repo_cursos = Repositorio[Curso]()
        self.repo_matriculas = Repositorio[Matricula]()

    def agregar_estudiante(self, carnet, nombre, carrera):
        if carnet == "":
            print("Carnet no puede estar vacío")
            return
        estudiante = Estudiante(carnet, nombre, carrera)
        self.repo_estudiantes.agregar(estudiante)

    def consultar_estudiantes(self):
        return self.repo_estudiantes.consultar()

    def agregar_curso(self, sigla, nombre, creditos):
        if sigla == "":
            print("Sigla no puede estar vacía")
            return
        curso = Curso(sigla, nombre, creditos)
        self.repo_cursos.agregar(curso)

    def consultar_cursos(self):
        return self.repo_cursos.consultar()

    def matricular(self, indice_estudiante, indice_curso):
        estudiante = self.repo_estudiantes.buscar(indice_estudiante - 1)
        curso = self.repo_cursos.buscar(indice_curso - 1)

        if estudiante is None:
            print("Estudiante no existe")
            return

        if curso is None:
            print("Curso no existe")
            return
        matricula = Matricula(estudiante, curso)
        self.repo_matriculas.agregar(matricula)

    def consultar_matriculas(self):
        return self.repo_matriculas.consultar()