class Repositorio():
    """clase que permite almacenar objetos en un diccionario"""

    def __init__(self):
        'Inicializa el diccionario'
        self.diccionario = {}

    def agregar(self, clave, valor):
        """Agrega un objeto al diccionario
        Parametros:
            clave (cualquiera, puede ser String, int): la clave que se usara en el diccionario
            valor (cualquiera): el valor asociado a la clave anterior dentro del diccionario

        """
        self.diccionario.update({clave: valor})

    def consultar(self):
        """retorna los elementos almacenados en el diccionario

            Retorna: un diccionario
            """
        return self.diccionario

    def modificar(self, clave, nuevoValor):
        if clave in self.diccionario:
            self.diccionario[clave] = nuevoValor
            return "Modificado correctamente"
        else:
            return "Clave no encontrada"

    def eliminar(self, clave):
        if clave in self.diccionario:
            del self.diccionario[clave]
            return "Eliminado correctamente"
        else:
            return "Clave no encontrada"

