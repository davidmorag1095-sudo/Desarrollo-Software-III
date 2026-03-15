from Sistema_Flete.Controller.Controller import Controller
from Sistema_Flete.View.View import View

def main():
    controller = Controller()
    vista = View()

    while True:
        opcion =  vista.menu()
        if opcion == 1:
            datos = vista.pedir_Cliente()
            controller.agregar_Cliente(*datos)


        elif opcion == 2:
            datos = View.pedir_Flete()
            controller.agregar_Flete(*datos)


        elif opcion == 4:
            "Modificar Flete"


        elif opcion == 5:
            "Consultar Cliente"

        elif opcion == 6:
            "Consultar Flete"

        elif opcion == 7:
            print ("--Fin del programa--")
            break

if __name__ == "__main__":
    main()


