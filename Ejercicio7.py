#CALCULADORA SIMPLE: Crea un programa que realice operaciones aritméticas simples (suma,resta,multiplicación,división) según la elección del usuario.

print("Operaciones disponibles:")
print("1.Suma")
print("2.Resta")
print("3.Multiplicación")
print("4.División")
opcion = int(input("Ingrese el número de la operación deseada: "))

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if opcion == 1:
  resultado = num1 + num2
  operación = "suma"
elif opcion == 2:
  resultado = num1 - num2
  operación = "resta"
elif opcion == 3:
  resultado = num1 * num2
  operación = "multiplicación"
elif opcion == 4:
    if num2 == 0:
      print("Error no se puede dividir entre cero.")
      resultado = None
    else:
      resultado = num1 / num2
      operación = "división"
else:
  print("Error opción no válida.")
  resultado = None

if resultado is not None:
  print(f"El resultado de la {operación} es: {resultado}")

