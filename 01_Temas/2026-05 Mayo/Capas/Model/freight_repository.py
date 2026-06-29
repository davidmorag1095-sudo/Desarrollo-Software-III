import os.path
import json
from CAPAS.model.freight import Freight

class FreightRepository:
    """"Este repositorio gestiona la persistencia de los fletes"""
    #El repositorio recibe el nombre del archivo donde se guardaran los fletes
    def __init__(self,filename="freights.json"):
        self.filename=filename

        #lista con todos los fletes registrados
        self._freights=[]

        #Diccionario que agrupa fletes por identificador de clientes la llave es customer_id y el valor es una lista
        #de fletes
        self._freights_by_customer_id={}
        #Se intenta cargar la información ya guardada
        #self._load() por el momento no existe

    def _load(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename,"r",enconding="utf-8") as file:
             data=json.load(file)

        for item in data:
            freight=Freight.from_dict(item)
            self._freights.append(freight)
            #Si  no existe una lista para ese cliente, la crea
            if freight.customer_id not in self._freights_by_customer_id:
                self._freights_by_customer_id[freight.customer_id]=[]