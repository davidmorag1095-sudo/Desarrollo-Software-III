class VideoJuego:
    def __init__(self, codigo, titulo, desarrollador, categoria, licencia):
        self.codigo = codigo
        self.titulo = titulo
        self.desarrollador = desarrollador
        self.categoria = categoria
        self.licencia = licencia


    def __str__(self) -> str:
        return f'{self.codigo} {self.titulo} {self.desarrollador} {self.categoria} {self.licencia}'



