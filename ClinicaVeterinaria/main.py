from controller.dueno_controller import Dueno_controller
from controller.mascota_controller import Mascota_controller
import View.vista as vista
controller = Dueno_controller()
mascota = Mascota_controller()
def main():
    while True:
        try:
            opcion = vista.menu_principal()

            if opcion == 1:
                menu_mascotas()

            elif opcion == 2:
                menu_duenos()

        except Exception as Error:
            vista.mostrar_mensajes(Error)

#---------------------------------------------------------------------------------------------------------
def menu_duenos():
    while True:
        try:
            opcion = vista.menu_duenos()

            if opcion == 1:
                id = int(input("Ingrese el id: "))
                nombre = input("Ingrese su nombre: ")
                telefono = input("Ingrese el telefono: ")
                email = input("Ingrese el email: ")
                controller.registrar(str(id), nombre, telefono, email)

            elif opcion == 2:
                print(controller.listar())

            elif opcion == 3:
                id = input("Ingrese el id del dueño a buscar: ")
                controller.serch_id(id)

            elif opcion == 4:
                id = int(input("Ingrese el id: "))
                nombre = input("Ingrese su nombre: ")
                telefono = input("Ingrese el telefono: ")
                email = input("Ingrese el email: ")
                controller.update(str(id), nombre, telefono, email)

            elif opcion == 5:
                id = input("Ingrese el id: ")
                controller.eliminar(id)

            elif opcion == 0:
                break

        except Exception as Error:
            vista.mostrar_mensajes(Error)

#---------------------------------------------------------------------------------------------------------
def menu_mascotas():
    while True:
        try:
            opcion = vista.menu_mascostas()

            if opcion == 1:
                codigo = input("Ingrese el codigo: ")
                nombre = input("Ingrese su nombre: ")
                especie = input("Ingrese el especie: ")
                edad = input("Ingrese el edad: ")
                id_dueno= input("Ingrese el ID del dueño: ")
                mascota.registrar_mascota(codigo, nombre, especie,  edad, id_dueno)

            elif opcion == 2:
                vista.mostrar_mensajes(mascota.get_all())

            elif opcion == 3:
                codigo = input("Ingrese el codigo de la mascota a buscar: ")
                mascota.buscar_codigo(codigo)

            elif opcion == 4:
                codigo = input("Ingrese el codigo: ")
                nombre = input("Ingrese su nombre: ")
                especie = input("Ingrese el especie: ")
                edad = input("Ingrese el edad: ")
                id_dueno = input("Ingrese el ID del dueño: ")
                mascota.update(codigo, nombre, especie, edad, id_dueno)

            elif opcion == 5:
                codigo = input("Ingrese el codigo: ")
                mascota.eliminar(codigo)

        except Exception as Error:
            vista.mostrar_mensajes(Error)
if __name__ == '__main__':
    main()
