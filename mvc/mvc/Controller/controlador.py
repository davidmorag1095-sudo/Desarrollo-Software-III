from mvc.Model.clienteModel import Cliente
from mvc.Model.fleteModel import Flete
from mvc.Model.repositorio import Repositorio

class Controlador:
    """Clase controlador MVC
    coordina la comnicacion entre vista y modelo"""

    def __init__(self):
        """Inicializa los repositorios genericos"""
        self.repo_clientes = Repositorio[Cliente]()
        self.repo_fletes = Repositorio[Flete]()

    def agregar_cliente(self, codigo, nombre, telefono):
        cliente = Cliente(codigo, nombre, telefono)
        self.repo_clientes.agregar(cliente)

    def consultar_clientes(self):
        return self.repo_clientes.consultar()
    def modificar_cliente(self, indice, codigo, nombre, telefono):
        nuevo = Cliente(codigo, nombre, telefono)
        return self.repo_clientes.modificar(indice, nuevo)


    '//Fletes'

    def agregar_flete(self, numero, destino, monto, indice_cliente):
        """"Crea y guarda un flete asociado a un cliente"""
        clientes = self.repo_clientes.consultar()

        if 0 < indice_cliente < len(clientes):
            cliente = clientes[indice_cliente]
            flete=Flete(numero, destino, monto, cliente)
            self.repo_fletes.agregar(flete)

    def consultar_fletes(self):
        return self.repo_fletes.consultar()

    def modificar_flete(self, indice, numero, destino, monto, indice_cliente):
        """Modificar un flete"""

        clientes = self.repo_clientes.consultar()
        if 0 < indice_cliente < len(clientes):
            nuevo = Flete(numero, destino, monto, clientes[indice_cliente])
            fletes  = self.repo_fletes.consultar()
            if 0 < indice < len(fletes):
                return self.repo_fletes.modificar(indice,nuevo)
            return False
        return False