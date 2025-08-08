# Crea un algoritmo que calcule el promedio de una lista de números.

def calcular_promedio(numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

numeros = []
cantidad = int(input("¿Cuántos números desea ingresar? "))
for i in range(cantidad):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

promedio = calcular_promedio(numeros)
print(f"El promedio de los números ingresados es: {promedio:.2f}")