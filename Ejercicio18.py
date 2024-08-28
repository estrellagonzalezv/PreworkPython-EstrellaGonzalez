#CONTADOR DE PALABRAS: Crea un programa que cuente la cantidad de palabras en una oración ingresada por el usuario.

oracion = input("Ingrese una oración: ")

palabras = oracion.split()

cantidad_palabras = len(palabras)

print(f"La oración ingresada contiene {cantidad_palabras} palabra(s).")