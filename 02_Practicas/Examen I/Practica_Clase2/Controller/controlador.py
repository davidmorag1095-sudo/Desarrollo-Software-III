from Practicas.Practica_Clase2.Model.prestamo import Prestamo
from Practicas.Practica_Clase2.Model.repositorio import Repositorio
from Practicas.Practica_Clase2.Model.estudiante import Estudiante
from Practicas.Practica_Clase2.Model.libro import Libro


class Controlador:
    def __init__(self):
        self.repo_estudiantes = Repositorio()
        self.repo_libros = Repositorio()
        self.repo_prestamos = Repositorio()

    #-----------------------------------------------------------------------
    #Agregar estudiante
    def agregar_estudiante(self, carnet, nombre, carrera):
        estudiante = Estudiante(carnet, nombre, carrera)
        tupla_estudiante = (nombre, carrera)
        self.repo_estudiantes.agregar_estudiante(carnet, tupla_estudiante)

    #Mostrar estudiante
    def mostrar_estudiantes(self):
        return self.repo_estudiantes.mostrar_estudiante()

    #-----------------------------------------------------------------------
    #Agregar Libro
    def agregar_libro(self,codigoLibro, titulo, autor, categoria):
        tupla_libro =(titulo, autor, categoria)
        self.repo_libros.agregar_libro(codigoLibro,tupla_libro)

    #Mostrar Libro
    def mostrar_libros(self):
        return self.repo_libros.mostrar_libro()

    def agregar_prestamo(self, numeroPrestamo, estudianteAsociado, libroAsociado, fecha):
        tupla_prestamo = (estudianteAsociado, libroAsociado, fecha)
        self.repo_prestamos.agregar_prestamo(numeroPrestamo, tupla_prestamo)
    #-----------------------------------------------------------------------------
    ##Consultar
    def consultar_estudiantes(self):
        return self.repo_estudiantes.mostrar_estudiante()

    def consultar_libros(self):
        return self.repo_libros.mostrar_libro()

    def consultar_prestamos(self):
        return self.repo_prestamos.mostrar_prestamo()

    def consultar_categorias(self):
        categorias = set()
        libros = self.repo_libros.mostrar_libro()
        for libro in libros.values():
            categorias.add(libro[2])  # <- aquí está el fix

        return categorias