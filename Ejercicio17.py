#COVERSOR DE MILLAS A KILÓMETROS: Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo que 1 milla equivale a 1.60934 kilómetros.

millas = float(input("Ingrese la distancia en millas: "))

constante_conversion = 1.60934

kilometros = millas * constante_conversion

print(f"{millas} millas equivalen a {kilometros} kilómetros.")