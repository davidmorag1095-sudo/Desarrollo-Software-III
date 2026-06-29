import tkinter as tk
from tkinter import messagebox

# Importar modelos
from PracticaExamen.model.beneficiario import Beneficiario
from PracticaExamen.model.recurso import Recurso
from PracticaExamen.model.asignacion import Asignacion

class GUI:
    def __init__(self, controller):
        self.controller = controller

        self.root = tk.Tk()
        self.root.title("Sistema de Ayuda Social")
        self.root.geometry("250x400")

        #Botones principales
        tk.Button(text="Registrar Beneficiario", command=self.reg_ben).pack()
        tk.Button(text="Ver Beneficiarios", command=self.ver_ben).pack()
        tk.Button(text="Buscar Beneficiario", command=self.buscar_ben).pack()
        tk.Button(text="Eliminar Beneficiario", command=self.eliminar_ben).pack()
        tk.Button(text="Por Comunidad", command=self.ben_comunidad).pack()

        tk.Button(text="Registrar Recurso", command=self.reg_rec).pack()
        tk.Button(text="Ver Recursos", command=self.ver_rec).pack()

        tk.Button(text="Registrar Asignación", command=self.reg_asig).pack()

        tk.Button(text="Top Beneficiarios", command=self.top).pack()
        tk.Button(text="Inventario Bajo", command=self.inv_bajo).pack()

        self.root.mainloop()
    #Beneficiarios
    def reg_ben(self):
        win = tk.Toplevel()
        win.title("Registrar Beneficiario")
        win.geometry("300x260")

        #Crear etiquetas y campos de entrada alineados con grid
        tk.Label(win, text="Identificación:").grid(row=0, column=0, sticky="e", padx=5, pady=3)
        entradaIdentificacionBeneficiario = tk.Entry(win)
        entradaIdentificacionBeneficiario.grid(row=0, column=1, padx=5, pady=3)

        tk.Label(win, text="Nombre:").grid(row=1, column=0, sticky="e", padx=5, pady=3)
        entradaNombreBeneficiario = tk.Entry(win)
        entradaNombreBeneficiario.grid(row=1, column=1, padx=5, pady=3)

        tk.Label(win, text="Comunidad:").grid(row=2, column=0, sticky="e", padx=5, pady=3)
        entradaComunidadBeneficiario = tk.Entry(win)
        entradaComunidadBeneficiario.grid(row=2, column=1, padx=5, pady=3)

        tk.Label(win, text="Integrantes:").grid(row=3, column=0, sticky="e", padx=5, pady=3)
        entradaCantidadIntegrantes = tk.Entry(win)
        entradaCantidadIntegrantes.grid(row=3, column=1, padx=5, pady=3)

        tk.Label(win, text="Prioridad:").grid(row=4, column=0, sticky="e", padx=5, pady=3)
        entradaPrioridadBeneficiario = tk.Entry(win)
        entradaPrioridadBeneficiario.grid(row=4, column=1, padx=5, pady=3)

        def guardar():
            try:
                #Crear la instancia de Beneficiario utilizando los valores ingresados
                beneficiario = Beneficiario(
                    entradaIdentificacionBeneficiario.get(),
                    entradaNombreBeneficiario.get(),
                    entradaComunidadBeneficiario.get(),
                    int(entradaCantidadIntegrantes.get()),
                    entradaPrioridadBeneficiario.get())

                #Registrar el beneficiario a través del controlador
                self.controller.registrar_beneficiario(beneficiario)
                messagebox.showinfo("Éxito", "Beneficiario registrado correctamente")
                win.destroy()
            except Exception as err:
                messagebox.showerror("Error", str(err))

        #Botón de guardar ocupa las dos columnas
        tk.Button(win, text="Guardar", command=guardar).grid(row=5, column=0, columnspan=2, pady=10)

    def ver_ben(self):
        data = self.controller.consultar_beneficiarios()

        if not data:
            messagebox.showinfo("Info", "Vacío")
            return

        texto = ""
        for beneficiario in data:
            texto += f"{beneficiario.identificacion} - {beneficiario.nombre} - {beneficiario.comunidad}\n"

        messagebox.showinfo("Beneficiarios", texto)

    def buscar_ben(self):
        win = tk.Toplevel()
        win.title("Buscar Beneficiario")
        win.geometry("300x120")

        tk.Label(win, text="Identificación:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        entradaIdentificacionBuscar = tk.Entry(win)
        entradaIdentificacionBuscar.grid(row=0, column=1, padx=5, pady=5)

        def buscar():
            # Buscar el beneficiario por identificación a través del controlador
            beneficiario = self.controller.buscar_beneficiario(entradaIdentificacionBuscar.get())

            if not beneficiario:
                messagebox.showerror("Error", "No existe")
                return

            messagebox.showinfo("Encontrado", f"{beneficiario.nombre} - {beneficiario.comunidad}")
            win.destroy()

        tk.Button(win, text="Buscar", command=buscar).grid(row=1, column=0, columnspan=2, pady=10)

    def eliminar_ben(self):
        win = tk.Toplevel()
        win.title("Eliminar Beneficiario")
        win.geometry("300x120")

        tk.Label(win, text="Identificación:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        entradaIdentificacionEliminar = tk.Entry(win)
        entradaIdentificacionEliminar.grid(row=0, column=1, padx=5, pady=5)

        def eliminar():
            self.controller.eliminar_beneficiario(entradaIdentificacionEliminar.get())
            messagebox.showinfo("Éxito", "Beneficiario eliminado")
            win.destroy()

        tk.Button(win, text="Eliminar", command=eliminar).grid(row=1, column=0, columnspan=2, pady=10)

    def ben_comunidad(self):
        win = tk.Toplevel()
        win.title("Beneficiarios por Comunidad")
        win.geometry("300x150")

        tk.Label(win, text="Comunidad:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        entradaComunidadFiltro = tk.Entry(win)
        entradaComunidadFiltro.grid(row=0, column=1, padx=5, pady=5)

        def listar():
            data = self.controller.listar_beneficiarios_por_comunidad(entradaComunidadFiltro.get())
            texto = "\n".join([beneficiario.nombre for beneficiario in data]) or "Vacío"
            messagebox.showinfo("Resultado", texto)
            win.destroy()

        tk.Button(win, text="Listar", command=listar).grid(row=1, column=0, columnspan=2, pady=10)

    #Recursos
    def reg_rec(self):
        win = tk.Toplevel()
        win.title("Registrar Recurso")
        win.geometry("300x260")

        tk.Label(win, text="Código:").grid(row=0, column=0, sticky="e", padx=5, pady=3)
        entradaCodigoRecurso = tk.Entry(win)
        entradaCodigoRecurso.grid(row=0, column=1, padx=5, pady=3)

        tk.Label(win, text="Nombre:").grid(row=1, column=0, sticky="e", padx=5, pady=3)
        entradaNombreRecurso = tk.Entry(win)
        entradaNombreRecurso.grid(row=1, column=1, padx=5, pady=3)

        tk.Label(win, text="Categoría:").grid(row=2, column=0, sticky="e", padx=5, pady=3)
        entradaCategoriaRecurso = tk.Entry(win)
        entradaCategoriaRecurso.grid(row=2, column=1, padx=5, pady=3)

        tk.Label(win, text="Cantidad:").grid(row=3, column=0, sticky="e", padx=5, pady=3)
        entradaCantidadRecurso = tk.Entry(win)
        entradaCantidadRecurso.grid(row=3, column=1, padx=5, pady=3)

        tk.Label(win, text="Costo:").grid(row=4, column=0, sticky="e", padx=5, pady=3)
        entradaCostoRecurso = tk.Entry(win)
        entradaCostoRecurso.grid(row=4, column=1, padx=5, pady=3)

        def guardar():
            try:
                #Crear el recurso con los valores suministrados por el usuario
                recurso = Recurso(
                    entradaCodigoRecurso.get(),
                    entradaNombreRecurso.get(),
                    entradaCategoriaRecurso.get(),
                    int(entradaCantidadRecurso.get()),
                    float(entradaCostoRecurso.get()))

                #Registrar el recurso a través del controlador
                self.controller.registrar_recurso(recurso)
                messagebox.showinfo("Éxito", "Recurso registrado")
                win.destroy()

            except Exception as err:
                messagebox.showerror("Error", str(err))

        tk.Button(win, text="Guardar", command=guardar).grid(row=5, column=0, columnspan=2, pady=10)

    def ver_rec(self):
        data = self.controller.consultar_recursos()

        texto = "\n".join([recurso.nombre for recurso in data]) or "Vacío"
        messagebox.showinfo("Recursos", texto)
    #Asignaciones
    def reg_asig(self):
        win = tk.Toplevel()
        win.title("Registrar Asignación")
        win.geometry("350x300")

        tk.Label(win, text="Código:").grid(row=0, column=0, sticky="e", padx=5, pady=3)
        entradaCodigoAsignacion = tk.Entry(win)
        entradaCodigoAsignacion.grid(row=0, column=1, padx=5, pady=3)

        tk.Label(win, text="ID Beneficiario:").grid(row=1, column=0, sticky="e", padx=5, pady=3)
        entradaIdBeneficiarioAsignacion = tk.Entry(win)
        entradaIdBeneficiarioAsignacion.grid(row=1, column=1, padx=5, pady=3)

        tk.Label(win, text="Código Recurso:").grid(row=2, column=0, sticky="e", padx=5, pady=3)
        entradaCodigoRecursoAsignacion = tk.Entry(win)
        entradaCodigoRecursoAsignacion.grid(row=2, column=1, padx=5, pady=3)

        tk.Label(win, text="Cantidad:").grid(row=3, column=0, sticky="e", padx=5, pady=3)
        entradaCantidadAsignacion = tk.Entry(win)
        entradaCantidadAsignacion.grid(row=3, column=1, padx=5, pady=3)

        tk.Label(win, text="Fecha:").grid(row=4, column=0, sticky="e", padx=5, pady=3)
        entradaFechaAsignacion = tk.Entry(win)
        entradaFechaAsignacion.grid(row=4, column=1, padx=5, pady=3)

        tk.Label(win, text="Responsable:").grid(row=5, column=0, sticky="e", padx=5, pady=3)
        entradaResponsableAsignacion = tk.Entry(win)
        entradaResponsableAsignacion.grid(row=5, column=1, padx=5, pady=3)

        def guardar():
            try:
            #Obtener beneficiario y recurso existentes a partir de los identificadores ingresados
                beneficiario = self.controller.buscar_beneficiario(entradaIdBeneficiarioAsignacion.get())
                recurso = self.controller.buscar_recurso(entradaCodigoRecursoAsignacion.get())

                if not beneficiario or not recurso:
                    raise ValueError("Datos inválidos")

                #Crear la asignación con los datos proporcionados
                asignacion = Asignacion(
                    entradaCodigoAsignacion.get(),
                    beneficiario,
                    recurso,
                    int(entradaCantidadAsignacion.get()),
                    entradaFechaAsignacion.get(),
                    entradaResponsableAsignacion.get())

                #Registrar la asignación a través del controlador
                self.controller.registrar_asignacion(asignacion)
                messagebox.showinfo("Éxito", "Asignación registrada")
                win.destroy()

            except Exception as err:
                messagebox.showerror("Error", str(err))

        tk.Button(win, text="Guardar", command=guardar).grid(row=6, column=0, columnspan=2, pady=10)
    #Reportes
    def top(self):
        data = self.controller.top()

        texto = "\n".join([f"{identificacion}: ₡{monto}" for identificacion, monto in data]) or "Vacío"
        messagebox.showinfo("Top", texto)

    def inv_bajo(self):
        win = tk.Toplevel()
        win.title("Recursos con Inventario Bajo")
        win.geometry("300x150")

        tk.Label(win, text="Límite:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        entradaLimiteInventario = tk.Entry(win)
        entradaLimiteInventario.grid(row=0, column=1, padx=5, pady=5)

        def ver():
            try:
                limite = int(entradaLimiteInventario.get())
            except ValueError:
                messagebox.showerror("Error", "Ingrese un número válido")
                return
            data = self.controller.inventario_bajo(limite)
            texto = "\n".join([recurso.nombre for recurso in data]) or "Vacío"
            messagebox.showinfo("Resultado", texto)
            win.destroy()

        tk.Button(win, text="Ver", command=ver).grid(row=1, column=0, columnspan=2, pady=10)