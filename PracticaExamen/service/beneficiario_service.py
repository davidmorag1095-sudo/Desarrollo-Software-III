class BeneficiarioService:
    def __init__(self, repo):
        # Repositorio genérico que almacena Beneficiario
        self.repo = repo
        # Set de comunidades para permitir consultas rápidas de comunidades únicas
        self.comunidades: set[str] = set()

    def registrar(self, beneficiario):
        # Utilizamos la identificación del beneficiario como clave única
        self.repo.add(beneficiario.identificacion, beneficiario)
        # Actualizar el conjunto de comunidades únicas con la comunidad del nuevo beneficiario
        self.comunidades.add(beneficiario.comunidad)

    def listar(self):
        """Retorna una lista de todos los beneficiarios registrados."""
        return self.repo.get_all()

    def buscar(self, identificacion):
        """Obtiene un beneficiario por su identificación."""
        return self.repo.get(identificacion)

    def eliminar(self, identificacion):
        """Elimina un beneficiario por su identificación."""
        self.repo.delete(identificacion)

    def listar_por_comunidad(self, comunidad: str):
        """Retorna los beneficiarios que pertenecen a una comunidad específica."""
        # Filtramos por cada beneficiario en el repositorio cuya comunidad coincida
        return [beneficiario for beneficiario in self.repo.get_all() if beneficiario.comunidad == comunidad]

    #Nombre para mantener compatibilidad con el controlador
    por_comunidad = listar_por_comunidad