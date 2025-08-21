
lista = []

def agregar():
    cantidad = int(input("¿Cuántas frutas desea ingresar? \n"))
    for i in range(cantidad):
        fruta =input("ingrese una fruta \n")
        lista.append(fruta)

def mostrar():
    for i in range(len(lista)):
        print(lista)
        
        return lista
agregar()

mostrar()       
try:
    opcion = input(f"{lista} que posicion escoges")

except KeyError:
    print("error")
