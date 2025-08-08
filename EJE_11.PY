#  Desarrolla un algoritmo que verifique si la temperatura de una habitación está dentro de
# un rango aceptable (por ejemplo, entre 20°C y 25°C)

temperatura = float(input("Introduce la temperatura de la habitación en °C: "))

if 20 <= temperatura <= 25:
    print("la temperatura esta dentro del rango aceptable.")
else:
    print("la temperatura esta fuera del rango aceptable.")