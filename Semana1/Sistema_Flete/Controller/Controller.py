#Importaciones para poder hacer instancias de las clases
from Semana1.Sistema_Flete.Model.RepositorioModel import Repositorio
from Semana1.Sistema_Flete.Model.ClienteModel import Cliente
from Semana1.Sistema_Flete.Model.FleteModel import Flete
class Controller:
    # -----------------------------------------------------------------------
    #Constructor
    def __init__(self):
        self.repo_Clientes = Repositorio[Cliente]()
        self.repoFletes = Repositorio[Flete]()
#-----------------------------------------------------------------------
    #Agregar un Cliente
    def agregar_Cliente(self, codigo, nombre, telefono):
        cliente = Cliente(codigo, nombre, telefono)
        self.repo_Clientes.consultar()
    #Consultar un Cliente
    def consultar_Clientes(self):
        return self.repo_Clientes.consultar()

    #Modificar Cliente
    def modificar_Cliente(self, indice, codigo, nombre, telefono):
        nuevo = Cliente(codigo, nombre, telefono)
        return self.repo_Clientes.modificar(nuevo)

    #Agregar Flete
    def agregar_Flete(self, numero, destino, monto, indice_Cliente):
        """Crea y guarda un Flete asociado a un cliente"""
        clientes = self.repo_Clientes.consultar()

        if 0 < indice_Cliente < len(clientes):
            cliente = clientes[indice_Cliente]
            flete = Flete(numero, destino, monto, cliente)
            self.repoFletes.agregar(flete)

# -----------------------------------------------------------------------
    #Consultar Flete
    def consultar_Fletes(self):
        return self.repoFletes.consultar()

    #Modificar Flete
    def modificar_Flete(self, indice, numero, destino, monto, indice_Cliente):
        clientes = self.repo_Clientes.consultar()
        if 0 < indice_Cliente < len(clientes):
            nuevo = Flete(numero, destino, monto, clientes[indice_Cliente])
            fletes = self.repoFletes.consultar()

            if 0 < indice < len(fletes):
                return self.repoFletes.modificar(indice, nuevo)
            return False
        return False
#-----------------------------------------------------------------------