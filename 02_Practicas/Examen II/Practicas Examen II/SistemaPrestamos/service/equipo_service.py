class Equipo_service:
    def __init__(self, repository):
        self.repo_categoria = repository()

    def save_equipo(self,codigo, nombre, marca, estado, categoria_id):
        if not codigo.strip() or not nombre.strip() or not marca.strip() or not estado.strip():
            raise ValueError ("Debe ingresar datos")

        if self.repo_categoria.serch_by_codigo(codigo):
            raise ValueError("Ya existe un categoria con ese codigo")

        return self.repo_categoria.save(codigo, nombre, marca, estado, categoria_id)
#---------------------------------------------------------------------------------------------------------
    def get_all_equipo(self):
        if self.repo_categoria.get_all() is None:
            raise ValueError("No hay equipos registrados")

        return self.repo_categoria.get_all()
#---------------------------------------------------------------------------------------------------------
    def serch_by_codigo(self,codigo):
        if not codigo.strip():
            raise ValueError("Debe ingresar datos")

        if self.repo_categoria.get_by_codigo(codigo) is None:
            raise ValueError("No hay equipos registrados con el codigo ingresado")

        return self.repo_categoria.get_by_codigo(codigo)
#---------------------------------------------------------------------------------------------------------
    def update_by_codigo(self,codigo, nombre, marca, estado, categoria_id):
        if not codigo.strip():
            raise ValueError("Debe ingresar datos")

        if self.repo_categoria.get_by_codigo(codigo) is None:
            raise ValueError("No hay equipos registrados con el codigo ingresado")

        return self.repo_categoria.update(codigo, nombre, marca, estado, categoria_id)
#---------------------------------------------------------------------------------------------------------
    def delete_by_codigo(self,codigo):
        if not codigo.strip():
            raise ValueError("Debe ingresar datos")

        if self.repo_categoria.get_by_codigo(codigo) is None:
            raise ValueError("No hay equipos registrados con el codigo ingresado")

        return self.repo_categoria.delete(codigo)
#---------------------------------------------------------------------------------------------------------


