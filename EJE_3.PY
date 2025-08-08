# Implementa un algoritmo que clasifique a una persona en "Niño"(13), 
# "Adolescente"(18), "Adulto" (+18) o "Adulto mayor"(65) según su edad. 

edad =int(input("Digite su edad "))

if edad >18 and edad <65:
    print("Usted es un adulto ")
elif edad >13 and edad <=18:
    print("Usted es un adolecente ")
elif edad >=1 and edad<=13:
    print("Usted es un niño ")
elif edad >= 65 :
    print("Usted es un adulto mayo ")
else:
    print("Dato invalido ")