class Libro:
    def __init__(self, codigo="", titulo="", autor="", categoria=""):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria

    def __str__(self):
        return f"Codigo: {self.codigo} | Titulo: {self.titulo} | Autor: {self.autor} | Categoria: {self.categoria}"
