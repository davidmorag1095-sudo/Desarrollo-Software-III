class Controlador:
    def __init__(self, ben_service, rec_service, asig_service, report_service):
        self.ben_service = ben_service
        self.rec_service = rec_service
        self.asig_service = asig_service
        self.report_service = report_service


    #Beneficiarios

    def registrar_beneficiario(self, beneficiario):
        """Registra un beneficiario mediante el servicio correspondiente."""
        self.ben_service.registrar(beneficiario)

    def consultar_beneficiarios(self):
        return self.ben_service.listar()

    def buscar_beneficiario(self, identificacion):
        return self.ben_service.buscar(identificacion)

    def eliminar_beneficiario(self, identificacion):
        self.ben_service.eliminar(identificacion)

    def listar_beneficiarios_por_comunidad(self, comunidad):
        return self.ben_service.listar_por_comunidad(comunidad)

    #Recursos

    def registrar_recurso(self, recurso):
        """Registra un recurso mediante el servicio correspondiente."""
        self.rec_service.registrar(recurso)

    def consultar_recursos(self):
        return self.rec_service.listar()

    def buscar_recurso(self, codigo):
        return self.rec_service.buscar(codigo)

    def eliminar_recurso(self, codigo):
        self.rec_service.eliminar(codigo)

    def listar_recursos_por_categoria(self, categoria):
        return self.rec_service.listar_por_categoria(categoria)
    #Asignaciones
    def registrar_asignacion(self, asignacion):
        """Registra una asignación mediante el servicio correspondiente."""
        self.asig_service.registrar(asignacion)

    def consultar_asignaciones(self):
        return self.asig_service.listar()

    def listar_asignaciones_por_beneficiario(self, identificacion):
        return self.asig_service.listar_por_beneficiario(identificacion)

    def listar_asignaciones_por_fecha(self, fecha):
        return self.asig_service.listar_por_fecha(fecha)

    def historial_entregas(self):
        return self.asig_service.listar()


    #Reportes
    def top(self):
        return self.report_service.top_beneficiarios()

    def inventario_bajo(self, limite):
        return self.report_service.inventario_bajo(limite)

    def costo_por_categoria(self):
        return self.report_service.costo_por_categoria()

    def beneficiarios_por_comunidad(self):
        """Expone el reporte de beneficiarios por comunidad al GUI."""
        return self.report_service.beneficiarios_por_comunidad()