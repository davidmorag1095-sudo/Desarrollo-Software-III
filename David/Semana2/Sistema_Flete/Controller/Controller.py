from David.Semana2.Sistema_Flete.Model.repositorio import Repositorio
from David.Semana2.Sistema_Flete.Model.FleteModel import Flete
class Controlador:

    def __init__(self):
        self.repo_clientes = ()
        self.repo_fletes = Repositorio

    def agregar(self, codigo, nombre, telefono):
        tupla = (nombre, telefono)
        self.repo_clientes.agregar

    def consultar_clientes(self):
        """Retorna diccionario de clientes"""
        return self.repo_clientes.consultar()

    def agregar_flete(self, numero, destino, monto, clave_cliente):
        """
        Crea y guarda un flete asociado a un cliente
        el usuario debe incluir la clave del cliente
        """
        self.repo_clientes = self.repo_clientes
    #Se verifica la clave del cliente exista en el diccionario
    if clave_cliente in diccionario_clientes:
        #Se extraen los datos de la tupla en las variables
        nombre_cliente, telefono_cliente = diccionario_clientes[clave_cliente]
        #Se crea el cliente
        cliente = Cliente(clave_cliente,nombre_cliente,telefono_cliente)

