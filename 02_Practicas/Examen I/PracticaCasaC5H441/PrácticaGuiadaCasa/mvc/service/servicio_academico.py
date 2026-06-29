from mvc.model.estudiante import Estudiante
from mvc.model.curso import Curso
from mvc.model.matricula import Matricula

class ServicioAcademico:
    def __init__(self, repo_estudiantes, repo_cursos, repo_matriculas):
        self.repo_estudiantes = repo_estudiantes
        self.repo_cursos = repo_cursos
        self.repo_matriculas = repo_matriculas

    def registrar_estudiante(self, identificador, nombre, carrera):
        if not identificador or not nombre or not carrera:
            return "Datos vacios..."
        estudiante = Estudiante(identificador, nombre, carrera)

        if not self.repo_estudiantes.agregar(estudiante):
            return "Ya existe ese estudiante"
        return "Registrado correctamente"

    def registrar_curso(self, codigo, nombre, creditos):
        if not codigo or not nombre or not creditos:
            return "Datos vacios..."
        curso = Curso(codigo, nombre, creditos)

        if not self.repo_cursos.agregar(curso):
            return "Ya existe ese curso"
        return "Registrado correctamente"

    def registrar_matricula(self, numero, estudiante_id, cod, periodo):
        if not numero or not estudiante_id or not cod or not periodo:
            return "Datos vacios..."
        if not self.repo_estudiantes.existe(estudiante_id):
            return "El estudiante no existe"
        if not self.repo_cursos.existe(cod):
            return "El curso no existe"
        matricula = Matricula(numero, estudiante_id, cod, periodo)

        if not self.repo_matriculas.agregar(matricula):
            return "Ya existe esa matricula"
        return "Registrado correctamente"

    def ver_estudiantes(self):
        return self.repo_estudiantes.obtener_todos()

    def ver_cursos(self):
        return self.repo_cursos.obtener_todos()

    def ver_matriculas(self):
        datos = self.repo_matriculas.obtener_todos()
        estudiantes = self.repo_estudiantes.obtener_todos()
        cursos = self.repo_cursos.obtener_todos()
        resultado = []

        for matricula in datos.values():
            estudiante = estudiantes.get(matricula["estudiante_id"])
            curso = cursos.get(matricula["curso_codigo"])

            nombre_estudiante = estudiante["nombre"] if estudiante else "No encontrado"
            nombre_curso = curso["nombre"] if curso else "No encontrado"
            resultado.append((matricula["numero"], nombre_estudiante, nombre_curso, matricula["periodo"]))
        return resultado

    def buscar_matriculas_estudiante(self, identificador):
        datos = self.repo_matriculas.obtener_todos()
        estudiantes = self.repo_estudiantes.obtener_todos()
        cursos = self.repo_cursos.obtener_todos()
        resultado = []

        for matricula in datos.values():
            if matricula["estudiante_id"] == identificador:
                estudiante = estudiantes.get(matricula["estudiante_id"])
                curso = cursos.get(matricula["curso_codigo"])

                nombre_estudiante = estudiante["nombre"] if estudiante else "No encontrado"
                nombre_curso = curso["nombre"] if curso else "No encontrado"
                resultado.append((matricula["numero"], nombre_estudiante, nombre_curso, matricula["periodo"]))
        return resultado

    def buscar_matriculas_curso(self, codigo):
        datos = self.repo_matriculas.obtener_todos()
        estudiantes = self.repo_estudiantes.obtener_todos()
        cursos = self.repo_cursos.obtener_todos()
        resultado = []

        for matricula in datos.values():
            if matricula["curso_codigo"] == codigo:
                estudiante = estudiantes.get(matricula["estudiante_id"])
                curso = cursos.get(matricula["curso_codigo"])

                nombre_estudiante = estudiante["nombre"] if estudiante else "No encontrado"
                nombre_curso = curso["nombre"] if curso else "No encontrado"
                resultado.append((matricula["numero"], nombre_estudiante, nombre_curso, matricula["periodo"]))
        return resultado