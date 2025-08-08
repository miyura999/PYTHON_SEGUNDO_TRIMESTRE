# Diseña un algoritmo que calcule el precio final de un producto después de aplicar un
# descuento.

precio_producto = float(input("Introduce el precio del producto: "))
descuebto = float(input("Introduce el porcentaje del descuento: "))

precio_final = precio_producto - (precio_producto * descuebto / 100)
print(f"El precio final del producto después de aplicar el descuento es: {precio_final:.2f} ")
