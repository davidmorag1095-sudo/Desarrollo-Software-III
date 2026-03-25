class Prestamo:
    def __init__(self, usuario, libro):
        self.usuario = usuario
        self.libro = libro
    #----------------------------------------------------------
    #Metodo to String
    def __str__(self):
        return f"{self.usuario.nombre} | {self.libro.titulo}"
    #----------------------------------------------------------



