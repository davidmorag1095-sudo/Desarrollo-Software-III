class CategoriaService:
    def __init__(self, repository):
        self.repo_categoria = repository()

    def save_categoria(self,id, nombre):

        if not id.strip() or not nombre.strip():
            raise ValueError("Debe ingresar un dato")

        if self.repo_categoria.serch_by_id(id):
            raise ValueError("El dato ya existe")

        return self.repo_categoria.save_estudent(id, nombre)
#---------------------------------------------------------------------------------------------------------
    def get_all_categoria(self):
        if self.repo_categoria.get_all() is None:
            raise ValueError("No hay categorias a mostrar")

        return self.repo_categoria.get_all()
#---------------------------------------------------------------------------------------------------------
    def serch_by_id(self,id):
        if not id.strip():
            raise ValueError("Debe ingresar un dato")

        if self.repo_categoria.serch_by_id(id) is None:
            raise ValueError("No existe ninguna categoria con ese ID")

        return self.repo_categoria.serch_by_id(id)
#---------------------------------------------------------------------------------------------------------
    def update_categoria(self, id, nombre):
        if not id.strip() or not nombre.strip():
            raise ValueError("Debe ingresar un dato")

        if self.repo_categoria.serch_by_id(id) is None:
            raise ValueError("No existe ninguna categoria con ese ID")

        return self.repo_categoria.update(id, nombre)
#---------------------------------------------------------------------------------------------------------
    def delete_categoria(self, id):
        if not id.strip():
            raise ValueError("Debe ingresar un dato")

        if self.repo_categoria.serch_by_id(id) is None:
            raise ValueError("No existe ninguna categoria con ese ID")

        return self.repo_categoria.delete(id)
#---------------------------------------------------------------------------------------------------------


