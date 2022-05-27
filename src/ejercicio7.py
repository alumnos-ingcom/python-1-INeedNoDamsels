################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
7. Transformación de un número

Precondiciones:
    Los valores ingresados deben ser números enteros positivos o cero/s.
Poscondiciones:
    Los resultados obtenidos deben ser números enteros positivos.
    Los resultados obtenidos deben ser la correcta conversión de valores.
"""

def sexadecimal_a_decimal(horas, minutos, segundos):
    """
    Esta función transforma los valores recibidos en formato H-M-S y lo retorna en segundos.
    """
    while horas > 0:
        horas -= 1
        minutos += 60
    while minutos > 0:
        minutos -= 1
        segundos += 60

    return segundos

def decimal_a_sexadecimal(valor_s):
    """
    Esta función transforma el valor decimal recibido y retorna en formato H-M-S.
    """
    valor_h = 0
    valor_m = 0
    while valor_s >= 60:
        valor_s -= 60
        valor_m += 1
    while valor_m >= 60:
        valor_m -= 60
        valor_h += 1

    return (valor_h, valor_m, valor_s)

def principal():
    """
     Este programa solicita el ingreso de distintos valores numéricos
    y enseña su equivalencia en distintos formatos horarios.
    """
    print("Complete los campos para horas, minutos y segundos con valores enteros positivos")
    horas = int(input(" >> Hrs: "))
    minutos = int(input(" >> Min: "))
    segundos = int(input(" >> Seg: "))
    assert (horas >= 0) and (minutos >= 0) and (segundos >= 0), "No se cumplen las precondiciones."

    decimal_a = sexadecimal_a_decimal(horas, minutos, segundos)
    print(f"    {horas}° {minutos}' {segundos}\" equivale a {decimal_a}\"")

    decimal_b = int(input("\nAhora, ingrese un número entero positivo: "))
    assert decimal_b >= 0, "Oh sh*t, here we go again..."
    valor_h, valor_m, valor_s = decimal_a_sexadecimal(decimal_b)
    print(f"    {decimal_b}\" equivalen a {valor_h}° {valor_m}' {valor_s}\"")

if __name__ == "__main__":
    principal()
