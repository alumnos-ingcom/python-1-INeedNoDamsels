################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
10. Palíndromo

Precondiciones:
    La palabra o frase ingresada no puede estar vacía.
Poscondiciones:
    El resultado obtenido debe ser un valor de verdad.
    El resultado obtenido debe indicar correctamente si el texto ingresado es un palíndromo o no.
"""

def es_palindromo(texto):
    """
    Esta función recibe texto y retorna un valor de verdad indicando si es un palíndromo.
    """
    texto = texto.replace(" ", "")
    texto = texto.lower()

    i = 0
    cantidad_iguales = 0
    valor_verdad = None
    while i != len(texto):
        if texto[i] == texto[(-i) - 1]:
            cantidad_iguales += 1
        i += 1

    valor_verdad = bool(cantidad_iguales = len(texto))

    return valor_verdad

def principal():
    """
     Este programa solicita el ingreso de una palabra o frase
    y enseña un valor de verdad indicando si se trata de un palíndromo.
    """
    palabra = input("Ingrese una palabra o frase: ")
    assert len(palabra) > 0, "Error, no se ha ingresado nada."
    valor_verdad = es_palindromo(palabra)

    print(f"    ¿Se trata de un palíndromo...? ¡{valor_verdad}!\n")

if __name__ == "__main__":
    principal()
