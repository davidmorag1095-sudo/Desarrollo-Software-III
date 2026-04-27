from practicaMixta.mvc.Model.repositorio import Repositorio
from practicaMixta.mvc.Model.matricula import Matricula
from practicaMixta.mvc.Model.estudiante import Estudiante

class Controlador:
    def __init__(self):
        self.repo_Estudiantes = Repositorio[tuple]()
        self.repo_Matricula = Repositorio[Matricula]()

    def agregar_Estudiantes(self, carnet, nombre, carrera):
        tupla = (nombre, carrera)
        self.repo_Estudiantes.agregar(carnet, tupla)

    def consultar_Estudiante(self):
        return self.repo_Estudiantes.consultar()

    def modificar_Estudiante(self, carnet, nombre, carrera):
        nueva_Tupla = (nombre, carrera)
        return self.repo_Estudiantes.modificar(carnet, nueva_Tupla)

    def eliminar_Estudiantes(self, carnet):
        return self.repo_Estudiantes.eliminar(carnet)

    def agregar_Matricula(self, numero_matricula, curso, creditos, carnet_estudiante):
        estudiante_Guardado = self.repo_Estudiantes.consultarUno(carnet_estudiante)

        if estudiante_Guardado is not None:
            nombre, carrera = estudiante_Guardado
            estudiante = Estudiante(carnet_estudiante, nombre, carrera)
            matricula = Matricula(numero_matricula, curso, creditos, estudiante)
            return self.repo_Matricula.agregar(numero_matricula, matricula)

        return False

    def consultar_Matricula(self):
        return self.repo_Matricula.consultar()

    def modificar_Matricula(self, numero_matricula, curso, creditos, carnet_estudiante):
        estudiante_Guardado = self.repo_Estudiantes.consultarUno(carnet_estudiante)

        if estudiante_Guardado is not None:
            nombre, carrera = estudiante_Guardado
            estudiante  = Estudiante(carnet_estudiante, nombre, carrera)
            nueva_Matricula = Matricula(numero_matricula, curso, creditos, estudiante)
            return self.repo_Matricula.modificar(numero_matricula, nueva_Matricula)
        return False

    def eliminar_Matricula(self, numero_matricula):
        return self.repo_Matricula.eliminar(numero_matricula)


