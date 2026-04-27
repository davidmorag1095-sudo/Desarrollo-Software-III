class Controlador:
    def __init__(self, servicio):
        self.servicio = servicio

    def crear_estudiante(self, identificador, nombre, carrera):
        return self.servicio.registrar_estudiante(identificador, nombre, carrera)

    def crear_curso(self, codigo, nombre, creditos):
        return self.servicio.registrar_curso(codigo, nombre, creditos)

    def crear_matricula(self, numero, est, curso, periodo):
        return self.servicio.registrar_matricula(numero, est, curso, periodo)

    def obtener_estudiantes(self):
        return self.servicio.ver_estudiantes()

    def obtener_cursos(self):
        return self.servicio.ver_cursos()

    def obtener_matriculas(self):
        return self.servicio.ver_matriculas()

    def buscar_matriculas_estudiante(self, identificador):
        return self.servicio.buscar_matriculas_estudiante(identificador)

    def buscar_matriculas_curso(self, codigo):
        return self.servicio.buscar_matriculas_curso(codigo)