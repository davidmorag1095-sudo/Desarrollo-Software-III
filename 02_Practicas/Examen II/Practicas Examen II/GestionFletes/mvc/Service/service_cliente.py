from Model.cliente_model import Cliente
class ServiceCliente:
    def __init__(self, repositorio):
        self.repo = repositorio(Cliente.from_dict, 'cliente.json')
    #----------------------------------------------------------------------------------------
    def registrar(self, id, nombre, telefono):
        if not id.strip() or not nombre.strip():
            raise ValueError('Debe de completar los espacios en blanco')
        
        if self.repo.list_id(id):
            raise ValueError(f'Ya existe un cliente con el mismo Id:{id} ')
        
        nuevo_cliente = Cliente(id,nombre,telefono)
        return self.repo.guardar(nuevo_cliente)
    #----------------------------------------------------------------------------------------
    def mostrar(self):
        datos_encontrados = self.repo.listar()
        if not datos_encontrados:
            raise ValueError('No se encontraron datos')
        return datos_encontrados
    #----------------------------------------------------------------------------------------
    def buscar(self, id):
        datos_encontrados = self.repo.list_id(id)
        if not datos_encontrados:
            raise ValueError('No se encontro')

        return datos_encontrados
    #----------------------------------------------------------------------------------------
    


