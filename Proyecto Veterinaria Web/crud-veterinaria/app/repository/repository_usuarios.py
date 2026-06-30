from app.config.database_conexion import SessionLocal
from app.entity.usuariosORM import UsuariosORM


class RepositoryUsuarios:

    def __init__(self):
        self.db = SessionLocal()

    def create_default_user(self):
        usuario = self.get("admin")
        if not usuario:
            usuario = UsuariosORM(usuario="admin", clave="admin123")
            self.db.add(usuario)
            self.db.commit()
        return usuario

    def get(self, usuario):
        return self.db.query(UsuariosORM).filter_by(usuario=usuario).first()

