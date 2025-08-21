
lista = []

def agregar():
    cantidad = int(input("¿Cuántas frutas desea ingresar? \n"))
    for i in range(cantidad):
        fruta =input("ingrese una fruta \n")
        lista.append(fruta)

def mostrar():
    try:
        posicion=int(input(f"que fruta deseas ver es de 0 a {len(lista) - 1}\n"))
        print(f"la fruta la cual usted quiere ves es \n {lista[posicion]}")
    except IndexError:
        print(f"debe ingresar una posicion entre 0 a {len(lista) - 1}")

agregar()

mostrar()