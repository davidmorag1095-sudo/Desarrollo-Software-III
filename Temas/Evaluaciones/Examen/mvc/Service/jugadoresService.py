from typing import List

from Examen.mvc.Model.jugadores import Jugador
from Examen.mvc.Repository.repositorio import Repositorio

class JugadorService:
    def __init__(self):
        self.repositorio = Repositorio[Jugador]()
    #Registrar los jugadores
    def registrar(self, jugador):
        #Verificaciones
        if not jugador.id or not jugador.nombre or not jugador.correo or not jugador.pais:
            raise ValueError("Debe ingresar todos los datos para registrar un jugador")

        if self.repositorio.buscar(clave=jugador.id):
            raise ValueError("Jugador ya existe")
        jugador = Jugador(jugador.id, jugador.nombre, jugador.correo)
        self.repositorio.agregar(jugador.id, jugador)

    #Buscar los jugadores
    def buscar(self, identificacion: str) -> Jugador | None:
        return self.repositorio.buscar(identificacion)

    #Listar los jugadores
    def listar(self) -> List[Jugador]:
        return self.repositorio.listar()

    #Listar por pais
    """def listar_por_pais(self, pais: str) -> List[Jugador]:
        jugadores_Por_Pais: List[Jugador] = []

        return jugadores_Por_Pais"""  #No logre hacerlo funcionar quede atorado
