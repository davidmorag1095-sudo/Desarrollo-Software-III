from Controller.Controller import Controller
from View.View import View


def main():
    controller = Controller()
    vista = View()

    while True:
        opcion =  vista.menu()
        if opcion == 1:
            datos = vista.pedir_Cliente()
            controller.agregar_cliente(*datos)
        #-------------------------------------------
        elif opcion == 2:
            datos = vista.pedir_Flete()
            controller.agregar_flete(*datos)
        #-------------------------------------------
        elif opcion == 3:
            "Modificar Cliente"
            indice= int (input("Indice a modificar: "))
            datos = vista.pedir_Cliente()
            controller.modificar_cliente(indice,*datos)
        #-------------------------------------------
        elif opcion == 4:
            "Modificar Flete"
            indice = int(input("Indice del cliente: "))
            datos = vista.pedir_Flete()
            controller.modificar_flete(indice,*datos)
        #-------------------------------------------
        elif opcion == 5:
            "Consultar Cliente"
            lista = int (input("Digite el indice del cliente el cual desea saber su informacion: "))
            View.mostrar_Lista(lista)
        #-------------------------------------------
        elif opcion == 6:
            "Consultar Flete"
        #-------------------------------------------
        elif opcion == 7:
            print ("--Fin del programa--")
            break

if __name__ == "__main__":
    main()


