from David.Semana2.Sistema_Flete.View.View import Vista
from Controller.controlador import Controlador

print("Hola")
def main():
    controlador = Controlador()
    vista = Vista()

    while True:
        opcion = vista.menu()

        if opcion == 1:
            datos = vista.pedir_cliente()
            controlador.agregar_clientes(*datos)
        elif opcion == 2:
            print("\n Clientes disponibles")
            vista.mostrar_clientes(controlador.consultar_clientes())

        elif opcion == 3:
            print("\n Clientes disponibles")
            vista.mostrar_clientes(controlador.consultar_clientes())
            datos = vista.pedir_flete()
            controlador.agregar_flete(*datos)

        elif opcion == 4:
            vista.mostrar_fletes(controlador.consultar_fletes())

        elif opcion == 5:
            print("--Fin del programa--")
            break

if __name__ == "__main__":
    print("Hola")
    main()


