################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
2. Números positivos y negativos

Precondiciones:
    El valor ingresado debe ser un número entero.
Poscondiciones:
    El resultado obtenido debe indicar correctamente el signo del número igresado.
"""

def signo(numero):
    """
    Esta función recibe un número y, mediante cálculos innecesarios, retorna su signo.
    """
    i = 0
    signo_numero = ""
    repeticiones = abs(numero)
    while i != repeticiones:
        numero -= 1
        i += 1

    if i != 0:
        if numero == (-2 * i):
            signo_numero = "negativo"
        else:
            signo_numero = "positivo"
    else:
        signo_numero = "cero"

    return signo_numero

def principal():
    """
    Este programa solicita el ingreso de un número y enseña su signo.
    """
    numero = int(input("Ingrese un número entero: "))
    resultado = signo(numero)

    print(f"El número ingresado es {resultado}.")

if __name__ == "__main__":
    principal()
