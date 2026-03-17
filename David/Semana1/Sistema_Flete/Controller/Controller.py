#Importaciones para poder hacer instancias de las clases
from Model.RepositorioModel import Repositorio
from Model.ClienteModel import Cliente
from Model.FleteModel import Flete
class Controller:
    # -----------------------------------------------------------------------
    #Constructor
    def __init__(self):
        self.repo_Clientes = Repositorio[Cliente]()
        self.repoFletes = Repositorio[Flete]()
#-----------------------------------------------------------------------
    #Agregar un Cliente
    def agregar_cliente(self, codigo, nombre, telefono):
        cliente = Cliente(codigo, nombre, telefono)
        self.repo_Clientes.consultar()
#Consultar un Cliente
    def consultar_clientes(self):
        return self.repo_Clientes.consultar()

    #Modificar Cliente
    def modificar_cliente(self, indice, codigo, nombre, telefono):
        nuevo = Cliente(codigo, nombre, telefono)
        return self.repo_Clientes.modificar(indice, nuevo)

    #Agregar Flete
    def agregar_flete(self, numero, destino, monto, indice_Cliente):
        """"Crea y guarda un flete asociado a un cliente"""""
        clientes = self.repo_Clientes.consultar()

        if 0 <= indice_Cliente < len(clientes):
            cliente = clientes[indice_Cliente]
            flete = Flete(numero, destino, monto, cliente)
            self.repoFletes.agregar(flete)
# -----------------------------------------------------------------------
    #Consultar Flete
    def consultar_fletes(self):
        return self.repoFletes.consultar()

    #Modificar Flete
    def modificar_flete(self, indice, numero, destino, monto, indice_cliente):
        """Modificar un flete"""""

        clientes = self.repo_Clientes.consultar()
        if 0 < indice_cliente < len(clientes):
            nuevo = Flete(numero, destino, monto, clientes[indice_cliente])
            fletes  = self.repoFletes.consultar()
            if 0 < indice < len(fletes):
                return self.repoFletes.modificar(indice,nuevo)
            return False
        return False
#-----------------------------------------------------------------------