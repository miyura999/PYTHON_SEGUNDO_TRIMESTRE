# Desarrolla un algoritmo que permita agregar, eliminar y mostrar una lista de compras. 

productos = []

def agregar_producto(lista, articulo):
    lista.append(articulo)
    print(f"{articulo} ha sido agregado")

def eliminar_producto(lista, articulo):
    if articulo in lista:
        lista.remove(articulo)
        print(f"{articulo} Ha si eliminado ")
    else:
        print("El producto no existe")

def mostrar_productos(lista):
    print("Producto almacenados ")

    if not lista:
        print("No hay productos alacenados")
    
    else:
        for i, articulo in enumerate(lista , 1):
            print(f"{i}.{articulo}")


while(True):
    print("Menu de opciones\n1. Agregar producto\n2. Eliminar producto\n3. Mostra productos\n4. Salir ")

    opcion = int (input("Seleccione una opcion ente 1-4 : "))

    if opcion !=1 and  opcion !=2 and  opcion !=3 and  opcion !=4 :

        print("opcion invalida ingrese una opcion entre 1-4 ")

    elif opcion == 1 :
        articulo=input("Ingrese el nombre del producto a agregar")
        agregar_producto(productos, articulo)

    elif opcion == 2 :
        articulo=input("Ingrese el nombre del producto a eliminar")
        eliminar_producto(productos, articulo)

    elif opcion == 3 :
        mostrar_productos(productos)
    
    else:
        print("Has salido del sistema fue un gusto")

