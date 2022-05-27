################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
8. Números primos

Precondiciones:
    El valor ingresado debe ser un número entero positivo.
Poscondiciones:
    El resultado obtenido debe ser un valor de verdad (bool).
    El resultado obtenido debe indicar correctamente si el valor ingresado es un número primo o no.
"""

def es_primo(numero):
    """
    Esta función recibe un número y retorna un valor de verdad.
    """
    i = 1
    divisores = 0
    valor_verdad = None
    while i <= numero:
        if (numero % i) == 0:
            divisores += 1
        i += 1

    valor_verdad = bool(divisores == 2)

    return valor_verdad

def principal():
    """
     Este programa solicita el ingreso de un número entero positivo
    y enseña un valor de verdad indicando si es primo o no.
    """
    numero = int(input("Ingrese un número natural mayor que 1 (uno): "))
    assert numero > 1, "Ups! El valor ingresado no cumple con las precondiciones."

    booleano = es_primo(numero)
    print(f"    ¿{numero} será primo...? ¡{booleano}!")

if __name__ == "__main__":
    principal()
