#CONTADOR DE VOCALES: Crea un programa que cuente el número de vocales en una palabra ingresada por el usuario.
#solicitar una palabra a el usuario

palabra = input("Ingrese una palabra: ")

vocales = "aeiouAEIOU"
contador = 0

for letra in palabra:
  if letra in vocales:
    contador += 1

print(f"El número de vocales en la palabra es: {contador}")