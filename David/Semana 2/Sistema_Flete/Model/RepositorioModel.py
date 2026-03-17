class Repositorio():

    def agregar(self, clave, valor):
        """
        Agregar un objeto al diccionario

        Parametros:
        clave(cualquiera): clave la cual se usara en el diccionario
        valor(cualquiera): el valor del asociado a la clave anterior dentro
        """
        self.diccionario.update({clave:valor})