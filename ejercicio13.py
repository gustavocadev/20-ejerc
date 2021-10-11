"""
13.Hacer un programa que lea un carácter por teclado y compruebe si es una letra mayúscula.
"""


def comprobarLetra(letra):
    for i in range(27):
        if chr(i+64) == letra:
            print("la letra es MAYÚSCULA")
            return
    print("la letra es minuscula")


letra = input("ingrese una letra: ")

comprobarLetra(letra)
