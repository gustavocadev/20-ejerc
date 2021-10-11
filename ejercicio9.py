"""
9. Pedir dos números y decir cuál es el mayor o si son iguales.
"""


def calcular_mayor(a, b):
    may = a
    men = b
    if may < men:
        may = men
        print('---------------')
        print(f"el numero mayor es: {may}")
        return
    if may == men:
        print('---------------')
        print("los numeros son iguales")
        return
    print('---------------')
    print(f"El número mayor es: {may}")


number1 = int(input("ingrese un numero: "))
number2 = int(input("ingrese un numero: "))

calcular_mayor(number1, number2)
