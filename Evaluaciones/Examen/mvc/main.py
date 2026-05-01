import tkinter as tk
from Examen.mvc.Controller.controlador import Controlador

#Views
from Examen.mvc.View.main_window import MainWindow
from Examen.mvc.View.uso_ventana import UseWindow
from Examen.mvc.View.report_window import ReportWindow
from Examen.mvc.View.ventana_juego import GameWindow
from Examen.mvc.View.ventana_jugador import PlayerWindow

def main():
    controlador = Controlador()
    root = tk.Tk()
    app = MainWindow(root)
    PlayerWindow(root)
    UseWindow(root)
    ReportWindow(root)
    GameWindow(root)

    root.mainloop()


if __name__ == "__main__":
    main()
