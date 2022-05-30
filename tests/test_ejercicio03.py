"""
Test correspondientes a 'ejercicio03.py'
"""

################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#!/usr/bin/python
import sys
import pytest

from src.ejercicio03 import compara

# testing: compara
def test_compara_positivo():
    """
    Este test evalúa la relación de tamaños de dos números cuando
     el primero menos el segundo da un resultado positivo.
    """
    numero = 10
    resultado = compara(numero)
    assert resultado == 1, "El resultado no es el esperado."

def test_compara_negativo():
    """
    Este test evalúa la relación de tamaños de dos números cuando
     el primero menos el segundo da un resultado negativo.
    """
    numero = -10
    resultado = compara(numero)
    assert resultado == -1, "El resultado no es el esperado."

def test_compara_cero():
    """
    Este test evalúa la relación de tamaños de dos números cuando
     el primero menos el segundo da cero.
    """
    numero = 0
    resultado = compara(numero)
    assert resultado == 0, "El resultado no es el esperado."