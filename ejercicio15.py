"""
15. Un obrero necesita calcular su salario semanal, el cual se obtiene de la siguiente manera: Si trabaja 40 horas o menos se le paga S /16 por hora Si trabaja mas de 40 horas se le paga S /16 por cada una de las primeras 40 horas y S /20 por cada hora extra.
"""


def calcular_salario_semanal(horasTrabajadas):
    pago_por_hora = 16
    pago_horas_extras = 20
    # # calculamos el pago total
    totalPago = pago_por_hora * horas_trabajadas
    if horasTrabajadas <= 40:
        return totalPago
    if horasTrabajadas > 40:
        # calculamos la cantidad de horas extras
        horasExtras = horasTrabajadas - 40
        # calculamos el total del pago extra recibido
        totalPagoExtra = horasExtras * pago_horas_extras

        pagoFinal = totalPago + totalPagoExtra
        return pagoFinal


horas_trabajadas = int(input("ingrese las horas trabajadas: "))

pago_final = calcular_salario_semanal(horas_trabajadas)

print(f"el pago final que usted recibirá es: {pago_final}")
