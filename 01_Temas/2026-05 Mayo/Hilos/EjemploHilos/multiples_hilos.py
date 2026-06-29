"""
Ejemplo #2 múltiple hilos

Este archivo muestra cómo varios hilos pueden
ejecutarse de manera concurrente.
Cada hilo símula un trabajador realizando su tarea
"""


import threading
import time

def trabajador(nombre):
    """
    Función que ejecutará el hilo
    El nombre es usado para identificar cuál hilo está trabajando
    :param nombre: nombre el trabajador
    """
    for i in range(1, 4):
        print(f"{nombre} ejecutando paso {i}")
        time.sleep(1)

    print(f"{nombre} terminó")

print("Iniciando múltiples hilos ...")

#Se crean tres hilos
hilo1= threading.Thread(target=trabajador, args=("Hilo 1",))
hilo2= threading.Thread(target=trabajador, args=("Hilo 2",))
hilo3= threading.Thread(target=trabajador, args=("Hilo 3",))

#Se inician los hilos
hilo1.start()
hilo2.start()
hilo3.start()

#El programa principal espera a que todos terminen
hilo1.join()
hilo2.join()
hilo3.join()

print("Todos los hilos finalizados")
