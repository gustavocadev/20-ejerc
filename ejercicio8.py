import ast

"""
8. Construir un programa que calcule y muestre por pantalla las raíces de la ecuación de segundo grado de coeficientes reales: ax^2 + bx + c = 0 
Use la formula general.
"""

a = int(input("ingrese un valor para a: "))
b = int(input("ingrese un valor para b: "))
c = int(input("ingrese un valor para c: "))


def parse_math_expression(expression):
    math_expression = ast.parse(expression, mode="eval")
    result = eval(compile(math_expression, '', mode="eval"))
    return result


def formula_cuadratica(signo):
    x = f'(-b {signo} ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)'
    return x


x1 = parse_math_expression(formula_cuadratica('+'))
x2 = parse_math_expression(formula_cuadratica('-'))

print(f"el resultado es:\nx1 = {x1}\nx2 = {x2}")
