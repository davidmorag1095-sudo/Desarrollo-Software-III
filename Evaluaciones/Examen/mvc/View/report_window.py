import tkinter as tk
from tkinter import ttk

class ReportWindow:
    def __init__(self, parent):

        self.window = tk.Toplevel(parent)
        self.window.title("Reportes")
        self.window.geometry("880x500")
        self.window.resizable(False, False)

        self._build_ui()

    def _build_ui(self):
        frame = ttk.Frame(self.window, padding=15)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Reportes", font=("Arial", 14, "bold")).grid(
            row=0, column=0, columnspan=3, sticky="w", pady=(0, 15)
        )

        # -------- BOTONES --------
        ttk.Button(frame, text="Jugadores por país", width=24).grid(row=1, column=0, padx=5, pady=8)

        ttk.Button(frame, text="Videojuegos con inventario bajo", width=24).grid(row=1, column=1, padx=5, pady=8)

        ttk.Button(frame, text="Top 3 videojuegos más usados", width=24).grid(row=1, column=2, padx=5, pady=8)

        # -------- TABLA --------
        columns = ("col1", "col2", "col3")
        self.tree = ttk.Treeview(frame, columns=columns, show="headings", height=12)
        self.tree.grid(row=2, column=0, columnspan=3, sticky="nsew", padx=5, pady=15)

        self.tree.heading("col1", text="Indicador")
        self.tree.heading("col2", text="Valor")
        self.tree.heading("col3", text="Observación")

        self.tree.column("col1", width=290)
        self.tree.column("col2", width=160)
        self.tree.column("col3", width=290)

        ttk.Button(frame, text="Volver al menú principal", command=self.window.destroy).grid(
            row=3, column=0, columnspan=3, pady=10
        )
