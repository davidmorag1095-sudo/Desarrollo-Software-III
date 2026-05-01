import tkinter as tk
from tkinter import ttk


class PlayerWindow:
    def __init__(self, parent):

        self.window = tk.Toplevel(parent)
        self.window.title("Gestión de Jugadores")
        self.window.geometry("900x620")
        self.window.resizable(False, False)

        self._build_ui()

    def _build_ui(self):
        frame = ttk.Frame(self.window, padding=15)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Gestión de Jugadores", font=("Arial", 14, "bold")).grid(
            row=0, column=0, columnspan=4, sticky="w", pady=(0, 15)
        )

        # -------- ENTRIES --------
        self.entry_id = ttk.Entry(frame, width=30)
        self.entry_nombre = ttk.Entry(frame, width=30)
        self.entry_correo = ttk.Entry(frame, width=30)
        self.entry_pais = ttk.Entry(frame, width=30)

        ttk.Label(frame, text="Identificación:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entry_id.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(frame, text="Nombre completo:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.entry_nombre.grid(row=2, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(frame, text="Correo electrónico:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.entry_correo.grid(row=3, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(frame, text="País:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.entry_pais.grid(row=4, column=1, sticky="w", padx=5, pady=5)

        # -------- BOTONES --------
        ttk.Button(frame, text="Registrar", width=18).grid(row=5, column=0, padx=5, pady=10)
        ttk.Button(frame, text="Buscar por ID", width=18).grid(row=5, column=1, padx=5, pady=10)
        ttk.Button(frame, text="Buscar por país", width=18).grid(row=5, column=2, padx=5, pady=10)
        ttk.Button(frame, text="Consultar todos", width=18).grid(row=5, column=3, padx=5, pady=10)

        # -------- TABLA --------
        columns = ("id", "nombre", "correo", "pais")
        self.tree = ttk.Treeview(frame, columns=columns, show="headings", height=10)
        self.tree.grid(row=6, column=0, columnspan=4, sticky="nsew", padx=5, pady=15)

        self.tree.heading("id", text="Identificación")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("correo", text="Correo")
        self.tree.heading("pais", text="País")
        sample = [
            ("J-101110111", "Ana Gómez", "ana@correo.com", "Portugal"),
            ("J-202220222", "Luis Vargas", "luis@correo.com", "España"),
        ]
        for row in sample:
            self.tree.insert("", "end", values=row)

        ttk.Button(frame, text="Volver al menú principal", command=self.window.destroy).grid(
            row=7, column=0, columnspan=4, pady=10
        )

        frame.columnconfigure(3, weight=1)
