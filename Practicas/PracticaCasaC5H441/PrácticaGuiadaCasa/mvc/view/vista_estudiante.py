import tkinter as tk

class VistaEstudiantes:
    def __init__(self, controlador):
        self.controlador = controlador

        self.win = tk.Toplevel()
        self.win.title("Estudiantes")
        self.win.geometry("300x250")

        tk.Label(self.win, text="ID").pack(pady=5)
        self.id = tk.Entry(self.win)
        self.id.pack(pady=5)

        tk.Label(self.win, text="Nombre").pack(pady=5)
        self.nombre = tk.Entry(self.win)
        self.nombre.pack(pady=5)

        tk.Label(self.win, text="Carrera").pack(pady=5)
        self.carrera = tk.Entry(self.win)
        self.carrera.pack(pady=5)

        tk.Button(self.win, text="Guardar", command=self.guardar).pack(pady=15)

    def guardar(self):
        resultado = self.controlador.crear_estudiante(self.id.get(), self.nombre.get(), self.carrera.get())
        print(resultado)