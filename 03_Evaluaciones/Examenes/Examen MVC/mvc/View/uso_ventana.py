import tkinter as tk
from tkinter import ttk


class UseWindow:
    def __init__(self, parent):

        self.window = tk.Toplevel(parent)
        self.window.title("Gestión de Usos")
        self.window.geometry("1120x520")
        self.window.resizable(False, False)

        self._build_ui()

    def _build_ui(self):
        frame = ttk.Frame(self.window, padding=15)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Gestión de Usos", font=("Arial", 14, "bold")).grid(
            row=0, column=0, columnspan=4, sticky="w", pady=(0, 15)
        )

        # -------- ENTRIES --------
        self.entry_codigo = ttk.Entry(frame, width=25)
        self.entry_jugador = ttk.Entry(frame, width=25)
        self.entry_juego = ttk.Entry(frame, width=25)
        self.entry_fecha = ttk.Entry(frame, width=20)
        self.entry_cantidad = ttk.Entry(frame, width=20)

        ttk.Label(frame, text="Código de uso:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.entry_codigo.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(frame, text="ID del jugador:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.entry_jugador.grid(row=2, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(frame, text="Código del videojuego:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.entry_juego.grid(row=3, column=1, sticky="w", padx=5, pady=5)

        ttk.Label(frame, text="Fecha:").grid(row=1, column=2, sticky="w", padx=5, pady=5)
        self.entry_fecha.grid(row=1, column=3, sticky="w", padx=5, pady=5)

        ttk.Label(frame, text="Cantidad:").grid(row=2, column=2, sticky="w", padx=5, pady=5)
        self.entry_cantidad.grid(row=2, column=3, sticky="w", padx=5, pady=5)

        # -------- BOTONES --------
        ttk.Button(frame, text="Registrar", width=18).grid(row=4, column=0, padx=5, pady=10)
        ttk.Button(frame, text="Consultar todos", width=18).grid(row=4, column=1, padx=5, pady=10)
        ttk.Button(frame, text="Buscar por jugador", width=18).grid(row=4, column=2, padx=5, pady=10)
        ttk.Button(frame, text="Buscar por fecha", width=18).grid(row=4, column=3, padx=5, pady=10)

        # -------- TABLA --------
        columns = ("código", "jugador", "juego", "fecha", "cantidad")
        self.tree = ttk.Treeview(frame, columns=columns, show="headings", height=10)
        self.tree.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=5, pady=15)

        self.tree.heading("código", text="Código")
        self.tree.heading("jugador", text="ID jugador")
        self.tree.heading("juego", text="Código juego")
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("cantidad", text="Cantidad")

        sample = [
            ("U-001", "J-101110111", "VJ-014", "2026-04-25", "1"),
            ("U-002", "J-202220222", "VJ-022", "2026-04-26", "2"),
        ]
        for row in sample:
           self.tree.insert("", "end", values=row)


        ttk.Button(frame, text="Volver al menú principal", command=self.window.destroy).grid(
            row=6, column=0, columnspan=4, pady=10
        )