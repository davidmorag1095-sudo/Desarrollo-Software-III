class Libro:
    def __init__(self, codigo, titulo, autor):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
    #----------------------------------------------------------------
    #Metodo toString()
    def __str__(self):
        return f"{self.codigo}|{self.titulo}|{self.autor}"
    #----------------------------------------------------------------

