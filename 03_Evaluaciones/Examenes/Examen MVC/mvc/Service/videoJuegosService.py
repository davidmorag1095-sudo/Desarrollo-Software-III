from typing import List

from Examen.mvc.Model.videoJuegos import VideoJuego
from Examen.mvc.Repository.repositorio import Repositorio

class VideoJuegoService:
    def __init__(self) -> None:
        self.repositorio = Repositorio()
    #Registrar Videojuegos
    def registrar(self,videoJuego: VideoJuego) -> None:
        if self.repositorio.buscar(videoJuego.codigo):
            raise ValueError("Codigo incorrecto")

        if not videoJuego.titulo or not videoJuego.desarrollador or not videoJuego.categoria or not videoJuego.licencia:
            raise ValueError("Debe llenar todos los campos")

        if int(videoJuego.licencia)<0:
            raise ValueError("Licencia invalida! porfavor intente de nuevo")

        juego = videoJuego

        self.repositorio.agregar(videoJuego.clave, juego)
    #Buscar videoJuegos
    def buscar(self, codigo: str) -> VideoJuego | None:
        return self.repositorio.buscar(codigo)
    #Listar VideoJuegos
    def listar(self) -> List[VideoJuego]:
        return self.repositorio.listar()
    #Listar por paises
    def listar_por_tipo(self, tipo: str) -> List[VideoJuego]:
        return [videoJuego for videoJuego in self.repositorio.listar() if videoJuego.categoria == categoria]


