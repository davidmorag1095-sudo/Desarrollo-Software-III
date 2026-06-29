class Estudiante_service:
    def __init__(self, repository):
        self.repo_estudiantes = repository()

    def save_estudiante(self, id, nombre, correo, carrera):
        if not id.strip() or not nombre.strip() or not correo.strip() or not carrera.strip():
            raise ValueError("Debe ingresar datos")

        if self.repo_estudiantes.serch_by_id(id):
            raise ValueError("Estudiante ya existe")

        return self.repo_estudiantes.save(id, nombre, correo, carrera)
#---------------------------------------------------------------------------------------------------------
    def get_all_estudiante(self):
        if self.repo_estudiantes.get_all() is None:
            raise ValueError("Error! No existen estudiantes")

        return self.repo_estudiantes.get_all()
#---------------------------------------------------------------------------------------------------------
    def serch_by_id(self,id):
        if not id.strip():
            raise ValueError("Debe ingresar datos")

        if self.repo_estudiantes.serch_by_id(id) is None:
            raise ValueError("Error! No se encontro estudiante con el ID ingresado")

        return self.repo_estudiantes.serch_by_id(id)
#---------------------------------------------------------------------------------------------------------
    def update_estudiante(self, id, nombre, correo, carrera):
        if not id.strip() or not nombre.strip() or not correo.strip() or not carrera.strip():
            raise ValueError("Debe ingresar datos")

        if self.repo_estudiantes.serch_by_id(id) is None:
            raise ValueError("Error! No se encontro estudiante con el ID ingresado")

        return self.repo_estudiantes.update(id, nombre, correo, carrera)
#---------------------------------------------------------------------------------------------------------
    def delete_estudiante(self, id):
        if not id.strip():
            raise ValueError("Debe ingresar datos")

        if self.repo_estudiantes.serch_by_id(id) is None:
            raise ValueError("Error! No se encontro estudiante con ID ingresado")
#---------------------------------------------------------------------------------------------------------


