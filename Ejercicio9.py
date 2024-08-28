#CONVERSOR DE DIVISAS: Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que 1 dólar es igual a 0.85 euros.
tasa_conversión = 0.85

cantidad_dolares = float(input("Ingresa la cantidad de dólares a convertir a euros: "))

cantidad_euros = cantidad_dolares * tasa_conversión

print(f"{cantidad_dolares} dólares equivalen a {cantidad_euros} euros")