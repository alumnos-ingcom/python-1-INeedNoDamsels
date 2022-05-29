################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
11. Múltiplos de

Precondiciones:
    Los valores ingresados deben ser números enteros distintos de cero.
Poscondiciones:
    El resultado obtenido debe indicar si el primer número ingresado es múltiplo del segundo.
"""

def es_multiplo(numero, multiplo):
    """
    Esta función recibe dos números e indica si el primero es múltiplo del otro.
    """
    valor_verdad = None
    while abs(numero) >= abs(multiplo):
        if (numero < 0) or (multiplo < 0):
            numero += multiplo
        else:
            numero -= multiplo

    valor_verdad = bool(numero == 0)

    return valor_verdad

def principal():
    """
     Este programa solicita el ingreso de dos números enteros,
    y enseña un valor de verdad indicando si el primero es múltiplo del segundo.
    """
    print("Ingrese un valor numérico entero para A y B:")
    valor_a = int(input(" >> A: "))
    valor_b = int(input(" >> B: "))
    assert (valor_a != 0) and (valor_b != 0), "Demonios, has vuelto a fallar."

    valor_verdad = es_multiplo(valor_a, valor_b)
    print(f"\n¿Será {valor_a} múltiplo de {valor_b}...? ¡{valor_verdad}!")

if __name__ == "__main__":
    principal()
