# Desarrolla un algoritmo que determine si un número dado es primo (solo divisible por 1
# # y por sí mismo).

def numero_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero =int(input("ingrese un numero: "))

if numero_primo(numero):
    print(f"El número {numero} es primo.")
else:
    print(f"El número {numero} no es primo.")