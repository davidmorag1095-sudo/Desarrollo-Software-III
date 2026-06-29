import tkinter as tk
from tkinter import scrolledtext

class ChatVista:
    """
    Clase encargada de la interfaz gráfica (UI).
    No contiene lógica de red.
    """

    def __init__(self, nombre):
        self.root = tk.Tk()
        self.root.title(f"Chat - {nombre}")
        self.root.geometry("600x500")

        main = tk.Frame(self.root)
        main.pack(fill=tk.BOTH, expand=True)

        # Panel de usuarios
        left = tk.Frame(main, width=150)
        left.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(left, text="Usuarios").pack(fill=tk.X)

        self.lista = tk.Listbox(left)
        self.lista.pack(fill=tk.BOTH, expand=True)

        # Panel de chat
        right = tk.Frame(main)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.area = scrolledtext.ScrolledText(right)
        self.area.pack(fill=tk.BOTH, expand=True)
        self.area.config(state="disabled")

        bottom = tk.Frame(right)
        bottom.pack(fill=tk.X)

        self.entry = tk.Entry(bottom)
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.btn = tk.Button(bottom, text="Enviar")
        self.btn.pack(side=tk.RIGHT)

        # Enter envía mensaje
        self.entry.bind("<Return>", lambda e: self.btn.invoke())

    def mostrar(self, texto):
        """
        Muestra un mensaje en el área de chat.
        """
        self.area.config(state="normal")
        self.area.insert(tk.END, texto + "\n")
        self.area.config(state="disabled")
        self.area.yview(tk.END)

    def get_texto(self):
        """
        Obtiene el texto ingresado por el usuario.
        """
        texto = self.entry.get()
        self.entry.delete(0, tk.END)
        return texto

    def on_enviar(self, callback):
        """
        Asocia la acción del botón enviar.
        """
        self.btn.config(command=callback)

    def actualizar_usuarios(self, lista):
        """
        Actualiza la lista de usuarios conectados.
        """
        self.lista.delete(0, tk.END)
        for u in lista:
            self.lista.insert(tk.END, u)

    def cerrar(self):
        """
        Cierra la aplicación.
        """
        self.root.quit()

    def iniciar(self):
        """
        Inicia el loop de la interfaz.
        """
        self.root.mainloop()