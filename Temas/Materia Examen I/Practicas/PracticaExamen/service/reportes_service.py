class ReportService:
    def __init__(self, asig_service, rec_service, ben_service):
        self.asig_service = asig_service
        self.rec_service = rec_service
        self.ben_service = ben_service

    def top_beneficiarios(self):
        conteo = {}

        for asignacion in self.asig_service.listar():
            identificacion = asignacion.beneficiario.identificacion
            #Acumulamos el costo total de cada asignación por beneficiario
            conteo[identificacion] = conteo.get(identificacion, 0) + asignacion.costo_total()

        return sorted(conteo.items(), key=lambda x: x[1], reverse=True)

    def inventario_bajo(self, limite):
        """Obtiene los recursos cuyo inventario se encuentra por debajo de un límite dado."""
        # Accedemos al repositorio del servicio de recursos para obtener todos los recursos
        return [recurso for recurso in self.rec_service.repositorio.get_all() if recurso.cantidad < limite]

    def costo_por_categoria(self):
        costos: dict[str, float] = {}

        for asignacion in self.asig_service.listar():
            categoria = asignacion.recurso.categoria
            #Acumulamos el costo total por cada categoría de recurso
            costos[categoria] = costos.get(categoria, 0) + asignacion.costo_total()

        return costos
    def beneficiarios_por_comunidad(self):
        """Devuelve un mapeo de comunidades a la cantidad de beneficiarios en cada una."""
        conteo: dict[str, int] = {}
        for beneficiario in self.ben_service.listar():
            conteo[beneficiario.comunidad] = conteo.get(beneficiario.comunidad, 0) + 1
        return conteo