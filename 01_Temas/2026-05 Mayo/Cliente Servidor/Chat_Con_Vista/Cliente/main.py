from tkinter import Tk,simpledialog

from Temas.Cliente_Servidor.Chat_Con_Vista.Cliente.View.chatVista import  ChatVista
from Temas.Cliente_Servidor.Chat_Con_Vista.Cliente.Controller.chat_controlador import ChatControlador
from Temas.Cliente_Servidor.Chat_Con_Vista.Cliente.Model.conexion import ClienteConexion

direccion_ip = "localhost"
puerto = 80

root = Tk()
root.withdraw()

nombre = simpledialog.askstring("nombre", "Ingresa tu ip")

if not nombre:
    exit()

conexion = ClienteConexion(direccion_ip,puerto)
vista = ChatVista(nombre)

controlador = ChatControlador(vista,conexion,nombre)

vista.iniciar()

