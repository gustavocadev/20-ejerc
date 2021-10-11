"""
12. Escribe un programa en que dado un número del 1 a 7 escriba el correspondiente nombre del día de la semana.
"""

dias = ["lunes", "martes", "miercoles",
        "jueves", "viernes", "sabado", "domingo"]


def calcularDiaSemana(dia):
    for i in range(7):
        if dia == i:
            print(dias[i])


num = int(input("ingrese un número del 1 al 7: "))
num -= 1
calcularDiaSemana(num)
