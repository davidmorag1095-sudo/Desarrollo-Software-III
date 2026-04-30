class BeneficiarioService:
    def __init__(self, repositorio):
        """
        Servicio encargado de manejar operaciones sobre beneficiarios.

        Args:
            repositorio: Repositorio genérico encargado de almacenar instancias de Beneficiario.
        """
        # Repositorio genérico que almacena Beneficiario
        self.repositorio = repositorio
        # Set de comunidades para permitir consultas rápidas de comunidades únicas
        self.comunidades: set[str] = set()

    def registrar(self, beneficiario):
        """
        Registra un nuevo beneficiario en el repositorio y actualiza la lista de comunidades.

        Args:
            beneficiario: Instancia de Beneficiario a registrar.
        """
        # Utilizamos la identificación del beneficiario como clave única
        self.repositorio.add(beneficiario.identificacion, beneficiario)
        # Actualizar el conjunto de comunidades únicas con la comunidad del nuevo beneficiario
        self.comunidades.add(beneficiario.comunidad)

    def listar(self):
        """Retorna una lista de todos los beneficiarios registrados."""
        return self.repositorio.get_all()

    def buscar(self, identificacion):
        """Obtiene un beneficiario por su identificación."""
        return self.repositorio.get(identificacion)

    def eliminar(self, identificacion):
        """Elimina un beneficiario por su identificación."""
        self.repositorio.delete(identificacion)

    def listar_por_comunidad(self, comunidad: str):
        """Retorna los beneficiarios que pertenecen a una comunidad específica."""
        # Filtramos por cada beneficiario en el repositorio cuya comunidad coincida
        return [beneficiario for beneficiario in self.repositorio.get_all() if beneficiario.comunidad == comunidad]

    #Nombre para mantener compatibilidad con el controlador
    por_comunidad = listar_por_comunidad