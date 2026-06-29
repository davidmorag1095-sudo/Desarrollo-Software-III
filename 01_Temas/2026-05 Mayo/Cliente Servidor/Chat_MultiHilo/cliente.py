import socket

#Configuraciones
direccion_ip = "10.35.118.211"
puerto = 80

socket_Cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_Cliente.connect((direccion_ip, puerto))
socket_Cliente.sendall(bytes("David Mora saluda a Herlin", 'utf-8'))

while True:
    in_data = socket_Cliente.recv(1024)

    print("Desde el servidor: ", in_data.decode())
    out_data = input()
    socket_Cliente.sendall(bytes(out_data, 'utf-8'))

    if out_data == 'end':
        break

socket_Cliente.close()


