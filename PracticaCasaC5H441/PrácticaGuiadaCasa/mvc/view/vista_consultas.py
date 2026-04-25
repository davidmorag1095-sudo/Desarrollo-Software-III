import tkinter as tk
from tkinter import ttk

class VistaConsultas:
    def __init__(self, controlador):
        self.controlador = controlador

        self.win = tk.Toplevel()
        self.win.title("Consultas")
        self.win.geometry("800x400")

        frame_botones = tk.Frame(self.win)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Ver estudiantes", command=self.ver_estudiantes).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Ver cursos", command=self.ver_cursos).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Ver matriculas", command=self.ver_matriculas).grid(row=0, column=2, padx=5)

        frame_busqueda = tk.Frame(self.win)
        frame_busqueda.pack(pady=10)

        tk.Label(frame_busqueda, text="ID estudiante").grid(row=0, column=0, padx=5)
        self.entry_estudiante = tk.Entry(frame_busqueda)
        self.entry_estudiante.grid(row=0, column=1, padx=5)
        tk.Button(frame_busqueda, text="Buscar", command=self.buscar_por_estudiante).grid(row=0, column=2, padx=5)

        tk.Label(frame_busqueda, text="Codigo curso").grid(row=1, column=0, padx=5)
        self.entry_curso = tk.Entry(frame_busqueda)
        self.entry_curso.grid(row=1, column=1, padx=5)
        tk.Button(frame_busqueda, text="Buscar", command=self.buscar_por_curso).grid(row=1, column=2, padx=5)

        self.tabla = ttk.Treeview(self.win)
        self.tabla.pack(fill="both", expand=True, pady=10)

    def resetear_tabla(self):
        self.tabla.delete(*self.tabla.get_children())
        self.tabla["columns"] = ()

    def ver_estudiantes(self):
        datos = self.controlador.obtener_estudiantes()
        self.resetear_tabla()

        self.tabla["columns"] = ("id", "nombre", "carrera")
        self.tabla["show"] = "headings"

        self.tabla.heading("id", text="ID")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("carrera", text="Carrera")

        for estudiante in datos.values():
            self.tabla.insert("", "end", values=(estudiante["identificador"], estudiante["nombre"], estudiante["carrera"]))

    def ver_cursos(self):
        datos = self.controlador.obtener_cursos()
        self.resetear_tabla()

        self.tabla["columns"] = ("codigo", "nombre", "creditos")
        self.tabla["show"] = "headings"

        self.tabla.heading("codigo", text="Codigo")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("creditos", text="Creditos")

        for curso in datos.values():
            self.tabla.insert("", "end", values=(curso["codigo"], curso["nombre"], curso["creditos"]))

    def ver_matriculas(self):
        datos = self.controlador.obtener_matriculas()
        self.resetear_tabla()

        self.tabla["columns"] = ("numero", "estudiante", "curso", "periodo")
        self.tabla["show"] = "headings"

        self.tabla.heading("numero", text="Numero")
        self.tabla.heading("estudiante", text="Estudiante")
        self.tabla.heading("curso", text="Curso")
        self.tabla.heading("periodo", text="Periodo")

        for matricula in datos:
            self.tabla.insert("", "end", values=matricula)

    def buscar_por_estudiante(self):
        identificador = self.entry_estudiante.get()
        datos = self.controlador.buscar_matriculas_estudiante(identificador)
        self.resetear_tabla()

        self.tabla["columns"] = ("numero", "estudiante", "curso", "periodo")
        self.tabla["show"] = "headings"

        self.tabla.heading("numero", text="Numero")
        self.tabla.heading("estudiante", text="Estudiante")
        self.tabla.heading("curso", text="Curso")
        self.tabla.heading("periodo", text="Periodo")

        for matricula in datos:
            self.tabla.insert("", "end", values=matricula)

    def buscar_por_curso(self):
        codigo = self.entry_curso.get()
        datos = self.controlador.buscar_matriculas_curso(codigo)
        self.resetear_tabla()

        self.tabla["columns"] = ("numero", "estudiante", "curso", "periodo")
        self.tabla["show"] = "headings"

        self.tabla.heading("numero", text="Numero")
        self.tabla.heading("estudiante", text="Estudiante")
        self.tabla.heading("curso", text="Curso")
        self.tabla.heading("periodo", text="Periodo")

        for matricula in datos:
            self.tabla.insert("", "end", values=matricula)