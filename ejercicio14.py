"""
14.En Plaza Vea se hace un 20% de descuento a los clientes cuya compra supere los S /300.00 ¿Cuál será la cantidad que pagará una persona por su compra?
"""


def aplicarDescuento(precioProducto):
    descuento = precioProducto * 0.20
    return precioProducto - descuento


valorSoles = int(input("ingrese el valor de su compra: "))

precioResultante = aplicarDescuento(valorSoles)

print(f'el nuevo precio aplicado con descuento es: {precioResultante}')
