from typing import TypeVar, Generic
#Clase generica que permite almacenar objetos,
# evitando duplicación de codigo

T = TypeVar("T")

class Repositorio(Generic[T]):
    def __init__(self):
        self.lista = []

    def agregar(self, objeto:T) -> None:
        self.lista.append(objeto)

    def consultar(self) -> list[T]:
        return self.lista

    def buscar(self, indice: int):
        if 0 <= indice < len(self.lista):
            return self.lista[indice]
        return None
