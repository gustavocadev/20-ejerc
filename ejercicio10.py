"""
10.Crea un programa que pedirá el ingreso de tres notas de un estudiante, luego calculará el promedio e imprimirá alguno de los siguientes mensajes:
> 10 Aprobado 
> 7 y <= 10 Recuperación 
<= 7 Desaprobado
"""


def inputInt(text):
    data = int(input(text))
    return data


def printDataStudent(average):
    if average > 10:
        print(f"tu promedio es: {average}, has aprobado :)")
    if average > 7 and average <= 10:
        print(
            f"tu promedio es: {average}, necesitas dar un examen de recuperacion =)")
    if average <= 7:
        print(f"tu promedio es: {average},Lo sentimos, has desaprobado :(")


def calculate_average(grade1, grade2, grade3):
    average = (grade1 + grade2 + grade3) / 3
    return round(average, 1)


grade1 = inputInt("ingrese su primera nota: ")
grade2 = inputInt("ingrese su segunda nota: ")
grade3 = inputInt("ingrese su tercer nota: ")

print("-----------")

average = calculate_average(grade1, grade2, grade3)
printDataStudent(average)