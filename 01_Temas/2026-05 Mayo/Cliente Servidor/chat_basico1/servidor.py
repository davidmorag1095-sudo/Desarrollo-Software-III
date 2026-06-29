import socket
#Configuracion
direccion_ip = "10.35.118.238"
puerto = 5002

#Crear socket               IPV4        Significa que estará en TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Asociar a IP y puerto
server.bind((direccion_ip, puerto))

server.listen(1)


print("Servidor esperando conexión")
socket_cliente, direccion_cliente = server.accept()

#El método aceptar devuelve un par de valores, primero un socket
#Con la conexión al cliente y seguidamente la dirección del cliente.

print("Conectado por: ", direccion_cliente)

#Recibir datos
data = socket_cliente.recv(1024)


print("El cliente dice: ", data.decode())

#Enviar respuesta
socket_cliente.send("Hola cliente".encode())


#Cerramos socket del cliente recién creado
socket_cliente.close()
server.close()


