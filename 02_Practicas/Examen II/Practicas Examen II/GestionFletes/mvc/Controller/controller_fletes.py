class ControllerFlete:
    def __init__(self, service):
        self.service = service

    # ----------------------------------------------------------------------------------------
    def registrar_flete(self, id_flete, id_cliente, ciudad, destino, peso):
        try:
            return self.service.registrar(id_flete, id_cliente, ciudad, destino, peso)
        except Exception as error:
            return f'{error}'
        # ----------------------------------------------------------------------------------------
    def mostrar_fletes(self):
        try:
            return self.service.mostrar()
        except Exception as error:
            return f'{error}'
        # ----------------------------------------------------------------------------------------
    def buscar_flete(self, id_flete):
        try:
            return self.service.buscar(id_flete)
        except Exception as error:
            return f'{error}'
        
        