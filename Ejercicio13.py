#VERIFICACIÓN DE NÚMERO PRIMO: Escribe un programa que determine si un número ingresado por el isiario es primo o no.
numero = int(input("Ingrese un número entero positivo mayor que 1: "))

if numero > 1:
  for i in range(2, numero):
    if (numero % i) == 0:
      print(f"{numero} no es número primo.")
      break
  else:
    print(f"{numero} es un número primo")
else:
  print("Por favor, ingrese un número entero positivo mayor que 1.")