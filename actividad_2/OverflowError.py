def calculo_potencia(numero , potencia):
    try:

        potencia = numero**potencia
        print(f"el resultado del calculo es {potencia:.2f}")

    except OverflowError:

        print("lo sentimos pero su calculo pasa el rango numerico")

numero = int(input("ingrese el valor de numero a calcular"))
potencia = int(input("ingrese el exponente para el calculo"))

calculo = calculo_potencia(numero , potencia)
