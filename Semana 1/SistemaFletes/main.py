from mvc.Controller.controlador import Controlador
from mvc.View.view import Vista

def main():
    controlador = Controlador()
    vista = Vista()

    while True:
        opcion = vista.menu()
        if opcion == 1:
            datos = vista.pedir_cliente()
            controlador.agregar_cliente(*datos)


        elif opcion == 2:
            datos = vista.pedir_flete()
            controlador.agregar_flete(*datos)


        elif opcion == 3:
            vista.mostrar_lista(controlador.consultar_clientes())
            indice = int(input('indice a modificar: '))
            datos = vista.pedir_cliente()
            controlador.modificar_cliente(indice,*datos)

        elif opcion == 4:
            'Modificar flete'
        elif opcion == 5:
            'consultar cliente'
        elif opcion == 6:
            'consultar flete'
        elif opcion == 7:
            print('Fin del programa')
            break

if __name__ == '__main__':
    main()