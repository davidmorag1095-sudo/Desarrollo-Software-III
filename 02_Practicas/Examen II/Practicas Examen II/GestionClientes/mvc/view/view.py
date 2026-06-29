
#-------------------------------------
def mostrar_principal():
    return int(input('''
            1. Cliente
            2. Flete
            3. Reportes
            0. Salir
            input: '''))
#-------------------------------------
def dialogo(tipo):
    return int(input(f'''
            1. Registrar {tipo}
            2. Mostrar {tipo}
            3. Buscar {tipo}
            0. Salir
            input: '''))
#-------------------------------------
def mostrar_mensaje(mensaje):
    print(mensaje)
#-------------------------------------
def mostrar_datos(dato):
    for items in dato:
        print(items.mostrar_dato())

