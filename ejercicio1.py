"""
1. Hacer un programa que calcule e imprima la suma de tres calificaciones.
"""


def printGrades(finalGrade):
    print(f"la suma de las tres calificaiones es: {finalGrade}")


acumulateGrade = 0
for i in range(3):
    grade = int(input("ingrese la primera calificación: "))
    acumulateGrade += grade

printGrades(acumulateGrade)
