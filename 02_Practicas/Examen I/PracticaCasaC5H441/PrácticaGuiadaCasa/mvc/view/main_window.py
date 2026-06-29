import tkinter as tk
from mvc.view.vista_estudiante import VistaEstudiantes
from mvc.view.vista_curso import VistaCursos
from mvc.view.vista_matricula import VistaMatriculas
from mvc.view.vista_consultas import VistaConsultas

class MainWindow:
    def __init__(self, controlador):
        self.controlador = controlador

        self.root = tk.Tk()
        self.root.title("Sistema academico")
        self.root.geometry("300x200")

        tk.Button(self.root, text="Estudiantes", command=self.abrir_estudiantes).pack(pady=10)
        tk.Button(self.root, text="Cursos", command=self.abrir_cursos).pack(pady=10)
        tk.Button(self.root, text="Matriculas", command=self.abrir_matriculas).pack(pady=10)
        tk.Button(self.root, text="Consultas", command=self.abrir_consultas).pack(pady=10)
        self.root.mainloop()

    def abrir_estudiantes(self):
        VistaEstudiantes(self.controlador)

    def abrir_cursos(self):
        VistaCursos(self.controlador)

    def abrir_matriculas(self):
        VistaMatriculas(self.controlador)

    def abrir_consultas(self):
        VistaConsultas(self.controlador)