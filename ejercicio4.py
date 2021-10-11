"""
4. Una compañía de venta de carros usados, paga a su personal de ventas un salario de $1000 mensuales, más una comisión de $150 por cada carro vendido, más el 5 % del valor de la venta por carro. Cada mes el capturista de la empresa ingresa en la computadora los datos pertinentes. Hacer un programa que calcule e imprima el salario mensual de un vendedor dado.
"""


def calcular_salario_mensual(carros, precioCarros):

    comision = 150
    valorVentaCarro = 0.5

    ganancia_comision = comision * carros
    ganancia_valor_vemta = valorVentaCarro * precioCarros

    return [ganancia_comision, ganancia_valor_vemta]


salarioMensual = 1000
carros = int(input("ingrese la cantidad de carros vendidos: "))
precio_carros = int(input("ingrese el precio de los carros: "))

ganancia1, ganancia2 = calcular_salario_mensual(carros, precio_carros)

salarioMensual += ganancia1 + ganancia2

print(f"El salario mensual que usted recibirá es: {salarioMensual} ")
