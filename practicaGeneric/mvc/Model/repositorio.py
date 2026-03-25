from math import trunc
from typing import TypeVar, Generic, List

T = TypeVar("T")
#--------------------------------------------------------------
class Repositorio(Generic[T]):
    def __init__(self):
        self.datos: List[T] = [ ]

    def agregar(self, objeto):
        self.datos.append(objeto)

    def consultar(self):
        return self.datos

    def buscar(self, condicion):
        for item in self.datos:
            if condicion(item):
                return item
        return None
    #--------------------------------------------------------------
    def editar(self, indice: int, nuevoObjeto:T) -> bool:
        if 0 <= indice < len(self.datos):
            self.datos[indice] = nuevoObjeto
            return True
        return False










