# Desarrolla un algoritmo que calcule la propina y el total a pagar en un restaurante, dado
# el monto de la cuenta y el porcentaje de propina.

monto_Cuenta=int(input("Por favor digite el valor de su cuenta a pagar\n"))
porcentaje_Propina=int(input("por favor digite el % de la propina"))

total_Pagar=monto_Cuenta+(porcentaje_Propina/100)*monto_Cuenta

print(f"el valor total a pagar es de ${total_Pagar}")