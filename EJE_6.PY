# Diseña un algoritmo que calcule el costo total de un viaje, sumando el costo del 
# combustible, el peaje y el alojamiento. 

combustible = float(input("Ingrese el costo del combustible: "))
peaje = float(input("Ingrese el costo del peaje: "))
alojamiento = float(input("Ingrese el costo del alojamiento: "))

costo_total = combustible + peaje + alojamiento
print(f"El costo total del viaje es: ${costo_total:.2f}")