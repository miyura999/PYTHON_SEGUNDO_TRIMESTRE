# Escribe un algoritmo que verifique si un elemento específico existe en una lista

def verificar_elemento(lista, elemento):
    if elemento in lista:
        return True
    else:
        return False
    
lista = [1, 2, 3, 4, 5]
elemento = int(input("Introduce el elemento a verificar: "))
if verificar_elemento(lista, elemento):
    print(f"El elemento {elemento} existe en la lista.")
else:
    print(f"El elemento {elemento} no existe en la lista.")