from typing import Dict, List, TypeVar, Generic
T = TypeVar("T")
class Repositorio(Generic[T]):
    def __init__(self) -> None:
        self._lista: List[T] = []
        self._diccionario: Dict[str, T] = {}

    def agregar(self, clave: str, objeto: T) -> None:
        if clave in self._diccionario:
            raise ValueError("Ya existe un objeto con la misma clave")
        self._lista.append(objeto)
        self._diccionario[clave] = objeto

    def buscar(self, clave: str):
        return self._diccionario.get(clave)

    def listar(self) -> List[T]:
        return list(self._lista)

    def eliminar(self, clave: str) -> None:
        objeto = self._diccionario.pop(clave, None)
        if objeto is not None:
            #Remover de la lista también.
            if objeto in self._lista:
                self._lista.remove(objeto)
