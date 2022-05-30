"""
Test correspondientes a 'ejercicio07.py'
"""

################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#!/usr/bin/python
import sys
import pytest

from src.ejercicio07 import sexadecimal_a_decimal, decimal_a_sexadecimal

# testing: sexadecimal_a_decimal
def test_sexadecimal_a_decimal():
    """
    Este test evalúa la conversión de valores enteros positivos en formato H-M-S a segundos.
    """
    numero_uno = 1
    numero_dos = 1
    numero_tre = 1
    resultado = sexadecimal_a_decimal(numero_uno, numero_dos, numero_tre)
    assert resultado == 3661, "El resultado no es el esperado."

def test_sexadecimal_a_decimal_cero():
    """
    Este test evalúa la conversión de cero H-M-S a segundos.
    """
    numero_uno = 0
    numero_dos = 0
    numero_tre = 0
    resultado = sexadecimal_a_decimal(numero_uno, numero_dos, numero_tre)
    assert resultado == 0, "El resultado no es el esperado."

# testing: decimal_a_sexadecimal
def test_decimal_a_sexadecimal():
    """
    Este test avalúa la conversión de un número entero positivo a formato H-M-S.
    """
    numero = 10921
    resultado = decimal_a_sexadecimal(numero)
    assert resultado == (3, 2, 1), "El resultado no es el esperado."

def test_decimal_a_sexadecimal_cero():
    """
    Este test evalúa la conversión de cero a formato H-M-S.
    """
    numero = 0
    resultado = decimal_a_sexadecimal(numero)
    assert resultado == (0, 0, 0), "El resultado no es el esperado."