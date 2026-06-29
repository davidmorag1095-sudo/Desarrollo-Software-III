import uuid

class GestorUsuarios:
    """Clase encargada de la gestion de usuarios del sistema.
    No depende de socket ni de la red maneja sesiones mediantes IDs únicos"""

    def __init__(self):
        #Diccionario:session_id-> nombre_usuarios
        self._usuarios={}

    def crear_session(self,nombre):
        """"Crea una nueva sesión para un usuario"""
        session_id=str(uuid.uuid4())
        self._usuarios[session_id]=nombre
        return session_id

    def eliminar_sesion(self,session_id):
        return self._usuarios.pop(session_id)

    def obtener_nombre(self,session_id):
        return self._usuarios.get(session_id)

    def listar(self):
        return list(self._usuarios.values())

    def existe(self,nombre):
        return nombre in self._usuarios.values()




