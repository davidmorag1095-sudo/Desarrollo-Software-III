from Model.fletes_model import Fletes

class FletesService:
    def __init__(self, repository, service_cliente):
        self.repo = repository(Fletes.from_dict, 'flete.json')
        self.service_cliente = service_cliente
    #----------------------------------------------------------------------------------------
    def registrar(self, id_flete, id_cliente, ciudad, destino, peso):
        if not id_flete.strip() or not id_cliente.strip() or not ciudad.strip() or not destino.strip():
            raise ValueError('Debe de completar los campos vacios')
        
        if self.repo.list_id(id_flete):
            raise ValueError(f'Ya existe un flete con el mismo ID: {id_flete}')
        if not self.service_cliente.buscar_cliente(id_cliente):
            raise ValueError(f'El cliente ingresado no existe, intente con uno valido. {id_cliente}')
        

        if peso < 0:
            raise ValueError('El peso no puede ser negativo.')
        
        nuevo = Fletes(id_flete, id_cliente, ciudad, destino, peso)
        return self.repo.guardar(nuevo)
    #----------------------------------------------------------------------------------------
    def mostrar(self):
        datos_encontrados = self.repo.listar()
        if not datos_encontrados:
            raise ValueError('No se encontraron datos')
        return datos_encontrados
    #----------------------------------------------------------------------------------------
    def buscar(self, id_flete):
        datos_encontrados = self.repo.buscar_flete_por_cliente(id_flete)
        if not datos_encontrados:
            raise ValueError('No se encontro')
        return datos_encontrados
        
    #----------------------------------------------------------------------------------------