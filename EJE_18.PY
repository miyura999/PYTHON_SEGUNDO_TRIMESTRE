# Diseña un algoritmo que imprima la tabla de multiplicar de un número hasta 10

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("ingrese el numero del cual desea la tabla de multiplicar: "))
tabla_multiplicar(numero)

print(f"La tabla de multiplicar del {numero} ha sido impresa.")