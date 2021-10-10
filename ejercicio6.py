"""
6.Hacer un programa que calcule el cuadrado de una suma.
X = a^2+ b^2 + 2ab
"""


def calcular_cuadrado(a, b):
    x = (a ** 2) + (b ** 2) + (2*a*b)
    print(f'el cuadrado de la suma es: {x}')


num1 = int(input("ingrese un numero para a: "))
num2 = int(input("ingrese un numero para b: "))

calcular_cuadrado(num1, num2)
