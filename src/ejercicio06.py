################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
6. Ordenar 3 valores

Precondiciones:
    Los valores ingresados deben ser números enteros.
Poscondiciones:
    Los resultados obtenidos deben ser números enteros.
    Los resultados obtenidos deben ser tuplas ordenadas con los valores ingresados.
"""

def ordenar_mayor_a_menor(valor_a, valor_b, valor_c):
    """
    Esta función retorna una tupla, con los valores recibidos, ordenados de manera decreciente.
    """
    tupla_decreciente = ()
    if valor_a > valor_b:
        if valor_a > valor_c:
            if valor_b > valor_c:
                tupla_decreciente = (valor_a, valor_b, valor_c)
            else:
                tupla_decreciente (valor_a, valor_c, valor_b)
        else:
            tupla_decreciente = (valor_c, valor_a, valor_b)
    elif valor_a > valor_c:
        tupla_decreciente =(valor_b, valor_a, valor_c)
    elif valor_b > valor_c:
        tupla_decreciente = (valor_b,valor_c, valor_a)
    else:
        tupla_decreciente = (valor_c, valor_b, valor_a)

    return tupla_decreciente

def ordenar_menor_a_mayor(valor_a, valor_b, valor_c):
    """
    Esta función retorna una tupla, con los valores recibidos, ordenados de manera creciente.
    """
    tupla_creciente = ()
    if valor_a > valor_b:
        if valor_a > valor_c:
            if valor_b > valor_c:
                tupla_creciente = (valor_c, valor_b, valor_a)
            else:
                tupla_creciente (valor_b, valor_c, valor_a)
        else:
            tupla_creciente = (valor_b, valor_a, valor_c)
    elif valor_a > valor_c:
        tupla_creciente =(valor_c, valor_a, valor_b)
    elif valor_b > valor_c:
        tupla_creciente = (valor_a,valor_c, valor_b)
    else:
        tupla_creciente = (valor_a, valor_b, valor_c)

    return tupla_creciente

def principal():
    """
    Este programa solicita el ingreso de tres números y los enseña ordenados en tuplas.
    """
    print("Ingrese un valor numérico entero para A, B y C")
    valor_a = int(input(" >> A: "))
    valor_b = int(input(" >> B: "))
    valor_c = int(input(" >> C: "))

    tupla_a = ordenar_mayor_a_menor(valor_a, valor_b, valor_c)
    print(f"\nTupla ordenada de MAYOR a MENOR: {tupla_a}")

    tupla_b = ordenar_menor_a_mayor(valor_a, valor_b, valor_c)
    print(f"\t  ...y de MENOR a MAYOR: {tupla_b}")

if __name__ == "__main__":
    principal()
