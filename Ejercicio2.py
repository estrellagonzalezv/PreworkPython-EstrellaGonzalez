#CALCULADORA DE PROPINA: Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo una propina del 15% sobre el total de la cuenta. 
def calculo_total_con_propina(monto):
    propina = monto * 0.15
    total = monto + propina
    return total

#solicitar monto de la cuenta

monto = float(input("Ingrese el monto de la cuenta:   "))

total_a_pagar = calculo_total_con_propina(monto)
print(f"El monto total a pagar, incluyendo una propina del 15%, es {total_a_pagar} euros")
