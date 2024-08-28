#COVERSOR DE TEMPERATURA: Escribe un programa que convierta una temperatura de grados Celsius a grados Fahrenheit.
def celsius_a_fahrenheit(celsius) :
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

#solicitar temperatura en grados celsius

celsius = float(input("Ingrese la temperatura en grados Celsius: ")) 
 
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}ºF")