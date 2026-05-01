"""Interfaz gráfica del sistema hotelero basada en Tkinter.

La clase :class:`GUI` construye una aplicación de escritorio para
interactuar con el sistema de gestión hotelera. El menú principal
permite acceder a tres módulos: gestión de huéspedes, gestión de
habitaciones y gestión de reservas. Cada módulo cuenta con sus
propias ventanas de entrada que permiten realizar operaciones de
registro, consulta, búsqueda y eliminación sin utilizar datos
predefinidos. Los nombres de variables y métodos son descriptivos para
facilitar la lectura y el mantenimiento del código.
"""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

from ..controller.controlador import Controlador
from ..model.huesped import Huesped
from ..model.habitacion import Habitacion
from ..model.reserva import Reserva


class GUI:
    """Clase que representa la interfaz gráfica de la aplicación."""

    def __init__(self, controlador: Controlador) -> None:
        self.controlador = controlador
        self.root = tk.Tk()
        self.root.title("Sistema de Gestión Hotelera")
        self.root.geometry("300x300")
        self.crear_menu_principal()

    def crear_menu_principal(self) -> None:
        """Crea el menú principal con botones para cada módulo."""
        lbl_titulo = tk.Label(self.root, text="Menú principal", font=("Arial", 14, "bold"))
        lbl_titulo.pack(pady=10)

        btn_huespedes = tk.Button(self.root, text="Gestión de huéspedes", command=self.mostrar_modulo_huespedes)
        btn_huespedes.pack(pady=5, fill=tk.X, padx=20)

        btn_habitaciones = tk.Button(self.root, text="Gestión de habitaciones", command=self.mostrar_modulo_habitaciones)
        btn_habitaciones.pack(pady=5, fill=tk.X, padx=20)

        btn_reservas = tk.Button(self.root, text="Gestión de reservas", command=self.mostrar_modulo_reservas)
        btn_reservas.pack(pady=5, fill=tk.X, padx=20)

        btn_salir = tk.Button(self.root, text="Salir", command=self.root.destroy)
        btn_salir.pack(pady=20, fill=tk.X, padx=20)

    # ---------- MÓDULO HUESPEDES ----------
    def mostrar_modulo_huespedes(self) -> None:
        """Ventana para gestionar huéspedes."""
        ventana = tk.Toplevel(self.root)
        ventana.title("Gestión de huéspedes")
        ventana.geometry("400x400")
        # Título
        tk.Label(ventana, text="Gestión de huéspedes", font=("Arial", 12, "bold")).pack(pady=10)
        # Botones de opciones
        tk.Button(ventana, text="Registrar huésped", command=self.formulario_registro_huesped).pack(pady=5, fill=tk.X, padx=20)
        tk.Button(ventana, text="Listar huéspedes", command=self.listar_huespedes).pack(pady=5, fill=tk.X, padx=20)
        tk.Button(ventana, text="Buscar huésped", command=self.formulario_buscar_huesped).pack(pady=5, fill=tk.X, padx=20)
        tk.Button(ventana, text="Eliminar huésped", command=self.formulario_eliminar_huesped).pack(pady=5, fill=tk.X, padx=20)
        tk.Button(ventana, text="Listar por país", command=self.formulario_listar_huespedes_por_pais).pack(pady=5, fill=tk.X, padx=20)

    def formulario_registro_huesped(self) -> None:
        """Formulario para registrar un nuevo huésped."""
        win = tk.Toplevel(self.root)
        win.title("Registrar huésped")
        win.geometry("350x300")
        # Etiquetas y campos
        tk.Label(win, text="Identificación:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        entrada_identificacion = tk.Entry(win)
        entrada_identificacion.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(win, text="Nombre completo:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        entrada_nombre = tk.Entry(win)
        entrada_nombre.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(win, text="País:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        entrada_pais = tk.Entry(win)
        entrada_pais.grid(row=2, column=1, padx=5, pady=5)

        def guardar_huesped() -> None:
            identificacion = entrada_identificacion.get().strip()
            nombre = entrada_nombre.get().strip()
            pais = entrada_pais.get().strip()
            try:
                huesped = Huesped(identificacion, nombre, pais)
                self.controlador.registrar_huesped(huesped)
            except Exception as e:
                messagebox.showerror("Error", str(e))
            else:
                messagebox.showinfo("Éxito", "Huésped registrado correctamente")
                win.destroy()

        tk.Button(win, text="Guardar", command=guardar_huesped).grid(row=3, column=0, columnspan=2, pady=10)

    def listar_huespedes(self) -> None:
        """Muestra una lista de todos los huéspedes registrados."""
        huespedes = self.controlador.listar_huespedes()
        if not huespedes:
            messagebox.showinfo("Información", "No hay huéspedes registrados")
            return
        win = tk.Toplevel(self.root)
        win.title("Lista de huéspedes")
        win.geometry("400x300")
        tk.Label(win, text="Huéspedes", font=("Arial", 12, "bold")).pack(pady=5)
        texto = tk.Text(win, height=10, width=50)
        texto.pack(padx=10, pady=10)
        for h in huespedes:
            texto.insert(tk.END, f"ID: {h.identificacion} | Nombre: {h.nombre} | País: {h.pais}\n")
        texto.config(state=tk.DISABLED)

    def formulario_buscar_huesped(self) -> None:
        """Formulario para buscar un huésped por identificación."""
        win = tk.Toplevel(self.root)
        win.title("Buscar huésped")
        win.geometry("300x200")
        tk.Label(win, text="Identificación:").pack(pady=5)
        entrada_identificacion = tk.Entry(win)
        entrada_identificacion.pack(pady=5)

        def buscar() -> None:
            ident = entrada_identificacion.get().strip()
            huesped = self.controlador.buscar_huesped(ident)
            if huesped:
                messagebox.showinfo("Huésped encontrado", f"ID: {huesped.identificacion}\nNombre: {huesped.nombre}\nPaís: {huesped.pais}")
            else:
                messagebox.showwarning("No encontrado", "No se encontró un huésped con esa identificación")

        tk.Button(win, text="Buscar", command=buscar).pack(pady=10)

    def formulario_eliminar_huesped(self) -> None:
        """Formulario para eliminar un huésped por identificación."""
        win = tk.Toplevel(self.root)
        win.title("Eliminar huésped")
        win.geometry("300x200")
        tk.Label(win, text="Identificación:").pack(pady=5)
        entrada_identificacion = tk.Entry(win)
        entrada_identificacion.pack(pady=5)

        def eliminar() -> None:
            ident = entrada_identificacion.get().strip()
            try:
                self.controlador.eliminar_huesped(ident)
            except Exception as e:
                messagebox.showerror("Error", str(e))
            else:
                messagebox.showinfo("Éxito", "Huésped eliminado correctamente")
                win.destroy()

        tk.Button(win, text="Eliminar", command=eliminar).pack(pady=10)

    def formulario_listar_huespedes_por_pais(self) -> None:
        """Formulario para listar huéspedes por país."""
        win = tk.Toplevel(self.root)
        win.title("Listar huéspedes por país")
        win.geometry("300x200")
        tk.Label(win, text="País:").pack(pady=5)
        entrada_pais = tk.Entry(win)
        entrada_pais.pack(pady=5)

        def listar_pais() -> None:
            pais = entrada_pais.get().strip()
            resultado = self.controlador.listar_huespedes_por_pais(pais)
            if not resultado:
                messagebox.showinfo("Sin resultados", "No hay huéspedes de ese país")
                return
            lista_win = tk.Toplevel(self.root)
            lista_win.title(f"Huéspedes de {pais}")
            lista_win.geometry("350x250")
            tk.Label(lista_win, text=f"Huéspedes de {pais}", font=("Arial", 12, "bold")).pack(pady=5)
            texto = tk.Text(lista_win, height=10, width=40)
            texto.pack(padx=10, pady=10)
            for h in resultado:
                texto.insert(tk.END, f"ID: {h.identificacion} | Nombre: {h.nombre}\n")
            texto.config(state=tk.DISABLED)
            win.destroy()

        tk.Button(win, text="Listar", command=listar_pais).pack(pady=10)

    # ---------- MÓDULO HABITACIONES ----------
    def mostrar_modulo_habitaciones(self) -> None:
        """Ventana para gestionar habitaciones."""
        ventana = tk.Toplevel(self.root)
        ventana.title("Gestión de habitaciones")
        ventana.geometry("400x400")
        tk.Label(ventana, text="Gestión de habitaciones", font=("Arial", 12, "bold")).pack(pady=10)
        tk.Button(ventana, text="Registrar habitación", command=self.formulario_registro_habitacion).pack(pady=5, fill=tk.X, padx=20)
        tk.Button(ventana, text="Listar habitaciones", command=self.listar_habitaciones).pack(pady=5, fill=tk.X, padx=20)
        tk.Button(ventana, text="Buscar habitación", command=self.formulario_buscar_habitacion).pack(pady=5, fill=tk.X, padx=20)
        tk.Button(ventana, text="Eliminar habitación", command=self.formulario_eliminar_habitacion).pack(pady=5, fill=tk.X, padx=20)
        tk.Button(ventana, text="Listar por tipo", command=self.formulario_listar_habitaciones_por_tipo).pack(pady=5, fill=tk.X, padx=20)

    def formulario_registro_habitacion(self) -> None:
        """Formulario para registrar una nueva habitación."""
        win = tk.Toplevel(self.root)
        win.title("Registrar habitación")
        win.geometry("350x300")
        tk.Label(win, text="Número:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        entrada_numero = tk.Entry(win)
        entrada_numero.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(win, text="Tipo:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        entrada_tipo = tk.Entry(win)
        entrada_tipo.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(win, text="Piso:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        entrada_piso = tk.Entry(win)
        entrada_piso.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(win, text="Precio por noche:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        entrada_precio = tk.Entry(win)
        entrada_precio.grid(row=3, column=1, padx=5, pady=5)

        def guardar_habitacion() -> None:
            numero = entrada_numero.get().strip()
            tipo = entrada_tipo.get().strip()
            piso_str = entrada_piso.get().strip()
            precio_str = entrada_precio.get().strip()
            try:
                piso = int(piso_str)
                precio = float(precio_str)
                habitacion = Habitacion(numero, tipo, piso, precio)
                self.controlador.registrar_habitacion(habitacion)
            except Exception as e:
                messagebox.showerror("Error", str(e))
            else:
                messagebox.showinfo("Éxito", "Habitación registrada correctamente")
                win.destroy()

        tk.Button(win, text="Guardar", command=guardar_habitacion).grid(row=4, column=0, columnspan=2, pady=10)

    def listar_habitaciones(self) -> None:
        """Muestra todas las habitaciones registradas."""
        habitaciones = self.controlador.listar_habitaciones()
        if not habitaciones:
            messagebox.showinfo("Información", "No hay habitaciones registradas")
            return
        win = tk.Toplevel(self.root)
        win.title("Lista de habitaciones")
        win.geometry("450x300")
        tk.Label(win, text="Habitaciones", font=("Arial", 12, "bold")).pack(pady=5)
        texto = tk.Text(win, height=12, width=60)
        texto.pack(padx=10, pady=10)
        for hb in habitaciones:
            estado = "Disponible" if hb.disponible else "Ocupada"
            texto.insert(tk.END, f"Número: {hb.numero} | Tipo: {hb.tipo} | Piso: {hb.piso} | Precio: {hb.precio} | Estado: {estado}\n")
        texto.config(state=tk.DISABLED)

    def formulario_buscar_habitacion(self) -> None:
        """Formulario para buscar una habitación por número."""
        win = tk.Toplevel(self.root)
        win.title("Buscar habitación")
        win.geometry("300x200")
        tk.Label(win, text="Número de habitación:").pack(pady=5)
        entrada_numero = tk.Entry(win)
        entrada_numero.pack(pady=5)

        def buscar() -> None:
            numero = entrada_numero.get().strip()
            habitacion = self.controlador.buscar_habitacion(numero)
            if habitacion:
                estado = "Disponible" if habitacion.disponible else "Ocupada"
                messagebox.showinfo("Habitación encontrada",
                                    f"Número: {habitacion.numero}\nTipo: {habitacion.tipo}\nPiso: {habitacion.piso}\nPrecio: {habitacion.precio}\nEstado: {estado}")
            else:
                messagebox.showwarning("No encontrada", "No se encontró una habitación con ese número")

        tk.Button(win, text="Buscar", command=buscar).pack(pady=10)

    def formulario_eliminar_habitacion(self) -> None:
        """Formulario para eliminar una habitación por número."""
        win = tk.Toplevel(self.root)
        win.title("Eliminar habitación")
        win.geometry("300x200")
        tk.Label(win, text="Número de habitación:").pack(pady=5)
        entrada_numero = tk.Entry(win)
        entrada_numero.pack(pady=5)

        def eliminar() -> None:
            numero = entrada_numero.get().strip()
            try:
                self.controlador.eliminar_habitacion(numero)
            except Exception as e:
                messagebox.showerror("Error", str(e))
            else:
                messagebox.showinfo("Éxito", "Habitación eliminada correctamente")
                win.destroy()

        tk.Button(win, text="Eliminar", command=eliminar).pack(pady=10)

    def formulario_listar_habitaciones_por_tipo(self) -> None:
        """Formulario para listar habitaciones por tipo."""
        win = tk.Toplevel(self.root)
        win.title("Listar habitaciones por tipo")
        win.geometry("300x200")
        tk.Label(win, text="Tipo de habitación:").pack(pady=5)
        entrada_tipo = tk.Entry(win)
        entrada_tipo.pack(pady=5)

        def listar_tipo() -> None:
            tipo = entrada_tipo.get().strip()
            resultado = self.controlador.listar_habitaciones_por_tipo(tipo)
            if not resultado:
                messagebox.showinfo("Sin resultados", "No hay habitaciones de ese tipo")
                return
            lista_win = tk.Toplevel(self.root)
            lista_win.title(f"Habitaciones tipo {tipo}")
            lista_win.geometry("400x250")
            tk.Label(lista_win, text=f"Habitaciones tipo {tipo}", font=("Arial", 12, "bold")).pack(pady=5)
            texto = tk.Text(lista_win, height=10, width=50)
            texto.pack(padx=10, pady=10)
            for hb in resultado:
                estado = "Disponible" if hb.disponible else "Ocupada"
                texto.insert(tk.END, f"Número: {hb.numero} | Piso: {hb.piso} | Precio: {hb.precio} | Estado: {estado}\n")
            texto.config(state=tk.DISABLED)
            win.destroy()

        tk.Button(win, text="Listar", command=listar_tipo).pack(pady=10)

    # ---------- MÓDULO RESERVAS ----------
    def mostrar_modulo_reservas(self) -> None:
        """Ventana para gestionar reservas."""
        ventana = tk.Toplevel(self.root)
        ventana.title("Gestión de reservas")
        ventana.geometry("400x450")
        tk.Label(ventana, text="Gestión de reservas", font=("Arial", 12, "bold")).pack(pady=10)
        tk.Button(ventana, text="Registrar reserva", command=self.formulario_registro_reserva).pack(pady=5, fill=tk.X, padx=20)
        tk.Button(ventana, text="Listar reservas", command=self.listar_reservas).pack(pady=5, fill=tk.X, padx=20)
        tk.Button(ventana, text="Buscar reserva", command=self.formulario_buscar_reserva).pack(pady=5, fill=tk.X, padx=20)
        tk.Button(ventana, text="Eliminar reserva", command=self.formulario_eliminar_reserva).pack(pady=5, fill=tk.X, padx=20)
        tk.Button(ventana, text="Listar por huésped", command=self.formulario_listar_reservas_por_huesped).pack(pady=5, fill=tk.X, padx=20)
        tk.Button(ventana, text="Listar por fecha", command=self.formulario_listar_reservas_por_fecha).pack(pady=5, fill=tk.X, padx=20)

    def formulario_registro_reserva(self) -> None:
        """Formulario para registrar una nueva reserva."""
        win = tk.Toplevel(self.root)
        win.title("Registrar reserva")
        win.geometry("400x400")
        # Campos de entrada
        tk.Label(win, text="Código de reserva:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        entrada_codigo = tk.Entry(win)
        entrada_codigo.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(win, text="ID huésped:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        entrada_id_huesped = tk.Entry(win)
        entrada_id_huesped.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(win, text="Número habitación:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        entrada_num_habitacion = tk.Entry(win)
        entrada_num_habitacion.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(win, text="Noches:").grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        entrada_noches = tk.Entry(win)
        entrada_noches.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(win, text="Fecha (YYYY-MM-DD):").grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
        entrada_fecha = tk.Entry(win)
        entrada_fecha.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(win, text="Responsable:").grid(row=5, column=0, sticky=tk.W, padx=5, pady=5)
        entrada_responsable = tk.Entry(win)
        entrada_responsable.grid(row=5, column=1, padx=5, pady=5)

        def guardar_reserva() -> None:
            codigo = entrada_codigo.get().strip()
            id_huesped = entrada_id_huesped.get().strip()
            num_habitacion = entrada_num_habitacion.get().strip()
            noches_str = entrada_noches.get().strip()
            fecha_str = entrada_fecha.get().strip()
            responsable = entrada_responsable.get().strip()
            try:
                noches = int(noches_str)
                # Validar fecha
                datetime.strptime(fecha_str, "%Y-%m-%d")
                huesped = self.controlador.buscar_huesped(id_huesped)
                habitacion = self.controlador.buscar_habitacion(num_habitacion)
                # Se crean instancias, pero se reusan de servicios para validar
                if huesped is None or habitacion is None:
                    raise ValueError("Huésped o habitación no existen")
                reserva = Reserva(codigo, huesped, habitacion, noches, fecha_str, responsable)
                self.controlador.registrar_reserva(reserva)
            except Exception as e:
                messagebox.showerror("Error", str(e))
            else:
                messagebox.showinfo("Éxito", "Reserva registrada correctamente")
                win.destroy()

        tk.Button(win, text="Guardar", command=guardar_reserva).grid(row=6, column=0, columnspan=2, pady=10)

    def listar_reservas(self) -> None:
        """Muestra todas las reservas registradas."""
        reservas = self.controlador.listar_reservas()
        if not reservas:
            messagebox.showinfo("Información", "No hay reservas registradas")
            return
        win = tk.Toplevel(self.root)
        win.title("Lista de reservas")
        win.geometry("500x300")
        tk.Label(win, text="Reservas", font=("Arial", 12, "bold")).pack(pady=5)
        texto = tk.Text(win, height=12, width=70)
        texto.pack(padx=10, pady=10)
        for r in reservas:
            texto.insert(tk.END, f"Código: {r.codigo} | Huésped: {r.huesped.nombre} | Habitación: {r.habitacion.numero} | Noches: {r.noches} | Fecha: {r.fecha} | Responsable: {r.responsable}\n")
        texto.config(state=tk.DISABLED)

    def formulario_buscar_reserva(self) -> None:
        """Formulario para buscar una reserva por código."""
        win = tk.Toplevel(self.root)
        win.title("Buscar reserva")
        win.geometry("300x200")
        tk.Label(win, text="Código de reserva:").pack(pady=5)
        entrada_codigo = tk.Entry(win)
        entrada_codigo.pack(pady=5)

        def buscar() -> None:
            codigo = entrada_codigo.get().strip()
            reserva = self.controlador.buscar_reserva(codigo)
            if reserva:
                messagebox.showinfo(
                    "Reserva encontrada",
                    f"Código: {reserva.codigo}\nHuésped: {reserva.huesped.nombre}\nHabitación: {reserva.habitacion.numero}\nNoches: {reserva.noches}\nFecha: {reserva.fecha}\nResponsable: {reserva.responsable}\nCosto total: {reserva.costo_total()}"
                )
            else:
                messagebox.showwarning("No encontrada", "No se encontró una reserva con ese código")

        tk.Button(win, text="Buscar", command=buscar).pack(pady=10)

    def formulario_eliminar_reserva(self) -> None:
        """Formulario para eliminar una reserva por código."""
        win = tk.Toplevel(self.root)
        win.title("Eliminar reserva")
        win.geometry("300x200")
        tk.Label(win, text="Código de reserva:").pack(pady=5)
        entrada_codigo = tk.Entry(win)
        entrada_codigo.pack(pady=5)

        def eliminar() -> None:
            codigo = entrada_codigo.get().strip()
            try:
                self.controlador.eliminar_reserva(codigo)
            except Exception as e:
                messagebox.showerror("Error", str(e))
            else:
                messagebox.showinfo("Éxito", "Reserva eliminada correctamente")
                win.destroy()

        tk.Button(win, text="Eliminar", command=eliminar).pack(pady=10)

    def formulario_listar_reservas_por_huesped(self) -> None:
        """Formulario para listar reservas por identificación de huésped."""
        win = tk.Toplevel(self.root)
        win.title("Listar reservas por huésped")
        win.geometry("300x200")
        tk.Label(win, text="Identificación de huésped:").pack(pady=5)
        entrada_identificacion = tk.Entry(win)
        entrada_identificacion.pack(pady=5)

        def listar_por_huesped() -> None:
            ident = entrada_identificacion.get().strip()
            resultado = self.controlador.listar_reservas_por_huesped(ident)
            if not resultado:
                messagebox.showinfo("Sin resultados", "No se encontraron reservas para ese huésped")
                return
            lista_win = tk.Toplevel(self.root)
            lista_win.title(f"Reservas de {ident}")
            lista_win.geometry("450x250")
            tk.Label(lista_win, text=f"Reservas de {ident}", font=("Arial", 12, "bold")).pack(pady=5)
            texto = tk.Text(lista_win, height=10, width=60)
            texto.pack(padx=10, pady=10)
            for r in resultado:
                texto.insert(tk.END, f"Código: {r.codigo} | Habitación: {r.habitacion.numero} | Noches: {r.noches} | Fecha: {r.fecha}\n")
            texto.config(state=tk.DISABLED)
            win.destroy()

        tk.Button(win, text="Listar", command=listar_por_huesped).pack(pady=10)

    def formulario_listar_reservas_por_fecha(self) -> None:
        """Formulario para listar reservas por fecha."""
        win = tk.Toplevel(self.root)
        win.title("Listar reservas por fecha")
        win.geometry("300x200")
        tk.Label(win, text="Fecha (YYYY-MM-DD):").pack(pady=5)
        entrada_fecha = tk.Entry(win)
        entrada_fecha.pack(pady=5)

        def listar_fecha() -> None:
            fecha = entrada_fecha.get().strip()
            try:
                datetime.strptime(fecha, "%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Error", "Formato de fecha incorrecto")
                return
            resultado = self.controlador.listar_reservas_por_fecha(fecha)
            if not resultado:
                messagebox.showinfo("Sin resultados", "No se encontraron reservas para esa fecha")
                return
            lista_win = tk.Toplevel(self.root)
            lista_win.title(f"Reservas de {fecha}")
            lista_win.geometry("450x250")
            tk.Label(lista_win, text=f"Reservas de {fecha}", font=("Arial", 12, "bold")).pack(pady=5)
            texto = tk.Text(lista_win, height=10, width=60)
            texto.pack(padx=10, pady=10)
            for r in resultado:
                texto.insert(tk.END, f"Código: {r.codigo} | Huésped: {r.huesped.nombre} | Habitación: {r.habitacion.numero} | Noches: {r.noches}\n")
            texto.config(state=tk.DISABLED)
            win.destroy()

        tk.Button(win, text="Listar", command=listar_fecha).pack(pady=10)

    def run(self) -> None:
        """Inicia el bucle principal de la aplicación."""
        self.root.mainloop()
