"""
7. Construir un programa que, dado un número total de horas, devuelve el número de semanas, días y horas equivalentes. Por ejemplo, dado un total de 1000 horas debe mostrar 5 semanas, 6 días y 16 horas.
"""


def calcular_semanas_dias(h):
    SEMANA_HORAS = 24 * 7
    DIA_HORAS = 24

    semanas = h // SEMANA_HORAS
    semanasSobra = h % SEMANA_HORAS

    dias = semanasSobra // DIA_HORAS
    diasSobra = semanasSobra % DIA_HORAS

    horasSobra = diasSobra

    print(f'hay {semanas} semanas, {dias} dias y {horasSobra} horas')


horas = int(input("ingrese las horas: "))

calcular_semanas_dias(horas)
