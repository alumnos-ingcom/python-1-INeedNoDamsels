################
# Manuel Bernabei - @INeedNoDamsels
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
1. Conversión de temperaturas

Precondiciones:
    Las valores ingresados deben ser números decimales.
Poscondiciones:
    Los resultados obtenidos deben ser números decimales.
    Los resultados obtenidos deben ser la correcta conversión de temperaturas.
"""

def convertir_a_fahrenheit(celsius):
    """
    Esta función obtiene un valor en grados celsius y retorna la conversión a fahrenheit.
    """
    return round((celsius * 1.8) + 32, 2)

def convertir_a_centigrados(fahrenheit):
    """
    Esta función obtiene un valor en grados fahrenheit y retorna la conversión a celsius.
    """
    return round((fahrenheit - 32) / 1.8, 2)

def principal():
    """
    Este programa solicita el ingreso de distintas temperaturas y enseña su conversión.
    """
    print("Ingrese la temperatura correspondiente (como número decimal)")

    cels_a_fahr = convertir_a_fahrenheit(float(input(" >> °C: ")))
    assert isinstance(cels_a_fahr, float), "El valor ingresado debe ser un número flotante."
    print("    °F: {}".format(cels_a_fahr))

    fahr_a_cels = convertir_a_centigrados(float(input("\n >> °F: ")))
    assert isinstance(fahr_a_cels, float), "El valor ingresado debe ser un número flotante."
    print("    °C: {}".format(fahr_a_cels))

if __name__ == "__main__":
    principal()
