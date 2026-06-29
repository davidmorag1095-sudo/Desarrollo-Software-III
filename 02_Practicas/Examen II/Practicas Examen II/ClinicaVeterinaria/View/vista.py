def menu_duenos():
    return int(input('''
            1. Registrar dueño
            2. Listar Dueños
            3. Buscar Dueño por id
            4. Actualiza datos
            5. Eliminar
            0. Salir
            Input: '''))

def menu_mascostas():
    return int(input('''
            1. Registrar mascosta
            2. Listar Mascotas
            3. Buscar mascota por codigo
            4. Actualizar datos
            5. Eliminar mascota
            Input: '''))

def menu_principal():
    return int(input('''
    1.Mascotas
    2.Dueños
    Input: '''))

def mostrar_mensajes(mensaje):
    print(mensaje)

def mostrar_datos(dato):
    print(f'{dato}')