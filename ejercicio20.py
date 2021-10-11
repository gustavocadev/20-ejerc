"""
20. Realiza un programa que diga si un número entero positivo introducido por teclado es capicúa. Se permiten números de hasta 5 cifras.
"""
numero_usuario = int(input("ingrese un número (maximo de 5 cifras): "))


def calcular_indices(num):
    listaCifras = []
    i2 = 100_000
    for _ in range(1, 6+1):
        indices = (num // i2) % 10
        listaCifras.append(indices)
        i2 //= 10
    listaFiltrada = []
    for lista in listaCifras:
        if lista != 0:
            listaFiltrada.append(lista)
    return listaFiltrada


def cifras_invertidas(lista):
    lista.reverse()
    return lista


lista = calcular_indices(numero_usuario)
lista_invertida = cifras_invertidas(calcular_indices(numero_usuario))


if lista == lista_invertida:
    print("SÍ es capicúa")
else:
    print("NO es capicúa")
