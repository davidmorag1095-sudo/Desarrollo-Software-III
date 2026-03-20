class Repertorio:
    # ----------------------------------------------------------------------------------------
    def __init__(self):
        self.diccionarioEstudiantes = {}
        self.diccionarioLibros = {}
        self.diccionarioPrestamos = {}
        self.categorias = set()

    #----------------------------------------------------------------------------------------
    #Agregar
    def agregar_estudiante(self, carnet, tuplaEstudiante):
        self.diccionarioEstudiantes.update({carnet, tuplaEstudiante})

    def agregar_libro(self, codigoLibro, libro, titulo, autor, categoria):
        self.diccionarioLibros.update({codigoLibro, libro, titulo, autor, categoria})

    def agregar_prestamo(self, numeroPrestamo, estudianteAsociado, libroAsociado, fecha):
        self.diccionarioPrestamos.update({numeroPrestamo, estudianteAsociado, libroAsociado, fecha})

    #----------------------------------------------------------------------------------------
    #Consultar
    def consultar_libro(self):
        return self.diccionarioLibros

    def consultar_estudiante(self):
        return self.diccionarioEstudiantes

    def consultar_prestamo(self):
        return self.diccionarioPrestamos

    #----------------------------------------------------------------------------------------
    #Buscar
    def buscar_estudiante(self, carnet):
        if carnet in self.diccionarioEstudiantes:
            return self.diccionarioEstudiantes[carnet]
        return None

    def buscar_Libro(self,codigoLibro):
        if codigoLibro in self.diccionarioLibros:
            return self.diccionarioLibros[codigoLibro]
        return None
    #----------------------------------------------------------------------------------------


