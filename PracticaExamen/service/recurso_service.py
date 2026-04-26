class RecursoService:
    def __init__(self, repo):
        # Repositorio genérico que almacena Recurso
        self.repo = repo
        # Set de categorías únicas registradas
        self.categorias: set[str] = set()

    def registrar(self, recurso):
        self.repo.add(recurso.codigo, recurso)
        self.categorias.add(recurso.categoria)

    def listar(self):
        """Devuelve la lista de todos los recursos registrados."""
        return self.repo.get_all()

    def buscar(self, codigo):
        """Obtiene un recurso por su código."""
        return self.repo.get(codigo)

    def listar_por_categoria(self, categoria: str):
        """Obtiene los recursos que pertenecen a una categoría específica."""
        # Recorremos todos los recursos del repositorio y seleccionamos los que coinciden con la categoría
        return [recurso for recurso in self.repo.get_all() if recurso.categoria == categoria]

    #Nombre para compatibilidad con el controlador
    por_categoria = listar_por_categoria

    def eliminar(self, codigo):
        """Elimina un recurso por su código."""
        self.repo.delete(codigo)
