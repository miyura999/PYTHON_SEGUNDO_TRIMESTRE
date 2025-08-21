def suma (a , b):
    suma = a + b
    return suma

a =int(input("ingrese el valor de a "))
b =int(input("ingrese el valor de b "))

suma = suma(a , b)
try:

    print(f"el resultado es {suma_1}")

except NameError:
    print("Error 404 , variable no definida")