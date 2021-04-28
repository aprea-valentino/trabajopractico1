def contar_vocales(cadena):
"""
    Se ingresa una cadena y la funcion devuelve
    la cantidad de vocales que hay.
"""
    vocales = 0
    for c in cadena:
        if c in "aeiouAEIOU":
            vocales = vocales + 1
    return vocales
