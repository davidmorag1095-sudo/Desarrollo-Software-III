from app.repository.repository_usuarios import RepositoryUsuarios


class ServiceUsuarios:

    def __init__(self):
        self.repo = RepositoryUsuarios()

    def crear_usuario_inicial(self):
        return self.repo.create_default_user()

    def iniciar_sesion(self, usuario, clave):
        datos = self.repo.get(usuario)
        if datos and datos.clave == clave:
            return {"mensaje": "Inicio de sesión correcto", "usuario": datos.usuario}
        return None

