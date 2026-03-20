from Practicas.Practica_Clase2.Model.estudiante import Estudiante
from Practicas.Practica_Clase2.Model.repositorio import Repertorio
from Practicas.Practica_Clase2.Model.estudiante import Estudiante
from Practicas.Practica_Clase2.Model.prestamo import Prestamo
class Controlador:
    def __init__(self):
        self.repo_Clientes = Repositorio[Cliente]()
        self.repoFletes = Repositorio[Flete]()
        self.repoPrestamos = Repositorio[restamo]()