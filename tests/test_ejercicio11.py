"""
Test correspondientes a 'ejercicio11.py'
"""

################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#!/usr/bin/python
import sys
import pytest

from src.ejercicio11 import es_multiplo

# testing: es_multiplo
def test_es_multiplo_ambos_positivos_multiplo():
    """
    Este test evalúa la multiplicidad de dos números enteros positivos.
    """
    numero_uno = 4
    numero_dos = 2
    resultado = es_multiplo(numero_uno, numero_dos)
    assert resultado == True, "El resultado no es el esperado."

def test_es_multiplo_ambos_positivos_no_multiplo():
    """
    Este test evalúa la multiplicidad de dos números enteros positivos (no múltiplos).
    """
    numero_uno = 5
    numero_dos = 3
    resultado = es_multiplo(numero_uno, numero_dos)
    assert resultado == False, "El resultado no es el esperado."

def test_es_multiplo_ambos_negativos_multiplo():
    """
    Este test evalúa la multiplicidad de dos números enteros negativos.
    """
    numero_uno = -4
    numero_dos = -2
    resultado = es_multiplo(numero_uno, numero_dos)
    assert resultado == True, "El resultado no es el esperado."

def test_es_multiplo_ambos_negativos_no_multiplo():
    """
    Este test evalúa la multiplicidad de dos números enteros negativos (no múltiplos).
    """
    numero_uno = -5
    numero_dos = -2
    resultado = es_multiplo(numero_uno, numero_dos)
    assert resultado == False, "El resultado no es el esperado."

def test_es_multiplo_uno_y_uno_multiplo():
    """
    Este test evalúa la multiplicidad de un número entero positivo y otro negativo.
    """
    numero_uno = -4
    numero_dos = 2
    resultado = es_multiplo(numero_uno, numero_dos)
    assert resultado == True, "El resultado no es el esperado."

def test_es_multiplo_uno_y_uno_no_multiplo():
    """
    Este test evalúa la multiplicidad de un número entero positivo y otro negativo (no múltiplos).
    """
    numero_uno = -5
    numero_dos = 3
    resultado = es_multiplo(numero_uno, numero_dos)
    assert resultado == False, "El resultado no es el esperado."

def test_es_multiplo_cero_positivo():
    """
    Este test evalúa la multiplicidad dos números iguales a cero.
    """
    numero_uno = 0
    numero_dos = 2
    resultado = es_multiplo(numero_uno, numero_dos)
    assert resultado == True, "El resultado no es el esperado."
