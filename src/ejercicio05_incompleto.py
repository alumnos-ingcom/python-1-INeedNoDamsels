################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
5. Divisiones

Precondiciones:
    Los valores ingresados deben ser números enteros.
Poscondiciones:
    Los resultados de la operación deben ser números enteros.
    Los resultados de la operación deben ser el correcto resto y cociente entre ambos valores.
"""

def division_lenta(dividendo, divisor):
    """
    Esta función recibe dos números y retorna la división lenta del primero entre el segundo.
    """
    i = 0
    signo = ""
    if ((dividendo > 0) and (divisor > 0)) or ((dividendo < 0) and (divisor < 0)):
        while abs(dividendo) >= abs(divisor):
            if divisor > 0:
                signo = "-"
            else:
                signo = "+"

            i += 1
            dividendo -= divisor

            print(f"{signo} {abs(divisor)} ", end = "")
    else:
        # terminar !!!
        pass

    return dividendo, i

def principal():
    """
     Este programa solicita el ingreso de dos números enteros
    y enseña la división lenta del primero entre el segundo.
    """
    print("Ingrese un valor numérico entero para A y B")
    dividendo = int(input(" >> A: "))
    divisor = int(input(" >> B: "))
    assert divisor != 0, "Cuidado campeón, no queremos destrozar el universo... o si..."

    print(f"\nDivisión lenta: {dividendo} ", end = "")
    resto, cociente = division_lenta(dividendo, divisor)
    print(f"\n  Resto: {resto}\n  Cociente: {cociente}")

if __name__ == "__main__":
    principal()
