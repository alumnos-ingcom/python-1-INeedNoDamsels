################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
3. Comparación de números

Precondiciones:
    Los valores ingresados deben ser números enteros.
Poscondiciones:
    El código de retorno debe indicar correctamente la relación entre ambos valores ingresados.
"""

def operacion(valor_a, valor_b):
    """
    Esta función retorna la diferencia entre dos valores ingresados.
    """
    return valor_a - valor_b

def compara(resultado):
    """
    Esta función retorna un código indicando la relación entre los valores ingresados.
    """
    codigo = 0
    if resultado < 0:
        codigo = -1
    elif resultado == 0:
        codigo = 0
    else:
        codigo = 1
    return codigo

def principal():
    """
    Este programa solicita el ingreso de dos números y enseña un código según su relación.
    """
    print("Ingrese un valor numérico entero para A y B")
    valor_a = int(input(" >> A: "))
    valor_b = int(input(" >> B: "))

    relacion = compara(operacion(valor_a, valor_b)) # CR = Código de Retorno
    print(f"Relación: '{relacion}'")

    print("\t\t    GLOSARIO:\n['-1' si A < B] ; ['0' si A = B] ; ['1' si A > B]")

if __name__ == "__main__":
    principal()
