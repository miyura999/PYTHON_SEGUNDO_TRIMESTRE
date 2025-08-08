# Implementa un algoritmo que convierta una temperatura de grados Celsius a
# Fahrenheit.

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Introduce la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius} grados Celsius son {fahrenheit:.2f} grados Fahrenheit.")