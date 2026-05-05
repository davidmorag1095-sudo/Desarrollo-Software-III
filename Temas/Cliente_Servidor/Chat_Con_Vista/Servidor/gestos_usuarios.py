import uuid


class GestorUsuarios:
    """
    Clase encargada de la gestión de usuarios del
    sistema.
    No depende de socket ni de la red
    Maneja sesiones mediante IDS únicos
    """

    def __init__(self):
        #Diccionario: session_id -> nombre de usuario_usuario
        self.usuarios = {}

    def crear_session(self, nombre):
        """
        Crea una nueva sesión para un usuario
        """
        session_id = str(uuid.uuid4())
        self.usuarios[session_id] = nombre
        return session_id

    #----------------------------------------------------------
    def eliminar_sesion(self, session_id):
        return self.usuarios.pop(session_id)

    #----------------------------------------------------------
    def obtener_nombre(self, session_id):
        return self.usuarios.get(session_id)

    #----------------------------------------------------------
    def listar(self):
        return list(self.usuarios.values())

    #----------------------------------------------------------
    def existe(self, nombre):
        return nombre in self.usuarios.values()
