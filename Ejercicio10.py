#DETERMINAR EL DÍA DE LA SEMANA: Escribe un programa que determine el día de la semana correspondiente a un número ingresado por el usuario (1 para lunes, 2 para martes,etc)

dias_semana = {
  1: "lunes",
  2: "martes",
  3: "miércoles",
  4: "jueves",
  5: "viernes",
  6: "sábado",
  7: "domingo"
}

numero = int(input("Ingrese un número del 1 al 7: "))

if numero in dias_semana:
  dia = dias_semana[numero]
  print(f"El número {numero} corresponde al día {dia}.")
else:
    print("Número no valido. Por favor, ingree un número del 1 al 7.")