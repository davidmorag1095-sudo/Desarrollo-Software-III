from Examen.mvc.Model.usos import Usos
from Examen.mvc.Repository.repositorio import Repositorio

class UsosService:
    def __init__(self, repositorio: object, repo_Jugador: object, repo_VideoJuego: object) -> None:
        self.repositorio = repositorio
        self.repo_Jugador = repo_Jugador
        self.repo_VideoJuego = repo_VideoJuego

    #Registrar Usos
    def registrar(self, codigo, iD_Jugador, codigoJuego, fecha, cantidad_Licencias):
        jugador = self.repo_Jugador.buscar(iD_Jugador)
        juego = self.repo_VideoJuego.buscar(codigoJuego)
        if not jugador:
            raise ValueError("Jugador no encontrado")

        if not juego:
            raise ValueError("Juego no encontrado")

        if int(cantidad_Licencias) <= 0:
            raise ValueError("El cantidad debe ser mayor que 0")

        if int(cantidad_Licencias) > juego.licencia:
            raise ValueError("No hay licencias suficientes para el juego")

        uso = Usos(jugador, juego, fecha, int(cantidad_Licencias))

        juego.licencia = int(cantidad_Licencias)
        self.repositorio.agregar(uso)

    def listarUso(self):
        return self.repositorio.listar()

    def buscar(self, identificacion: str) -> Usos | None:
        return self.repositorio.buscar(identificacion)




