################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
4. Suma lenta

Precondiciones:
    Los valores ingresados deben ser números enteros.
Poscondiciones:
    El resultado de la operación debe ser un número entero.
    El resultado de la operación debe ser la correcta suma de los valores ingresados.
"""

def suma_lenta(mensaje, valor_a, valor_b):
    """
    Esta función realiza la suma lenta de los valores ingresados.
    """
    print(mensaje, end = "")
    i = 0
    while i != abs(valor_b):
        if valor_b > 0 :
            signo = "+"
            valor_a += 1
        else:
            signo = "-"
            valor_a -= 1
        print(f"{signo} 1 ", end = "")
        i += 1
    return valor_a

def principal():
    """
    Este programa solicita el ingreso de dos números enteros y enseña la suma lenta de ambos.
    """
    print("Ingrese un valor numérico entero para A y B")
    valor_a = int(input(" >> A: "))
    valor_b = int(input(" >> B: "))

    resultado = suma_lenta(f"\nSuma lenta: {valor_a} ", valor_a, valor_b)
    print(f"= {resultado}")

if __name__ == "__main__":
    principal()
