from Semana1.Sistema_Flete.Model.RepositorioModel import Repositorio
from Semana1.Sistema_Flete.Model.ClienteModel import Cliente
from Semana1.Sistema_Flete.Model.FleteModel import Flete
class Controller:
    def __init__(self):
        self.repoClientes = Repositorio[Cliente]()
        self.repoFletes = Repositorio[Flete]()