"""
Test correspondientes a 'ejercicio04.py'
"""

################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#!/usr/bin/python
import sys
import pytest

from src.ejercicio04 import suma_lenta

# testing: suma_lenta
def test_suma_lenta_positivo_positivo():
    """
    Este test evalúa la suma lenta de dos números positivos.
    """
    numero_uno = 6
    numero_dos = 4
    resultado = suma_lenta(f"\nSuma lenta: {numero_uno} ", numero_uno, numero_dos)
    assert resultado == 10, "El resultado no es el esperado."

def test_suma_lenta_negativo_negativo():
    """
    Este test evalúa la suma lenta de dos números negativos.
    """
    numero_uno = -6
    numero_dos = -4
    resultado = suma_lenta(f"\nSuma lenta: {numero_uno} ", numero_uno, numero_dos)
    assert resultado == -10, "El resultado no es el esperado."

def test_suma_lenta_positivo_negativo():
    """
    Este test evalúa la suma lenta de un número positivo con otro negativo.
    """
    numero_uno = 6
    numero_dos = -4
    resultado = suma_lenta(f"\nSuma lenta: {numero_uno} ", numero_uno, numero_dos)
    assert resultado == 2, "El resultado no es el esperado."

def test_suma_lenta_negativo_positivo():
    """
    Este test evalúa la suma lenta de un número negativo con otro positivo.
    """
    numero_uno = -6
    numero_dos = 4
    resultado = suma_lenta(f"\nSuma lenta: {numero_uno} ", numero_uno, numero_dos)
    assert resultado == -2, "El resultado no es el esperado."
