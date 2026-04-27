class Repositorio:
    """
    Repositorio genérico que almacena y gestiona objetos de cualquier tipo.

    Este repositorio mantiene internamente una lista de elementos para permitir
    recorridos completos y un diccionario para búsquedas rápidas por clave.
    """

    def __init__(self) -> None:
        # Lista que contiene todos los objetos guardados en el repositorio
        self.lista_elementos: list = []
        # Diccionario que mapea una clave única al objeto correspondiente
        self.diccionario_elementos: dict = {}

    def add(self, clave, objeto) -> None:
        """Agrega un objeto al repositorio usando la clave indicada.

        Args:
            clave: Identificador único del objeto.
            objeto: Instancia del objeto a almacenar.

        Raises:
            ValueError: Si la clave ya existe en el repositorio.
        """
        if clave in self.diccionario_elementos:
            raise ValueError("Elemento ya existe")

        self.lista_elementos.append(objeto)
        self.diccionario_elementos[clave] = objeto

    def get(self, clave):
        """Obtiene un objeto por su clave, o None si no existe."""
        return self.diccionario_elementos.get(clave)

    def get_all(self) -> list:
        """Devuelve una lista con todos los objetos almacenados."""
        return self.lista_elementos

    def delete(self, clave) -> None:
        """Elimina un objeto del repositorio por su clave."""
        objeto = self.diccionario_elementos.pop(clave, None)
        if objeto:
            self.lista_elementos.remove(objeto)
