"""
11.Realiza un programa que pida una hora por teclado y que muestre luego buenos días, buenas tardes o buenas noches según la hora. Se utilizarán los tramos de 6 a 12. de 13 a 20 y de 21 a 5. respectivamente. Sólo se tienen en cuenta las horas, los minutos no se deben introducir por teclado.
"""


def saludar(hora):
    if hora >= 6 and hora <= 12:
        print("buenos días")
    if hora >= 13 and hora <= 20:
        print("Buenas tardes")
    if hora >= 21 or hora <= 5:
        print("Buenas noches")


hora_ingresada = int(input("ingrese una hora: "))


saludar(hora_ingresada)
