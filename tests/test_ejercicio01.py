"""
Test correspondientes a 'ejercicio01.py'.
"""

################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#!/usr/bin/python
import sys
import pytest

from src.ejercicio01 import convertir_a_fahrenheit, convertir_a_centigrados

# testing: convertir_a_fahrenheit
def test_convertir_a_fahrenheit_positivo():
    """
    Este test evalúa la conversión de grados °C positivos a °F.
    """
    numero = 10
    resultado = convertir_a_fahrenheit(numero)
    assert resultado == 50, "El resultado no es el esperado."

def test_convertir_a_fahrenheit_negativo():
    """
    Este test evalúa la conversión de grados °C negativos a °F.
    """
    numero = -10
    resultado = convertir_a_fahrenheit(numero)
    assert resultado == 14, "El resultado no es el esperado."

def test_convertir_a_fahrenheit_cero():
    """
    Este test evalúa la conversión de cero grados °C a °F.
    """
    numero = 0
    resultado = convertir_a_fahrenheit(numero)
    assert resultado == 32, "El resultado no es el esperado."

# testing: convertir_a_centigrados
def test_convertir_a_centigrados_positivo():
    """
    Este test evalúa la conversión de grados °F positivos a °C.
    """
    numero = 20
    resultado = convertir_a_centigrados(numero)
    assert resultado == -6.67, "El resultado no es el esperado."

def test_convertir_a_centigrados_negativo():
    """
    Este test evalúa la conversión de grados °F negativos a °C.
    """
    numero = -20
    resultado = convertir_a_centigrados(numero)
    assert resultado == -28.89, "El resultado no es el esperado."

def test_convertir_a_centigrados_cero():
    """
    Este test evalúa la conversión de cero grados °F a °C.
    """
    numero = 0
    resultado = convertir_a_centigrados(numero)
    assert resultado == -17.78, "El resultado no es el esperado."
