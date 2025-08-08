# Implementa un algoritmo que calcule la edad de un perro en años humanos (1 año de
# perro = 7 años humanos).

def calcular_edad_perro(edad_perro):
    return edad_perro * 7

edad_perro = int(input("introduce la edad de su perro en años: "))
edad_humana = calcular_edad_perro(edad_perro)
print(f"La edad de su perro en años humanos es: {edad_humana} años")