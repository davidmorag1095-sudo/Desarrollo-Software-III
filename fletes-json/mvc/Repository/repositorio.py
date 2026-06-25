import os
import json

class Repositorio:
    def __init__(self, from_dict, nombre_archivo):
        self.from_dict = from_dict
        self.lista = []
        dir_data = os.path.dirname(os.path.abspath(__file__))
        self.archivo = os.path.abspath(os.path.join(dir_data,'..','..','Data',nombre_archivo))
        self._load()
    #-==--==-=--==-=-=--=-==-=-=-=--==-=-=--==-=-=--=-=-=-=-==-=-=--=-=-==-=-=--==-=--==--==-=-=-=--==-=--==-=-=-=-=#
    def _load(self):
        if not os.path.exists(self.archivo):
            return None
        with open(self.archivo, 'r', encoding = 'utf-8') as file:
            data = json.load(file)
            for items in data: 
                self.lista.append(self.from_dict(items))
            return True
        
    #-==--==-=--==-=-=--=-==-=-=-=--==-=-=--==-=-=--=-=-=-=-==-=-=--=-=-==-=-=--==-=--==--==-=-=-=--==-=--==-=-=-=-=#
    def _save(self):
        os.makedirs(os.path.dirname(self.archivo), exist_ok=True) 

        dato_para_guardar = []
        for items in self.lista:
            diccionario = items.to_dict()
            dato_para_guardar.append(diccionario)

        with open(self.archivo, 'w', encoding='utf-8') as file:
            json.dump(dato_para_guardar, file, ensure_ascii=False, indent=4)
            return True
    #-==--==-=--==-=-=--=-==-=-=-=--==-=-=--==-=-=--=-=-=-=-==-=-=--=-=-==-=-=--==-=--==--==-=-=-=--==-=--==-=-=-=-=#

    #Guardar
    def guardar(self, objeto):
        self.lista.append(objeto)
        return self._save()
    

    #Listar todos
    def listar(self):
        return self.lista
    

    #Buscar
    def list_id(self, id):
        resultado = []
        for items in self.lista:
            if items:
                if str(items.get_id()) == str(id): #error
                    resultado.append(items)
        return resultado
                    

