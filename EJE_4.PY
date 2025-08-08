def raiz_cuadrada(n):
    x = n /2.0

    while(True):
        aproximacion = (x + n /x ) /2.0

        if abs(x - aproximacion)<0.00001:
            return aproximacion
        x = aproximacion

peso=float(input("Digite su peso "))
altura = float(input("Digite su altura en metros "))

raiz_cuadrada=raiz_cuadrada(altura)

IMC= peso /raiz_cuadrada

print(f"Su indice de masa corporal es de : {IMC :.2f}")

