# Desarrolla un algoritmo que reste los gastos de un presupuesto mensual y muestre el
# saldo restante.
presupuesto = float(input("Introduce el presupuesto mensual: "))
while True:
    opcion = input("¿Desea calcular el saldo restante de un presupuesto mensual? (s/n): ")

    if opcion != "s":
        print("Fin del programa.")
        break

    gastos = float(input("introduce el valor del : "))

    if gastos > presupuesto:
        print("Los gastos superan el presupuesto mensual.")
    else:
        presupuesto = presupuesto - gastos
        print(f"El saldo restante del presupuesto mensual es: {presupuesto:.2f}")
        


