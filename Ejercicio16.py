#CONTADOR DE NÚMEROS PARES E IMPARES: Crea un programa que cuente y muestre la cantidad de números pares e impares en una lista ingresada por el usuario.

numeros = input("Ingrese una lista de números separados por espacios: ").split()

pares = 0
impares = 0

for numero in numeros:
  numero = int(numero)
  if numero % 2 == 0:
    pares += 1
  else:
      impares += 1

print(f"La lista contiene {pares} número(s) par(es) y {impares} número(s) impar(es).")