"""
16. Construir un programa que simule el funcionamiento de una calculadora que puede realizar las cuatro operaciones aritméticas básicas(suma, resta, producto y división) con valores numéricos enteros. El usuario debe especificar la operación con el primer carácter del primer parámetro de la línea de comandos: S o s para la suma R o r para la resta P, p, M o m para el producto y D o d para la división.
"""


def calcular_expresion_matematica(caracter, num1, num2):
    resultado = 0
    if caracter.lower() == 's':
        resultado = num1 + num2
    if caracter.lower() == 'r':
        resultado = num1 - num2
    if caracter.lower() == 'p' or caracter.lower() == 'm':
        resultado = num1 * num2
    if caracter.lower() == 'd' and num2 != 0:
        resultado = num1 / num2
    return resultado


user_caracter = input("ingrese el caracter: ")
num1 = int(input("ingrese un número: "))
num2 = int(input("ingrese un otro número: "))

resFinal = calcular_expresion_matematica(user_caracter, num1, num2)

print(f'el resultado es: {resFinal}')
