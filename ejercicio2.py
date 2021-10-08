"""
2. Hacer un programa que calcule e imprima el salario semanal de un empleado a partir de sus horas semanales trabajadas y de su salario por hora.
"""


def imprimir_salario_semanal(res):
    return print(f"El salario semanal es: {res}")


horas_semanales = int(input("ingrese las horas semales trabajadas: "))
salario_hora = int(input("ingrese su salario por hora: "))

res = horas_semanales * salario_hora

imprimir_salario_semanal(res)
