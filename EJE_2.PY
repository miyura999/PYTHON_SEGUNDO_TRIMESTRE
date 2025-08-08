# Crea un algoritmo que convierta de dólares a euros.

euro=0.86
dolar=1.16


while True:
    opcion=int(input("desea hacer una coversion \n1. euro/dolar \n2. dolar/euro \n"))
    if (opcion != 1 and opcion != 2):
        print("operacion invalida")
        break
    cantidad=int(input("digite la catidad a covertir \n"))
    
    if(opcion==1):
        cantidadDolares = cantidad * (1 / euro)
        print(f"usted convirtio ${cantidad} euros a ${cantidadDolares:.2f} dolares")
    
    if (opcion==2):
        cantidadEuros= cantidad  * (1 / dolar)
        print(f"usted convirtio ${cantidad} dolares a ${cantidadEuros:.2f} euros")

print("usted a salido del programa")


