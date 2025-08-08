# Desarrolla un algoritmo que simule el lanzamiento de un dado y devuelva un número
# aleatorio entre 1 y 6

import random
def lanzar_dado():
    return random.randint(1, 6) 

opcion = 's'
while opcion.lower() == 's':
    resultado = lanzar_dado()
    print(f"El resultado del lanzamiento del dado es: {resultado}")
    opcion = input("¿Quieres lanzar el dado de nuevo? (s/n): ")

