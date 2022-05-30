"""
Test correspondientes a 'ejercicio06.py'
"""

################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#!/usr/bin/python
import sys
import pytest

from src.ejercicio06 import ordenar_mayor_a_menor, ordenar_menor_a_mayor

# testing: ordenar_mayor_a_menor
def test_ordenar_mayor_a_menor_positivos():
    """
    Este test evalúa el correcto ordenamiento decreciente de tres valores positivos distintos.
    """
    numero_uno = 2
    numero_dos = 3
    numero_tre = 1
    resultado = ordenar_mayor_a_menor(numero_uno, numero_dos, numero_tre)
    assert resultado == (3, 2, 1), "El resultado no es el esperado."

def test_ordenar_mayor_a_menor_negativos():
    """
    Este test evalúa el correcto ordenamiento decreciente de tres valores negativos distintos.
    """
    numero_uno = -2
    numero_dos = -3
    numero_tre = -1
    resultado = ordenar_mayor_a_menor(numero_uno, numero_dos, numero_tre)
    assert resultado == (-1, -2, -3), "El resultado no es el esperado."

def test_ordenar_mayor_a_menor_ambos():
    """
    Este test evalúa el correcto ordenamiento decreciente de tres valores distintos.
    """
    numero_uno = -2
    numero_dos = 3
    numero_tre = -1
    resultado = ordenar_mayor_a_menor(numero_uno, numero_dos, numero_tre)
    assert resultado == (3, -1, -2), "El resultado no es el esperado."

# testing: ordenar_menor_a_mayor
def test_ordenar_menor_a_mayor_positivos():
    """
    Este test evalúa el correcto ordenamiento creciente de tres valores positivos distintos.
    """
    numero_uno = 2
    numero_dos = 3
    numero_tre = 1
    resultado = ordenar_menor_a_mayor(numero_uno, numero_dos, numero_tre)
    assert resultado == (1, 2, 3), "El resultado no es el esperado."

def test_ordenar_menor_a_mayor_negativos():
    """
    Este test evalúa el correcto ordenamiento creciente de tres valores negativos distintos.
    """
    numero_uno = -2
    numero_dos = -3
    numero_tre = -1
    resultado = ordenar_menor_a_mayor(numero_uno, numero_dos, numero_tre)
    assert resultado == (-3, -2, -1), "El resultado no es el esperado."

def test_ordenar_menor_a_mayor_ambos():
    """
    Este test evalúa el correcto ordenamiento creciente de tres valores distintos.
    """
    numero_uno = -2
    numero_dos = 3
    numero_tre = -1
    resultado = ordenar_menor_a_mayor(numero_uno, numero_dos, numero_tre)
    assert resultado == (-2, -1, 3), "El resultado no es el esperado."
