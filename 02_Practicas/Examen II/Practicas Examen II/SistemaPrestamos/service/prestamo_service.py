class Prestamo_service:
    def __init__(self, repository):
        self.repo_prestamo = repository()

    def save_prestamo(self,id, estudiante_id, equipo_codigo, fecha_prestamo, fecha_devolucion, estado):
        if not id.strip() or not estudiante_id.strip() or not equipo_codigo.strip() or not fecha_prestamo.strip() or not fecha_devolucion.strip() or not estado:
            raise ValueError("Debe ingresar un dato")

        if self.repo_prestamo.serch_by_id(id):
            raise ValueError("Ya existe un prestamo con ese ID")

        return self.repo_prestamo.save(id, estudiante_id, equipo_codigo, fecha_prestamo, fecha_devolucion, estado)
#---------------------------------------------------------------------------------------------------------
    def get_all_prestamo(self):
        if self.repo_prestamo.get_all() is None:
            raise ValueError("No hay prestamos registrados")

        return self.repo_prestamo.get_all()
#---------------------------------------------------------------------------------------------------------
    def serch_by_id(self,id):
        if not id.strip():
            raise ValueError("Debe ingresar un dato")

        if self.repo_prestamo.serch_by_id(id) is None:
            raise ValueError("No hay prestamos registrados con ese ID")

        return self.repo_prestamo.serch_by_id(id)
#---------------------------------------------------------------------------------------------------------
    def update_prestamo(self, id, estudiante_id, equipo_codigo, fecha_prestamo, fecha_devolucion, estado):
        if not id.strip() or not estudiante_id.strip() or not equipo_codigo.strip() or not fecha_prestamo.strip() or not fecha_devolucion.strip() or not estado.strip():
            raise ValueError("Debe ingresar un dato")

        if self.repo_prestamo.serch_by_id(id) is None:
            raise ValueError("No hay prestamos registrados con ese ID")

        return self.repo_prestamo.update(id, estudiante_id, equipo_codigo, fecha_prestamo, fecha_devolucion, estado)
#---------------------------------------------------------------------------------------------------------
    def delete_prestamo(self, id):
        if not id.strip():
            raise ValueError("Debe ingresar un dato")

        if self.repo_prestamo.serch_by_id(id) is None:
            raise ValueError("No hay prestamos registrados con ese ID")

        return self.repo_prestamo.delete(id)
#---------------------------------------------------------------------------------------------------------