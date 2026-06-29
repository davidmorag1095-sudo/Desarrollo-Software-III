from typing import List

from Examen.mvc.Model.jugadores import Jugador
from Examen.mvc.Model.usos import Usos
from Examen.mvc.Model.videoJuegos import VideoJuego
from Examen.mvc.Service.jugadoresService import JugadorService
from Examen.mvc.Service.usosService import UsosService
from Examen.mvc.Service.videoJuegosService import VideoJuegoService

class Controlador:
    def __init__(self) -> None:
        self.jugadoresService = JugadorService()
        #self.usosService = UsosService() Tuve que comentar esta linea debido a que si no el main tan siquiera se mostraba
        self.videoJuegosService = VideoJuegoService()

    #Metodos para jugadores
    def registrar_Jugador(self, jugador: Jugador) -> None:
        self.jugadoresService.registrar(jugador)

    def buscar_Jugador(self, identificacion: str) -> Jugador | None:
        return self.jugadoresService.buscar(identificacion)

    def listar_Jugadores(self) -> List[Jugador]:
        return self.jugadoresService.listar()

    """def listar_Jugadores_por_pais(self, pais: str) -> List[Jugador]:
        return self.jugadoresService.listar_por_pais(pais)"""

    #Metodos para VideoJuegos
    def registrar_VideoJuego(self, videoJuego: VideoJuego) -> None:
        self.videoJuegosService.registrar(videoJuego)

    def buscar_VideoJuego(self, numero: str) -> VideoJuego | None:
        return self.videoJuegosService.buscar(numero)

    def listar_VideoJuego(self) -> List[VideoJuego]:
        return self.videoJuegosService.listar()

    def listar_VideoJuego_por_tipo(self, tipo: str) -> List[VideoJuego]:
        return self.videoJuegosService.listar_por_tipo(tipo)

    #Metodos para Usos
    def registrar_Usos(self, usos: Usos) -> None:
        self.usosService.registrar(usos)

    def buscar_Usos(self, codigo: str) -> Usos | None:
        return self.usosService.buscar(codigo)

    def listar_Usos(self) -> List[Usos]:
        return self.usosService.listarUso()

    #def listar_usos_por_jugador(self, identificacion: str) -> List[Usos]:
        return self.usosService.listar_por_jugador(identificacion)

    #def listar_usos_por_fecha(self, fecha: str) -> List[Usos]:
        return self.usosService.listar_por_fecha(fecha)
