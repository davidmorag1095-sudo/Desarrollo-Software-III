import socket
import json
import struct
import threading
from json.decoder import WHITESPACE

from servidor.gestorUsuarios import GestorUsuarios


class ServidorChat:
    def __init__(self,direccion_ip,puerto):
        self.direccion_ip=direccion_ip
        self.puerto=puerto
        self.socket_servidor=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.clientes=[]#sockets
        self.sockets_a_sesiones={}#socet->session_id
        self.lock=threading.Lock
        self.gestor=GestorUsuarios()

    #----------Serilización-----------

    def enviar_objeto(self,el_socket,objeto):
        data=json.dumps(objeto).encode()
        el_socket.send(struct.pack("!T",len(data)))
        el_socket.sendall(data)

    def recibir_objeto(self,el_socket):
        datos=el_socket.recv(4)
        if not datos:
            return None

        size=struct.unpack("!I",datos)[0]
        data=b""

        while len(data)<size:
            fragmento=el_socket.rev(4096)
            if not fragmento:
                data+=fragmento
        return  json.loads(data.decode())
    #---------comunicación-----------

    def broadcast(self,objeto):
        for c in  self.clientes:
            try:
                self.enviar_objeto(c,objeto)
            except:
                self.desconectar(c)

    def enviar_lista(self):
        self.broadcast({
            "tipo":"usuarios","lista":self.gestor.listar()
        })

    #------------clientes---------
    def manejar_clientes(self,el_socket,direccion_ip):
        print("Conectando: ",direccion_ip)

        try:
            objeto=self.recibir_objeto(el_socket)
            if not objeto or objeto.get("tipo")!="login":
                return
            nombre =objeto["usuario"]

            if self.gestor.existe(nombre):
                self.enviar_objeto(el_socket,{
                    "tipo":"error",
                    "texto":"Nombre en uso"
                })
                return
            session_id=self.gestor.crear_session(nombre)
            self.sockets_a_sesiones[el_socket]=session_id
            self.broadcast({
                "tipo":"sistema",
                "texto":f"{nombre} se unio"
            })
            #LOOP
            while True:
                objeto=self.recibir_objeto(el_socket)
                if objeto is None:
                    break

                if objeto.get("tipo")=="mensaje":
                    nombre=self.gestor.obtener_nombre(session_id)
                    self.broadcast({
                        "tipo":"mensaje",
                        "usuario":nombre,
                        "texto":objeto.get("texto","")
                    })
        finally:
            self._desconectar(self,el_socket)
            print ("Desconectado",direccion_ip)

    def _desconectar(self,el_socket):
        session_id=self.sockets_a_sesiones.pop(el_socket)
        nombre=None
        if session_id:
            nombre=self.gestor.eliminar_sesion(session_id)

        with self.lock:
            if el_socket in self.clientes:
                self.clientes.remove(el_socket)
        try:
            el_socket.close()
        except:
            pass
        if nombre:
            self.broadcast({
                "tipo":"sistema","texto":f"{nombre}salio"
            })
        self.enviar_lista()

    def iniciar(self):
        self.socket_servidor.bind(self.direccion_ip,self.puerto)
        self.socket_servidor.listen()
        print(f"Servidor en {self.direccion_ip,self.puerto}")

        while True:
            socket_cliente,direccion_cliente=self.socket_servidor.accept()
            with self.lock:
                self.clientes.append(socket_cliente)

            threading.Thread(
                target=self.manejar_clientes,
                args=(socket_cliente,direccion_cliente),
                daemon=True
            ).start()
