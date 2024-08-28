#SUMA DE NÚMEROS EN UNA LISTA: Crea un programa que sume todos los números en una lista ingresada por el usuario.

numeros = input("Ingrese una lista de números separados por espacios: ").split()

numeros = [int(numero) for numero in numeros]

suma_total = sum(numeros)

print(f"La suma de los números en la lista es: {suma_total}.")