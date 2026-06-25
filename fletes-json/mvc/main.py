import View.view as vista

from Repository.repositorio import Repositorio
#----------------------------------------------#
from Service.service_cliente import ServiceCliente
from Service.service_fletes import FletesService
#----------------------------------------------#
from Controller.controller_cliente import ControllerCliente
from Controller.controller_fletes import ControllerFlete


def cargar_aplicacion():
    #----------------------------------------------#
    service_cliente = ServiceCliente(Repositorio)
    service_flete = FletesService(Repositorio,service_cliente)
    #----------------------------------------------#
    controller_cliente = ControllerCliente(service_cliente)
    controller_flete = ControllerFlete(service_flete)
    #----------------------------------------------#
    while(True):
        opcion = vista.mostrar_principal()
        if opcion == 1:
            menu_cliente(controller_cliente)
        elif opcion == 2:
            menu_fletes(controller_flete)
        else:
            vista.mostrar_mensaje('opcion invalida')
            
#-=-=-=-=-==-=--==-=--==--==-=--==--==--=-=-==--==--=-=-=-=-=-=-==-=--=#
def menu_cliente(controller):
    while True:
        opcion = vista.dialogo('Cliente')
        if opcion == 1:
            id = input('Id: ')
            nombre = input('Nombre: ')
            telefono = int(input('Telefono: '))
            vista.mostrar_mensaje(controller.registrar_cliente(id,nombre,telefono))

        elif opcion == 2:
            vista.mostrar_datos(controller.mostrar_clientes())

        elif opcion == 3:
            id =input('Id: ')
            vista.mostrar_datos(controller.buscar_cliente(id))

        elif opcion == 0:
            break
        else:
            vista.mostrar_mensaje('Opcion invalida')

#-=-=-=-=-==-=--==-=--==--==-=--==--==--=-=-==--==--=-=-=-=-=-=-==-=--=#
def menu_fletes(controller_f):
    while True:
        opcion = vista.dialogo('Flete')
        if opcion == 1:
            id_fl = input('Id: ')
            id_cl = input('Id cliente: ')
            ciudad = input('ciudad: ')
            destino = input('destino: ')
            peso = int(input('Peso: '))
            vista.mostrar_mensaje(controller_f.registrar_flete(id_fl,id_cl,ciudad,destino,peso))

        elif opcion == 2:
            vista.mostrar_datos(controller_f.mostrar_fletes())
        elif opcion == 3:
            id_fl = input('Id: ')
            vista.mostrar_datos(controller_f.buscar_flete(id_fl))
        elif opcion == 0:
            break
        else:
            vista.mostrar_mensaje('Opcion invalida')
#-=-=-=-=-==-=--==-=--==--==-=--==--==--=-=-==--==--=-=-=-=-=-=-==-=--=#
if __name__ == '__main__':
    cargar_aplicacion()
