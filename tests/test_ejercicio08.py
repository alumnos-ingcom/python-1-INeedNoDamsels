"""
Test correspondientes a 'ejercicio08.py'
"""

################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#!/usr/bin/python
import sys
import pytest

from src.ejercicio08 import es_primo

# testing: es_primo
def test_es_primo_entero_primo():
    """
    Este test evalúa si un número entero positivo (primo) es primo o no.
    """
    numero = 7
    resultado = es_primo(numero)
    assert resultado == True, "El resultado no es el esperado."

def test_es_primo_entero_no_primo():
    """
    Este test evalúa si un número entero positivo (no primo) es primo o no.
    """
    numero = 8
    resultado = es_primo(numero)
    assert resultado == False, "El resultado no es el esperado."