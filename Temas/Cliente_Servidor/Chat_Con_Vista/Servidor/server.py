import socket
import threading
import json
import struct
from Temas.Cliente_Servidor.Chat_Con_Vista.Servidor.gestos_usuarios import GestorUsuarios

#---------------------------------------------------------------------------------------------
class ServidorChat:
    def __init__(self, direccion_ip = "10.35.118.213", puerto= "80"):
        self.direccion_ip = direccion_ip
        self.puerto = puerto
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.clientes = [ ] #sockets
        self.sockets_a_sesiones = {}
        self.lock = threading.Lock()
        self.gestor = GestorUsuarios ()

    #--------------------------Serilización---------------------------------------------------
    def enviar_objeto(self, el_socket, objeto):
        data = json.dumps(objeto).encode()
        el_socket.send(struct.pack("!I", len(data)))
        el_socket.sendall(data)

    def recibir_objeto(self, el_socket):
        datos = el_socket.recv(4)
        if not datos:
            return None

        size = struct.unpack("!I", datos)[0]
        data = b""

        while len(data) < size:
            fragmento = el_socket.recv(4096)

            if not fragmento:
                return None
            data += fragmento

            return json.loads(data.decode())
        return None

    #---------------------------------------------------------------------------------------------
    def broadcast(self, objeto):
        for c in list(self.clientes):
            try:
                self.enviar_objeto(c, objeto)
            except:
                #self._desconectar(c)

    def enviar_lista(self):
        self.broadcast({
            "Tipo": "Usuarios",
            "Lista":self.gestor.listar()
        })

    # --------------------------Clientes-----------------------------------------------------------
    #manejar_clientes
    def desconectar(self, el_socket):
        session_id = self.sockets_a_sesiones.pop(el_socket)
        nombre = None

        if session_id:
            nombre = self.gestor.eliminar_sesion(session_id)
        with self.lock:
            if el_socket in self.clientes:
                self.clientes.remove(el_socket)
        try:
            el_socket.close()
        except:
            pass
        if nombre:
            self.broadcast({
                "Tipo": "Sistema",
                "Texto": f"{nombre} salio"
            })




