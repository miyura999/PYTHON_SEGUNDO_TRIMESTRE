prestamo = float(input("ingrese la cantida la cual debes "))
tasa_interes = float(input("ingrese la tasa de interes mesual"))
numero_meses = int(input("ingrese el numero de meses que durara el prestamo"))

interes = tasa_interes / 100
pago_mensual=prestamo * (interes * (1 + interes) ** numero_meses) / ((1 + interes) ** numero_meses - 1)

print(f"El pago mensual es: {pago_mensual:.2f}")
print(f"El total a pagar al final del prestamo es: {pago_mensual * numero_meses:.2f}")
print(f"El total de interes pagado al final del prestamo es: {(pago_mensual * numero_meses) - prestamo:.2f}")