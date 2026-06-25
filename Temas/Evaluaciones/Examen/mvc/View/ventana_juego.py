import tkinter as tk
from tkinter import ttk


class GameWindow:
    def __init__(self, parent):

        self.window = tk.Toplevel(parent)
        self.window.title("Gestión de Videojuegos")
        self.window.geometry("1120x620")
        self.window.resizable(False, False)

        self._build_ui()

    def _build_ui(self):
        frame = ttk.Frame(self.window, padding=15)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Gestión de Videojuegos", font=("Arial", 14, "bold")).grid(
            row=0, column=0, columnspan=4, sticky="w", pady=(0, 15)
        )

        # -------- ENTRIES --------
        self.entry_codigo = ttk.Entry(frame, width=30)
        self.entry_titulo = ttk.Entry(frame, width=30)
        self.entry_desarrollador = ttk.Entry(frame, width=30)
        self.entry_categoria = ttk.Entry(frame, width=30)
        self.entry_stock = ttk.Entry(frame, width=30)

        ttk.Label(frame, text="Código:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entry_codigo.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(frame, text="Título:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.entry_titulo.grid(row=2, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(frame, text="Desarrollador:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.entry_desarrollador.grid(row=3, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(frame, text="Categoría:").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.entry_categoria.grid(row=4, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(frame, text="Licencias disponibles:").grid(row=5, column=0, sticky="w", padx=5, pady=5)
        self.entry_stock.grid(row=5, column=1, sticky="w", padx=5, pady=5)

        # -------- BOTONES --------
        ttk.Button(frame, text="Registrar", width=18).grid(row=6, column=0, padx=5, pady=10)
        ttk.Button(frame, text="Buscar por código", width=18).grid(row=6, column=1, padx=5, pady=10)
        ttk.Button(frame, text="Buscar por categoría", width=18).grid(row=6, column=2, padx=5, pady=10)
        ttk.Button(frame, text="Consultar todos", width=18).grid(row=6, column=3, padx=5, pady=10)

        # -------- TABLA --------
        columns = ("codigo", "titulo", "desarrollador", "categoria", "stock")
        self.tree = ttk.Treeview(frame, columns=columns, show="headings", height=10)
        self.tree.grid(row=8, column=0, columnspan=4, sticky="nsew", padx=5, pady=15)

        self.tree.heading("codigo", text="Código")
        self.tree.heading("titulo", text="Título")
        self.tree.heading("desarrollador", text="Desarrollador")
        self.tree.heading("categoria", text="Categoría")
        self.tree.heading("stock", text="Licencias")

        sample = [
            ("VJ-001", "Fortnite", "Epic Games", "supervivencia", "5"),
            ("VJ-014", "Grand Theft Auto V", "Rockstar Games", "acción-aventura", "2"),
        ]
        for row in sample:
            self.tree.insert("", "end", values=row)

        # -------- BOTÓN VOLVER --------
        ttk.Button(frame, text="Volver al menú principal", command=self.window.destroy).grid(
            row=9, column=0, columnspan=4, pady=10
        )