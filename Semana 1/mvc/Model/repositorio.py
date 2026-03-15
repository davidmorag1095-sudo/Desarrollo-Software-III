from typing import TypeVar, Generic, List

tipoGen = TypeVar('tipoGen')

class Repositorio(Generic[T]):
    def __init__(self):
        self.lista = []

    def agregar(self, obj: T):
        self.lista.append(obj)

    def consultar(self) -> List[T]:
        return self.lista

    def modificar(self, indice: int, nuevoObjeto: T) -> bool:
        if 0 <= indice < len(self.lista):
            self.lista[indice] = nuevoObjeto
            return True
        return False