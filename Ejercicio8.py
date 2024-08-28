#CÁLCULO DE ÍNDICE DE MASA CORPORAL: Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
peso = float(input("Ingrese su peso en kilogramos: "))
altura= float(input("Ingrese su altura en metros: "))

imc = peso / (altura ** 2)

print(f"Su Índice de Masa Corporal es: {imc:2f}")
