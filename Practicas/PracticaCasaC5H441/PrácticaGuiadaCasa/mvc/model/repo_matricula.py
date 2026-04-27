import json
import os

class RepoMatriculas:
    def __init__(self):
        self.archivo = "matriculas.json"
        self.datos = self.cargar()

    def cargar(self):
        if not os.path.exists(self.archivo):
            return {}
        with open(self.archivo, "r") as f:
            return json.load(f)

    def guardar(self):
        with open(self.archivo, "w") as f:
            json.dump(self.datos, f, indent=4)

    def agregar(self, matricula):
        if matricula.numero in self.datos:
            return False
        self.datos[matricula.numero] = matricula.to_dict()
        self.guardar()
        return True

    def obtener_todos(self):
        return self.datos