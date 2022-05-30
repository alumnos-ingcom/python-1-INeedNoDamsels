"""
Test correspondientes a 'ejercicio02.py'
"""

################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#!/usr/bin/python
import sys
import pytest

from src.ejercicio02 import signo

# testing: signo
def test_signo_positivo():
    """
    Este test evalúa el signo de un número entero positivo.
    """
    numero = 10
    resultado = signo(numero)
    assert resultado == "positivo", "El resultado no es el esperado."

def test_signo_negativo():
    """
    Este test evalúa el signo de un número entero negativo.
    """
    numero = -10
    resultado = signo(numero)
    assert resultado == "negativo", "El resultado no es el esperado."

def test_signo_cero():
    """
    Este test evalúa el signo del número cero.
    """
    numero = 0
    resultado = signo(numero)
    assert resultado == "cero", "El resultado no es el esperado."
