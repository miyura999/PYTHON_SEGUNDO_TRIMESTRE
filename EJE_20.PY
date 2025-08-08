# Escribe un algoritmo que calcule el área de un círculo dado su radio.
import math
def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

radio = float(input("ingrese el radio del circulo: "))
area = calcular_area_circulo(radio)
print(f"El área del círculo con radio {radio} es: {area:.2f} ")