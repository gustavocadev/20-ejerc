"""
9. Pedir dos números y decir cuál es el mayor o si son iguales.
"""


# def intercambiar_variables(a, b):
#     aux = a
#     a = b
#     b = aux
#     return [a, b]


def calcular_mayor(a, b):
    may = a
    men = b
    if may < men:
        may = men
        print(f"el numero mayor es: {may}")
    if may == men:
        print("los numeros son iguales")


number1 = int(input("ingrese un numero: "))
number2 = int(input("ingrese un numero: "))

calcular_mayor(number1, number2)
# lack
