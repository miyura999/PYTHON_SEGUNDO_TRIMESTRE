# Diseña un algoritmo que calcule el tiempo que se tarda en viajar una distancia, dada la
# velocidad promedio. 

def calcular_tiempo(distancia, velocidad):
    if velocidad <= 0:
        return "La velocidad debe ser mayor que cero."
    return distancia / velocidad

distancia = float(input("Introduce la distancia a recorrer en kilómetros: "))
velocidad = float(input("Introduce la velocidad promedio en km/h: "))
tiempo = calcular_tiempo(distancia, velocidad)

print(f"el tiempo estimado para viajar {distancia} km a una velocidad de {velocidad} km/h es : {tiempo:.2f} horas")