"""Ejemplo#3: Sincronización usando lock
Este archivo muestra porque se necesita sincronización cuando varios hilos comparten el mismo recurso
En este ejemplo, varios hilos actualizan una variable compartida. Se usa un lock para evitar que dos kilos
modifiquen la variable exactamente al mismo tiempo"""

import threading
import time

#Recurso compartido
contador = 0

#Lock para controlar el acceso al recurso compartido
candado = threading.Lock()

def incrementar(nombre):
    """Función que incrementa la variable global contador
    El Lock garantiza que solo un hilo a la vez pueda entrar a la seccion critica"""
    global contador
    for _ in range(5):
        with candado:
            valor_actual = contador
            print(f"{nombre} lee contador = {valor_actual}")
            #Se simula un pequeño retraso para hacer más evidente el problema de concurrencia
            time.sleep(0.5)
            contador = valor_actual + 1
            print(f"{nombre} actualiza contador a {contador}")
        print("Inicio del programa")

hilo1 = threading.Thread(target=incrementar, args=("Hilo 1",))
hilo2 = threading.Thread(target=incrementar, args=("Hilo 2",))

hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()

print(f"Valor del contador:{contador}")
print(f"Fin del programa")