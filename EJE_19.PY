# . Implementa un algoritmo que encuentre los elementos comunes entre dos listas.

def encontrar_comunes(lista_1, lista_2):
    comunes = []
    for elemento in lista_1 :
        if elemento in lista_2:
            comunes.append(elemento)
    return comunes

lista_1 = [1, 2, 3, 4, 5]
lista_2 = [4, 5, 6, 7, 8]
elementos_comunes = encontrar_comunes(lista_1, lista_2)
print (f"los elementos comunes entre las dos listas son: {elementos_comunes}")