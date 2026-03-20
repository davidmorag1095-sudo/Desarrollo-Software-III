class Repositorio:
    # ----------------------------------------------------------------------------------------
    def __init__(self):
        self.diccionarioEstudiantes = {}
        self.diccionarioLibros = {}
        self.diccionarioPrestamos = {}
        self.categorias = set()

    #----------------------------------------------------------------------------------------
    #Agregar
    def agregar_estudiante(self, carnet, tupla_estudiante):
        self.diccionarioEstudiantes.update({carnet, tupla_estudiante})

    def agregar_libro(self, codigoLibro, libro, titulo, autor, categoria):
        self.diccionarioLibros.update({codigoLibro, libro, titulo, autor, categoria})

    def agregar_prestamo(self, numeroPrestamo, estudianteAsociado, libroAsociado, fecha):
        self.diccionarioPrestamos.update({numeroPrestamo, estudianteAsociado, libroAsociado, fecha})

    #----------------------------------------------------------------------------------------
    #Mostrar
    def mostrar_libro(self):
        return self.diccionarioLibros

    def mostrar_estudiante(self):
        return self.diccionarioEstudiantes

    def mostrar_prestamo(self):
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


