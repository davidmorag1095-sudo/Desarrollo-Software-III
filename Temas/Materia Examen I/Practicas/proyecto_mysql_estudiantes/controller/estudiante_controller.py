"""
Archivo: estudiante_controller.py

Responsabilidad:
El controller coordina la interacción entre el usuario y el service.

En este ejemplo el controller trabaja con un menú por consola.
Más adelante, esta misma lógica podría conectarse con una interfaz gráfica.
"""

from service.estudiante_service import EstudianteService


class EstudianteController:
    """
    Controlador del módulo de estudiantes.
    """

    def __init__(self):
        """
        Constructor del controlador.

        Se crea una instancia del servicio para usar la lógica de negocio.
        """

        self.service = EstudianteService()

    def mostrar_menu(self):
        """
        Muestra el menú principal del sistema.
        """

        opcion = ""

        # El menú se repite hasta que el usuario elija salir.
        while opcion != "6":
            print("\n====================================")
            print(" SISTEMA DE GESTIÓN DE ESTUDIANTES")
            print("====================================")
            print("1. Registrar estudiante")
            print("2. Consultar estudiantes")
            print("3. Buscar estudiante por ID")
            print("4. Actualizar estudiante")
            print("5. Eliminar estudiante")
            print("6. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar()

            elif opcion == "2":
                self.consultar()

            elif opcion == "3":
                self.buscar()

            elif opcion == "4":
                self.actualizar()

            elif opcion == "5":
                self.eliminar()

            elif opcion == "6":
                print("Saliendo del sistema...")

            else:
                print("Opción inválida. Intente de nuevo.")

    def registrar(self):
        """
        Solicita los datos de un estudiante y los envía al servicio.
        """

        print("\n--- Registrar estudiante ---")

        nombre = input("Nombre completo: ")
        correo = input("Correo electrónico: ")
        carrera = input("Carrera: ")

        mensaje = self.service.registrar_estudiante(nombre, correo, carrera)

        print(mensaje)

    def consultar(self):
        """
        Consulta e imprime todos los estudiantes registrados.
        """

        print("\n--- Lista de estudiantes ---")

        estudiantes = self.service.consultar_estudiantes()

        if len(estudiantes) == 0:
            print("No hay estudiantes registrados.")
            return

        for estudiante in estudiantes:
            print(estudiante)

    def buscar(self):
        """
        Busca un estudiante por ID.
        """

        print("\n--- Buscar estudiante ---")

        try:
            id_estudiante = int(input("Digite el ID del estudiante: "))
        except ValueError:
            print("Error: el ID debe ser un número entero.")
            return

        estudiante = self.service.buscar_estudiante(id_estudiante)

        if estudiante is None:
            print("No se encontró un estudiante con ese ID.")
        else:
            print(estudiante)

    def actualizar(self):
        """
        Solicita el ID y los nuevos datos del estudiante.
        """

        print("\n--- Actualizar estudiante ---")

        try:
            id_estudiante = int(input("Digite el ID del estudiante: "))
        except ValueError:
            print("Error: el ID debe ser un número entero.")
            return

        # Se busca primero para mostrar los datos actuales.
        estudiante = self.service.buscar_estudiante(id_estudiante)

        if estudiante is None:
            print("No existe un estudiante con ese ID.")
            return

        print("\nDatos actuales:")
        print(estudiante)

        print("\nDigite los nuevos datos:")
        nombre = input("Nuevo nombre: ")
        correo = input("Nuevo correo: ")
        carrera = input("Nueva carrera: ")

        mensaje = self.service.actualizar_estudiante(
            id_estudiante,
            nombre,
            correo,
            carrera
        )

        print(mensaje)

    def eliminar(self):
        """
        Elimina un estudiante después de solicitar su ID.
        """

        print("\n--- Eliminar estudiante ---")

        try:
            id_estudiante = int(input("Digite el ID del estudiante: "))
        except ValueError:
            print("Error: el ID debe ser un número entero.")
            return

        estudiante = self.service.buscar_estudiante(id_estudiante)

        if estudiante is None:
            print("No existe un estudiante con ese ID.")
            return

        print("\nEstudiante encontrado:")
        print(estudiante)

        confirmacion = input("¿Está seguro de eliminarlo? (s/n): ")

        if confirmacion.lower() == "s":
            mensaje = self.service.eliminar_estudiante(id_estudiante)
            print(mensaje)
        else:
            print("Operación cancelada.")
