# Escribe un algoritmo que tome una lista de canciones y devuelva una lista de
# reproducción en orden aleatorio.

import random
import time 

def aleatorias_canciones(canciones):
    return random.sample(canciones, len(canciones))

canciones = ["cancion #1" , "cancion #2", "cancion #3", "cancion #4", "cancion #5"]

reproduccion = aleatorias_canciones(canciones)
print("Lista de reproducción aleatoria:")
for cancion in reproduccion:
    print(cancion)
    time.sleep(3)  



