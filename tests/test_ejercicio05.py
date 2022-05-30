"""
Test correspondientes a 'ejercicio05.py'.
"""

################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#!/usr/bin/python
import sys
import pytest

from src.ejercicio05 import division_lenta

# testing: division_lenta
def test_division_lenta_ambos_positivos_exacta():
    """
    Este test evalúa la división lenta de dos números enteros positivos.
    """
    numero_uno = 10
    numero_dos = 2
    resultado = division_lenta(numero_uno, numero_dos)
    assert resultado == (0, 5), "El resultado no es el esperado."

def test_division_lenta_ambos_positivos_no_exacta():
    """
    """
    numero_uno = 10
    numero_dos = 3
    resultado = division_lenta(numero_uno, numero_dos)
    assert resultado == (1, 3), "El resultado no es el esperado."

def test_division_lenta_ambos_negativos_exacta():
    """
    Esta función evalúa la división lenta de dos números enteros negativos.
    """
    numero_uno = -15
    numero_dos = -3
    resultado = division_lenta(numero_uno, numero_dos)
    assert resultado == (0, 5), "El resultado no es el esperado."

def test_division_lenta_ambos_negativos_no_exacta():
    """
    """
    numero_uno = -15
    numero_dos = -4
    resultado = division_lenta(numero_uno, numero_dos)
    assert resultado == (-3, 3), "El resultado no es el esperado."
