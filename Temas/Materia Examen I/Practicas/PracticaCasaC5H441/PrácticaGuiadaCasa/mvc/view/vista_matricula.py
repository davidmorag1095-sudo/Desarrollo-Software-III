import tkinter as tk

class VistaMatriculas:
    def __init__(self, controlador):
        self.controlador = controlador

        self.win = tk.Toplevel()
        self.win.title("Matriculas")
        self.win.geometry("300x300")

        tk.Label(self.win, text="Numero").pack(pady=5)
        self.numero = tk.Entry(self.win)
        self.numero.pack(pady=5)

        tk.Label(self.win, text="ID Estudiante").pack(pady=5)
        self.estudiante = tk.Entry(self.win)
        self.estudiante.pack(pady=5)

        tk.Label(self.win, text="Codigo Curso").pack(pady=5)
        self.curso = tk.Entry(self.win)
        self.curso.pack(pady=5)

        tk.Label(self.win, text="Periodo").pack(pady=5)
        self.periodo = tk.Entry(self.win)
        self.periodo.pack(pady=5)

        tk.Button(self.win, text="Guardar", command=self.guardar).pack(pady=15)

    def guardar(self):
        resultado = self.controlador.crear_matricula(self.numero.get(), self.estudiante.get(), self.curso.get(), self.periodo.get())
        print(resultado)