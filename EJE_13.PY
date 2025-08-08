# Diseña un algoritmo que simule el cambio de colores de un semáforo (rojo, amarillo,
# verde).

import time

def semaforo():
    colores = ["Rojo", "Amarillo", "Verde"]
    for color in colores:
        print(f"El semáforo está en: {color}")
        time.sleep(7)  

while True:
    semaforo()
    opcion = input("¿Deseas reiniciar el semáforo? (s/n): ")
    if opcion.lower() != 's':
        print("Fin del programa.")
        break