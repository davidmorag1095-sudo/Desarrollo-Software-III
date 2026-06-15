class Estudiante:
    def __init__(self, id_estudiante=None, nombre="", correo="", carrera=""):

        # El ID puede ser None cuando el estudiante todavía no ha sido guardado.
        self.id_estudiante = id_estudiante

        # Nombre completo del estudiante.
        self.nombre = nombre

        # Correo electrónico del estudiante.
        self.correo = correo

        # Carrera del estudiante.
        self.carrera = carrera

    def __str__(self):
        """
        Devuelve una representación en texto del estudiante.

        Esto permite imprimir un objeto Estudiante de forma legible.
        """

        return f"ID: {self.id_estudiante} | Nombre: {self.nombre} | Correo: {self.correo} | Carrera: {self.carrera}"
