'''Archivo principal del sistema
Respondabilidad:
    -iniciar aplicacion
    -crear la vista y el controlador
    -mantener el ciclo principal del menu

Relacion SOLID
SRP: Este archivo solamente iniciay controla el ciclo general del programa
No tiene logica de negocio'''




from ArquitecturavsDiseñoSOLID.PracticaGuiada3.solid.view.vista import VistaConsola
from ArquitecturavsDiseñoSOLID.PracticaGuiada3.solid.controller.procesador_pago import ProcesadorPago

def main(opcion=None)->None:

    vista = VistaConsola()
    controlador = ProcesadorPago()
    while True:
        try:
            vista.mostrar_menu()

            if opcion =="4":
                vista.mostrar_resultado("Saliendo")
                break

            monto = vista.solicitar_monto()
            resultado = controlador.procesa_pago(opcion, monto)
            vista.mostrar_resultado(resultado)

        except ValueError as error:
            vista.mostrar_error(str(error))
        except Exception as error:
            vista.mostrar_error(f"Ocurrio un error en el programa: {error}")

if __name__ == "__main__":
    main()