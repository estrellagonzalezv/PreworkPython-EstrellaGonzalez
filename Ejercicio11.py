#CALCULADORA DE EDAD: Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad actual.

from datetime import datetime
año_actual = datetime.now().year

año_nacimiento = int(input("Ingrese su año de nacimiento (YYYY): "))

edad = año_actual - año_nacimiento

print(f"Usted tiene {edad} años.")