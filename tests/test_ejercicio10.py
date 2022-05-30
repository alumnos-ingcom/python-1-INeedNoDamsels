"""
Test correspondientes a 'ejercicio10.py'
"""

################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#!/usr/bin/python
import sys
import pytest

from src.ejercicio10 import es_palindromo

# testing: es_palindromo
def test_es_palindromo_texto_palindromo():
    """
    Este test evalúa si una testo (palíndromo) es palíndromo o no.
    """
    texto = "Anita lava la tina"
    resultado = es_palindromo(texto)
    assert resultado == True, "El resultado no es el esperado."

def test_es_palindromo_texto_no_palindromo():
    """
    Este test avalúa si un texto (no palíndromo) es palíndromo o no.
    """
    texto = "Hola profesor"
    resultado = es_palindromo(texto)
    assert resultado == False, "El resultado no es el esperado."
