class RecursoService:
    def __init__(self, repositorio):
        """
        Servicio encargado de manejar operaciones sobre recursos.

        Args:
            repositorio: Repositorio genérico encargado de almacenar instancias de Recurso.
        """
        # Repositorio genérico que almacena Recurso
        self.repositorio = repositorio
        # Set de categorías únicas registradas
        self.categorias: set[str] = set()

    def registrar(self, recurso):
        """
        Registra un nuevo recurso en el repositorio y actualiza el conjunto de categorías.

        Args:
            recurso: Instancia de Recurso a registrar.
        """
        self.repositorio.add(recurso.codigo, recurso)
        self.categorias.add(recurso.categoria)

    def listar(self):
        """Devuelve la lista de todos los recursos registrados."""
        return self.repositorio.get_all()

    def buscar(self, codigo):
        """Obtiene un recurso por su código."""
        return self.repositorio.get(codigo)

    def listar_por_categoria(self, categoria: str):
        """Obtiene los recursos que pertenecen a una categoría específica."""
        # Recorremos todos los recursos del repositorio y seleccionamos los que coinciden con la categoría
        return [recurso for recurso in self.repositorio.get_all() if recurso.categoria == categoria]

    #Nombre para compatibilidad con el controlador
    por_categoria = listar_por_categoria

    def eliminar(self, codigo):
        """Elimina un recurso por su código."""
        self.repositorio.delete(codigo)
