import queue
import threading
from queue import Queue, Empty


class CarreraController:

    def __init__(self, carrera, vista):
        self.carrera = carrera
        self.vista = vista

        #Lock para proteger la sección crítica
        self.lock = threading.Lock()

        #Cola para enviar los eventos desde los
        #Hilos hacia la interfaz
        self.eventos = Queue()

        #Lista de hilos creados
        self.hilos = []

        #Bandera de control
        self.detener = False

        self.configurar_vista()

    def configurar_vista(self):
        """Conecta botones y dibuja la escena inicial"""
        self.vista.btn_iniciar.config(commnad = self.iniciar_Carrera)
        self.vista.btn_reiniciar.config(commnad=self.reiniciar_Carrera)
        self.vista.dibujar_escena(self.carrera)

        #After() permite revisar periódicamente

        #La cola desde el hilo principal de Tkinter
        self.vista.root.after(50, self.procesar_eventos)

    def procesar_eventos(self):
        """
        Atiende los eventos enviados por los hilos
        Esta función se ejecuta repetidamente en el hilo principal de Tkinter, lo cual evita actualizar la
        interfaz directamente desde hilos secundarios
        """

        try:
            while True:
                """remueve y retorna un item de la cola sin bloquear el programa"""
                evento = self.eventos.get_nowait()
                tipo = evento["tipo"]

                if tipo == "avance":
                    self.vista.actualizar_corredor(evento["nombre"], evento["posicion"])
                elif tipo == "estado":
                    self.vista.mostrar_estado(evento["mensaje"])
                elif tipo == "ganador":
                    self.vista.marcar_ganador(evento["nombre"])
                    self.vista.mostrar_estado(f"Gano {evento['nombre']} la carrera")
                    self.vista.activar_inicio()
        except Empty:
            pass
            # Se vuelve a ejecutar la revision de la cola
        self.vista.root.after(50, self.procesar_eventos())

        def mover_corredor(self, corredor):
            """"Funcion que ejecuta cada hilo ,cada corredor avanza en intervalos aleatorios y con pasos aleatorios"""

            while True:
                time.sleep(Random.uniform(0.08, 0.25))

                with self.lock:
                    if self.detener or self.carrera.ganador is not None:
                        break

                    avance = random.randint(3, 15)
                    corredor.posicion += avance

                    # No permitimos que sobrepase demaciado la meta
                    if corredor.posicion > self.carrera.meta:
                        corredor.posicion = self.carrera.meta

                    self.eventos.put(
                        {"tipo": "avance",
                         "nombre": corredor.nombre}
                    )




