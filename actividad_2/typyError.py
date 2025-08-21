def resta(a , b):
    try:

        resultado=a - b

        print(f"el resultado de la operacion es {resultado}")

    except TypeError:
        print("lo sentimos pero no podemos ahcer operaiones con texto y numero combinados")

a =int(input("ingrese el valor de a "))
b =input("ingrese el valor de b ")

resta = resta(a , b)

