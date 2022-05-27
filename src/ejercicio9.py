################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
9. Factores primos

Precondiciones:
    El valor ingresado debe ser un número entero positivo.
Poscondiciones:
    Los resultados obtenidos deben ser números enteros positivos.
    Los resultados obtenidos deben ser factores primos del valor ingresado.
"""

def factores_primos(numero):
    """
    Esta función recibe un número y retorna una tupla con todos sus factores primos.
    """
    i = 1
    lista = []
    while i <= numero:
        if (numero % i) == 0:
            lista.append(i)
        i += 1
    tupla = tuple(lista)

    return tupla

def principal():
    """
     Este programa solicita el ingreso de un número entero positivo
    y enseña todos sus factores primos ordenados en un tupla.
    """
    numerito = int(input("Ingrese un número natural: "))
    assert numerito >= 0, "Ojo! No estarías cumpliendo con las precondiciones establecidas..."

    tupla = factores_primos(numerito)
    print(f"\nEl número {numerito} tiene los siguientes factores primos:\n    {tupla}")

if __name__ == "__main__":
    principal()
