class ControllerCliente:
    def __init__(self, service):
        self.service = service

    def registrar_cliente(self, id, nombre, telefono):
        try:
            return self.service.registrar(id,nombre,telefono)
        except Exception as error:
            return f'{error}'
        
    def mostrar_clientes(self):
        try:
            return self.service.mostrar()
        except Exception as error:
            return f'{error}'
        
    def buscar_cliente(self, id):
        try:
            return self.service.buscar(id)
        except Exception as error:
            return f'{error}'
        

