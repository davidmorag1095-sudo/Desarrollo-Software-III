import os
import json
from InventarioGamer.mvc.Model.periferico import Periferico

dir_data = os.path.dirname(os.path.abspath(__file__))
archivo = os.path.join(dir_data, 'periferico.json')


class Repository:
    def __init__(self):
        self.perifericos = [ ]
        self._load()

    def _load(self):
        if not os.path.exists(archivo):
            return

        with open(archivo, 'r', encoding='utf-8') as file:
            listaPerifericosJson = json.load(file)

            for items  in listaPerifericosJson:
                nuevo_periferico = Periferico(
                    items['Modelo'],
                    items['Tipo'],
                    items['Precio']
                )
                self.perifericos.append(nuevo_periferico)

    def save(self):
        os.makedirs(os.path.dirname(archivo), exist_ok=True)
        datos_para_guardar = [ ]

        for items in self.perifericos:
            diccionario = items.to_dict()
            datos_para_guardar.append(diccionario)

        with open(archivo, 'w', encoding='utf-8') as file:
            json.dump(datos_para_guardar, file, indent=4, ensure_ascii=False)



    def save(self):
        os.makedirs(os.path.dirname(archivo), exist_ok=True)
        datos_para_guardar = [ ]

        for item in self.perifericos:
            diccionario = item.to_dict()
            datos_para_guardar.append(diccionario)

        with open(archivo, 'w', encoding='utf-8') as file:
            json.dump(datos_para_guardar, file, indent=4, ensure_ascii=False)




