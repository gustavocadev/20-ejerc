"""
5.La calificación final de un estudiante de Informática se calcula con base a las calificaciones de tres aspectos de su rendimiento académico: participación, tareas y examen parcial. Sabiendo que las calificaciones anteriores entran a la calificación con ponderaciones del 10 %, 40% y 50 %. Hacer un programa que calcule e imprima la calificación de la Unidad obtenida por un estudiante.
"""


def calcular_nota_unidad(participacionNota, tareaNota, parcialNota):
    nota_unidad = (participacionNota * 0.10) + \
        (tareaNota * 0.40) + (parcialNota * 0.50)
    print(f"Su nota final de la unidad es: {nota_unidad}")


participacionNota = int(input("ingrese la nota de participación: "))
tareaNota = int(input("ingrese la nota de las tareas: "))
parcialNota = int(input("ingrese la nota de su examen parcial: "))

calcular_nota_unidad(participacionNota, tareaNota, parcialNota)
