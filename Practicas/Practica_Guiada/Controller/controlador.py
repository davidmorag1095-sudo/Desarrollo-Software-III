from Practicas.Practica_Guiada.Model.ClienteModel import Cliente
from Practicas.Practica_Guiada.Model import Repositorio
from Practicas.Practica_Guiada.Model.FleteModel import Flete

class Controlador:
    """
    Clase controladora (MVC)
    Coordina la comunicacion entre la vista y el modelo
    """

    def __init__(self):
        """Inicializa los repositorios"""
        self.repo_clientes = Repositorio()
        self.repo_fletes = Repositorio()

    def agregar_cliente(self, codigo, nombre, telefono):
        """Almacena los datos de un cliente, coloca el codigo como clave en el diccionario
        y agrega el resto de datos a una tupla para incluirlos como valor asociado a dicha clave en el diccionario"""

        tupla = (nombre, telefono)
        self.repo_clientes.agregar(codigo, tupla)

    def consultar_clientes(self):
        """Retorna el diccionario de clientes"""
        return self.repo_clientes.consultar()

    def agregar_flete(self, numero, destino, monto, clave_cliente):
        """
        Crea y guarda un flete asociado a un cliente, el usuario debe incluir la clave del cliente
        """

        diccionario_clientes = self.repo_clientes.consultar()
        #Se verifica que la clave realmente exista en el diccionario
        if clave_cliente in diccionario_clientes:
            #Se extrae los datos de la tupla
            nombre_cliente, telefono_cliente = diccionario_clientes[clave_cliente]

            #Se crea el cliente
            cliente = Cliente(clave_cliente, nombre_cliente, telefono_cliente)

            #se crrea el flete con el cliente
            flete = Flete(numero, destino, monto, cliente)
            self.repo_fletes.agregar(numero, flete)

    def consultar_fletes(self):
        """Retorna el diccionario de fletesp"""
        return self.repo_fletes.consultar()

