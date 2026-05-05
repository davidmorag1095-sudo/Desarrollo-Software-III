import socket
import threading

class AtenderCliente(threading.Thread):
    def __init__(self, direccion_Cliente, socket_Cliente):
        threading.Thread.__init__(self)
        self.direccion_Cliente = direccion_Cliente
        self.socket_cliente = socket_Cliente
        print("Nueva conexión incluida", direccion_Cliente)

    def run(self):
        print("Conexión desde: ", self.direccion_Cliente)

        while True:
            data = self.socket_cliente.recv(2040)
            mensaje = data.decode()

            if mensaje == "Bye":
                break

            print("Desde cliente: ", mensaje)
            self.socket_cliente.send(bytes(mensaje, 'utf-8'))

        print("Cliente ", self.direccion_Cliente, "Desconectado")

direccion_ip = "10.35.118.213"
puerto = 80

socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socket_servidor.bind((direccion_ip, puerto))

print("Servidor iniciado")
print("Esperando petición de cliente...")

socket_servidor.listen(1)

while True:
    socket_cliente, direccion_Cliente = socket_servidor.accept()
    nuevo_hilo = AtenderCliente(direccion_Cliente, socket_cliente)

    nuevo_hilo.start()


