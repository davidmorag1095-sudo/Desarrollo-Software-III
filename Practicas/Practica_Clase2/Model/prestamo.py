class Prestamo:
    def _init_(self, numeroPrestamo, estudianteAsociado, libroAsociado, fecha):
        self.numeroPrestamo = numeroPrestamo
        self.estudianteAsociado = estudianteAsociado
        self.libroAsociado = libroAsociado
        self.fecha = fecha

    def mostrarInfo(self):
        return f"Numero de restamo:{self.numeroPrestamo}\nEstudiante asociado:{self.estudianteAsociado}\nLibro asociado{self.libroAsociado}\nFecha:{self.fecha}"