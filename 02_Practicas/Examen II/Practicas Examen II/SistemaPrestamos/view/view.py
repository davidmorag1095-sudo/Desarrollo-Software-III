def menu_principal():
    return int (input("""
    1.Gestion estudiantes
    2.Gestion equipos
    3.Gestion categorias
    4.Gestion prestamos"""))

def menu_categoria():
    return int (input("""
    1.Registrar
    2.Consultar
    3.Buscar
    4.Actualizar
    5.Eliminar
    0.Salir
    Input:"""))

def menu_estudiantes():
    return int (input("""
    1.Registrar
    2.Consultar
    3.Buscar
    4.Actualizar
    5.Eliminar
    0.Salir
    Input:"""))

def menu_prestamo():
    return int (input("""
    1.Registrar
    2.Consultar
    3.Buscar
    4.Actualizar
    5.Eliminar
    0.Salir
    Input: """))

def menu_equipo():
    return int (input("""
    1.Registrar
    2.Consultar
    3.Buscar
    4.Actualizar
    5.Eliminar
    0.Salir
    Input:"""))

def mostrar_mensaje(mensaje):
    print(mensaje)

def mostrar_dato(dato):
    print(f'{dato}')