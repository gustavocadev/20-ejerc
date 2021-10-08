"""
3. Guillermo tiene N dólares. Luis tiene la mitad de lo que posee Guillermo. Juan tiene la mitad de lo que poseen Luis y Guillermo juntos. Hacer un programa que calcule e imprima la cantidad de dinero que tienen entre los tres.
"""

n = int(input("ingrese la cantidad n de dolares: "))

g = n
l = g / 2
j = (g + l) / 2

print(f'entre los tres tienen: {g + l + j}')
