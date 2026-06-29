"""El controlador coordina la interaccion entre el usuario
y el servicio
En este ejemplo el controller trabaja con un menu por consola
 Mas adelante,esta misma clase podria conectarse con una interfaz grafica"""
from Temas.BaseDeDatos.Service.EstudianteService import EstudianteService


class EstudianteController:
    def __init__(self):
        self.service = EstudianteService()

    def mostrar_menu(self):
        opcion = ""
        while opcion != "6":
            print("\n===============================")
            print("SISTEMA DE GESTION DE ESTUDIANTES")
            print("===============================")
            print("1. Registrar estudiante")
            print("2. Consultar estudiante")
            print("3. Buscar estudiante por ID")
            print("4. Actualizar estudiante")
            print("5. Eliminar estudiante")
            print("6. Salir")

            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                self.registrar()
            elif opcion == "2":
                self.consultar_estudiantes()
            elif opcion == "3":
                self.buscar()
            elif opcion == "4":
                self.actualizar()
            elif opcion == "5":
                self.eliminar()
            elif opcion == "6":
                print("Saliendo del programa")
            else:
                print("Debe seleccionar una opcion valida")

    def registrar(self):
        """Solicita los datos de un estudiante y los envia al servicio"""
        nombre = input("Nombre completo")
        correo = input("Correo")
        carrera = input("carrera")

        mensaje = self.service.registrar_estudiante(nombre,correo,carrera)
        print(mensaje)

    def consultar_estudiantes(self):
        """Consulta e imprime todos los estudiantes registrados"""
        print("\n-----Lista de estudiantes------------")
        estudiantes = self.service.consultar_estudiante()
        if len(estudiantes) == 0:
            print("No hay estudiantes en la lista")
            return
        for estudiante in estudiantes:
            print(estudiante)

    def buscar(self):
        """Busca un estudiante  por ID """
        print("\n--------Buscar estudiantes-------")
        try:
            id_estudiante = int(input("Digite el ID del estudiante"))
        except ValueError:
            print("Error: el ID de ser un número entero")
            return

        estudiante = self.service.buscar_estudiante(id_estudiante)
        print(estudiante)

    def actualizar(self):
        """
        Solicita el id y los nuevos datos del estudiante y actualiza la base dae datos"""
        print("\n--------Actualizar estudiantes---------")

        try:
            id_estudiante = int(input("Digite el ID del estudiante"))
        except ValueError:
            print("Error: el ID deber ser un número entero")
            return
            # Se busca primero para mostrar los datos actuales
        estudiante = self.service.buscar_estudiante(id_estudiante)

        if estudiante is None:
            print("No hay estudiantes en la lista")
            return
        print("Datos actuales")
        print(estudiante)

        print("Digite los nuevos datos del estudiante")

        nombre = input("Nombre completo")
        correo = input("Correo")
        carrera = input("Carrera")

        mensaje = self.service.actualizar_estudiante(
            id_estudiante,
            nombre,
            correo,
            carrera)
        print(mensaje)

    def eliminar(self):
        """
        Solicite el ID de un estudiante y elimina dicho"""
        print("\n--------Eliminar estudiantes---------")
        try:
            id_estudiante = int(input("Digite el ID del estudiante"))
        except ValueError:
            print("Error: el ID debe ser un numero entero")
            return

        estudiante = self.service.buscar_estudiante(id_estudiante)
        if estudiante is None:
            print("No hay estudiantes en la lista")
            return
        print("Estudiante encontrado")
        print(estudiante)

        confirmacion = input("¿Está seguro de eliminarlo?(s/n): ")

        if confirmacion.lower() == "s":
            mensaje = self.service.eliminar_estudiante(id_estudiante)
            print(mensaje)
        else:
            print("Operacion cancelada")
