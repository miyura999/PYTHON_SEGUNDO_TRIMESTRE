numero_1 = int(input("digita el primer numero a dividir \n"))
numero_2 = int(input("digita el segundo numero a dividir \n"))


try:
    division = numero_1 / numero_2
    print(f"el resultado de la division es {division}")
except ZeroDivisionError:
    print(f"el numero {numero_2} no puede ser 0")