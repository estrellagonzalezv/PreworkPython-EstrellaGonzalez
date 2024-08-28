#SUMA DE NÚMEROS PARES: Escribe un programa que calcule la suma de todos los números pares del 1 al 100.
suma_pares = 0

for numero in range(2,101,2):
    suma_pares += numero

print(f"La suma de los números pares del 1 al 100 es {suma_pares}")