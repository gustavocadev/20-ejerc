"""
17. Hacer un programa que simule un cajero automático con un saldo inicial de 1000 Dólares, con el siguiente menú de opciones: 
- Ingresar dinero a la cuenta 
- Retirar dinero de la cuenta 
- Salir
"""
saldo_inicial = 1000


def imprimir_saldo(saldo):
    print(f'su dinero actual es: {saldo} soles')


def ingresarDinero(dinero):
    global saldo_inicial
    saldo_inicial += dinero
    imprimir_saldo(saldo_inicial)


def retirar_dinero(dinero):
    global saldo_inicial
    saldo_inicial -= dinero
    imprimir_saldo(saldo_inicial)


while True:
    accion = input(
        "ingrese la accion que desea ejecutar: r [retirar], i [ingresar dinero], q [para_salirte]: ")
    if accion == 'i':
        dinero_ingresado = int(input("ingrese dinero a la cuenta: "))
        ingresarDinero(dinero_ingresado)
    if accion == 'r':
        dinero_retirado = int(input("retire dinero a la cuenta: "))
        retirar_dinero(dinero_retirado)
    if accion == 'q':
        print(f"su saldo final es de: {saldo_inicial}")
        break
