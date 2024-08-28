#CALCULADORA DE DESCUENTO: Crea un programa que calcule el precio final de un artículo después de aplicar un descuento al 20%.

precio_original = float(input("Ingrese el precio original del artículo: "))

descuento = precio_original * 0.20

precio_final = precio_original - descuento

print(f"El precio final del artículo después del descuento del 20% es: {precio_final}")