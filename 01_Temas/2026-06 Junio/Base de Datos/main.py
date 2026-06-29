from Temas.BaseDeDatos.Controller.EstudianteController import EstudianteController


def main():
    controller = EstudianteController()
    controller.mostrar_menu()

#Recordatorio: La siguiente instrucción permite que
#el programa solo inicie cuando se ejecuta este archivo
#Si el archivo fuera importado desde otro módulo,
#main() no se ejecutará automáticamente.

if __name__ == "__main__":
    main()

