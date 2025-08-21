
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
def buscar():     
    try:
        opcion = input(f"{lista} que posicion escoges entre 0 y {len(lista) - 1}")
        print(f"lista[opcion]")

    except KeyError:
        print("error")

agregar()

mostrar()  

buscar()