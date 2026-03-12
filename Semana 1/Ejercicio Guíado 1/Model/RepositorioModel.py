from typing import TypeVar, Generic


#T representa un tipo genérico,
# puede ser cliente, flete o cualquiera
T = TypeVar("T")


class Repositorio:
    """Clase generica que permite almacenar objetos en una lista
    esta clase se reuriliza para distintos tipos de datos"""

    def __init__(self):
        #Inicializamos una lista
        self.lista = []

    def agregar(self, objeto: T):
        """" Agrega un objeto en la lista
        Parametros:
           objeto(T) objeto de tipo genérico
        """
        self.lista.append(objeto)

    def consultar(self) -> list [T]:
        """Retorna todos los objetos almacenados en la lista

        retorna:
            list[T]: Lista de objetos
        """
        return self.lista

    def modificar(self, indice: int, nuevoObjeto: T) -> bool:
        if 0 <= indice < len(self.lista):
            self.lista[indice] = nuevoObjeto
            return True
        return False
