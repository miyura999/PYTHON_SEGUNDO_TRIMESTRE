# ZeertoDivisionError

try:
    #resultado = 100/0 buena
    resultado = 100/0
    print(resultado)

except ZeroDivisionError:    
    print("no se puede dividir por 0")


#indexError

try:
    lista = [1 , 3 , 5 , 7 , 9]
   #print(lista[2]) buena
    print(lista[70])

except IndexError:
    print("lista fuera de rango")


#nameError

try:
    #x = 2 buena
    print(x)

except NameError:
    print("Error la variable x no esta definida")


#typyError

try:
    #suma = 2 + "juan" buena
    suma = 2 + "juan"
    print(suma)

except TypeError:
    print("Error no se puede sumar enteros con cadena de texto")


#ModuleNotFoundError

try:
    #import random bueno
    import randomx

except ModuleNotFoundError:
    print("Error el modulo de llama random")


#OverflowError

try:
    #resultado_1 = 5.25**5 bueno
    resultado_1 = 5.25**536273

except OverflowError:
    print("Error resultado demasiado grande")


#KeyError

try:
    productos = {"manzanas" : 39,
                 "peras" : 32,
                 "lechuga" : 17
                 }
    #print(productos["peras"])
    print(productos["sandias"])

except KeyError:
    print("llave erronea , sandia no existe")
    