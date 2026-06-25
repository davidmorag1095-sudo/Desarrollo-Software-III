class Libro:
    def __init__(self, codigoLibro, titulo, autor, categoria):
        self.codigoLibro = codigoLibro
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria

    def mostrarInfo(self):
        return f"Codigo del libro: {self.codigoLibro} \n Titulo: {self.titulo}\n Autor: {self.autor}\n Categoria: {self.categoria}"