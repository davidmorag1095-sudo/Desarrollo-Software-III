"""
Ejemplo #1: Hilo básico en Python
Este archivo muestra cómo crear
Objetivo:
    Cómo crear un hilo
    Cómo iniciar un hilo
    Cómo esperar a que termine
"""


import threading
import time
from xml.dom.expatbuilder import theDOMImplementation


def tarea():
    """
    El hilo va a ejecutar esta función
    Acá simulamos una tarea que tarda un poco en ejecutarse
    """

    for i in range(1,6):
        print(f"Hilo trabajando... paso {i}")
        time.sleep(1)

        print("El hilo terminó su trabajo")


print("Programa principal iniciado")

#Se crea el hilo indicando la función que va a ejecutar
hilo = threading.Thread(target=tarea)


#Star() inicia la ejecución del hilo
hilo.start()

#join() hace que el programa principal espere
#Hasta que el hilo termine
hilo.join()

print("Programa principal terminado")
