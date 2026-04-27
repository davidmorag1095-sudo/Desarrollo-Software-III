import tkinter as tk

class VistaCursos:
    def __init__(self, controlador):
        self.controlador = controlador

        self.win = tk.Toplevel()
        self.win.title("Cursos")
        self.win.geometry("300x250")

        tk.Label(self.win, text="Codigo").pack(pady=5)
        self.codigo = tk.Entry(self.win)
        self.codigo.pack(pady=5)

        tk.Label(self.win, text="Nombre").pack(pady=5)
        self.nombre = tk.Entry(self.win)
        self.nombre.pack(pady=5)

        tk.Label(self.win, text="Creditos").pack(pady=5)
        self.creditos = tk.Entry(self.win)
        self.creditos.pack(pady=5)

        tk.Button(self.win, text="Guardar", command=self.guardar).pack(pady=15)

    def guardar(self):
        resultado = self.controlador.crear_curso(self.codigo.get(), self.nombre.get(), self.creditos.get())
        print(resultado)