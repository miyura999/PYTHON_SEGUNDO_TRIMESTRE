# Diseña un algoritmo que ordene una lista de números de menor a mayor.

def ordenar_lista(numeros):
    return sorted(numeros)  

numeros = []
cantidad = int(input("¿Cuántos números desea ingresar? "))
for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)
numeros_ordenados = ordenar_lista(numeros)
print(f"La lista de números ordenada de menor a mayor es: {numeros_ordenados}")