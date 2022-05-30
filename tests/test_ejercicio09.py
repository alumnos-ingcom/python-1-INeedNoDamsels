"""
Test correspondientes a 'ejercicio09.py'
"""

################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#!/usr/bin/python
import sys
import pytest

from src.ejercicio09 import factores_primos

# testing: factores_primos
def test_factores_primos_natural_primo():
    """
    Este test evalúa los factores primos de un número primo.
    """
    numero = 7
    resultado = factores_primos(numero)
    assert resultado == (1, 7), "El resultado no es el esperado."

def test_factores_primos_natural_no_primo():
    """
    Este test evalúa los factores primos de un número no primo.
    """
    numero = 8
    resultado = factores_primos(numero)
    assert resultado == (1, 2, 4, 8), "El resultado no es el esperado."
