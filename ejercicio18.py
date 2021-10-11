"""
18. Hacer un programa que pase de Kg a otra unidad de medida de masa, mostrar en pantalla un menú con las opciones posibles.
"""


def convertir(kg, unidad):
    tonelada = 1000
    gramos = 1000
    libras = 2.205
    unidadConvetida = 0
    if unidad == 1:
        unidadConvetida = kg * gramos
    if unidad == 2:
        unidadConvetida = kg * libras
    if unidad == 3:
        unidadConvetida = kg / tonelada
    return unidadConvetida


kg = int(input("ingrese una cantidad kg: "))

unidad = int(input(
    "¿A qué unidad lo desea convertir?\n1) Gramos\n2) Libras\n3) Tonelada\nElige => "))

unidad_convertida = convertir(kg, unidad)

print(f'el resultado es: {unidad_convertida}')
