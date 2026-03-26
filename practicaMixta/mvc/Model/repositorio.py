from typing import TypeVar,Generic

T = TypeVar("T")

class Repositorio(Generic[T]):
    def __init__(self):
        self.diccionario = {}

    def agregar(self,clave, valor):
        self.diccionario.update({clave: valor})

    def consultar(self):
        return self.diccionario


    def consultarUno(self,clave):
        if clave in self.diccionario:
            return self.diccionario[clave]
        return None


    def eliminar(self, clave):
        if clave in self.diccionario:
            del self.diccionario[clave]
            return True
        return False


    def modificar(self, clave, valor):
        if clave in self.diccionario:
            self.diccionario[clave] = valor
            return True
        return False






