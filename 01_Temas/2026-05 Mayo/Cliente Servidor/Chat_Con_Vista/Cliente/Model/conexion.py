import socket
import struct
import json
import threading


class ClienteConexion:
    """
    Clase encargada de la comunicación con el servidor maneja socket,envio y recepcion de datos
    """

    def __init__(self,direccion_ip,puerto):
        self.socket_cliente=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket_cliente.connect((direccion_ip,puerto))

        self.callback=None
        self.conectando=True

    def enviar(self,objeto):
        """Envia un objeto al servidor :param objeto a enviar"""
        try:
            datos=json.dumps(objeto).encode()
            self.socket_cliente.send(struct.pack("!I",len(datos)))
            self.socket_cliente.sendall(datos)
        except:
            self.conectando=False

    def recibir_loop(self):
        """
        ciclo continuo de recepcion de datos
        se ejecutan en un hilo
        :return:
        """

        while self.conectando:
            try:
                datos=self.socket_cliente.recv(4)
                if not datos:
                    break

                size=struct.unpack("!I",datos)[0]
                data=b""
                while len(data)<size:
                    fragmento=self.socket_cliente.recv(4096)
                    if not fragmento:
                        return
                    data+=fragmento

                objeto=json.loads(data.decode())

                if self.callback:
                    self.callback(objeto)
            except:
                break

        self.conectando=False

    def iniciar(self,callback):
        """
        inicia el hilo de recepcion de datos
        :param callback:
        :return: funcion para procesar mensajes
        """
        self.callback=callback
        threading.Thread(
            target=self.recibir_loop,
            daemon=True
        ).start()


