from mvc.model.cliente_model import ClienteModel
class ClienteService:
    def __init__(self, repositorio):
        self.repository = repositorio(ClienteModel.from_dict, 'cliente.json')

    def save_cliente(self, id, nombre, telefono):
        if not id.strip() or not nombre.strip():
            raise ValueError('Debe de completar los espacios en blanco')

        if self.repository.list_id(id):
            raise ValueError(f'Ya existe un cliente con el mismo Id:{id} ')

        nuevo_cliente = ClienteModel(id, nombre, telefono)
        return self.repository.guardar(nuevo_cliente)
#------------------------------------------------------------------------------------------------------------
    def get_all_clientes(self):
        if self.repository.list() is None:
            raise ValueError("No hay clientes registrados")
        return self.repository.list()
#------------------------------------------------------------------------------------------------------------
    def serch_cliente(self, id):
        if not id.strip():
            raise ValueError("Debe ingresar datos")

        cliente_encontrado = self.repository.buscar(id)

        if cliente_encontrado is None:
            raise ValueError("No hay clientes registrados")

        return cliente_encontrado
#------------------------------------------------------------------------------------------------------------
    def update_cliente(self, id, nombre, telefono):
        if not id.strip() or not nombre.strip() or not telefono.strip():
            raise ValueError("Debe ingresar datos")

        encontrado = self.repository.buscar(id)
        if encontrado is None:
            raise ValueError("No hay clientes registrados")

        return encontrado
#------------------------------------------------------------------------------------------------------------







