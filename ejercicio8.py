def conversion_entero_romano(entero):
    """
        Se ingresa un numero entero y la funcion
        lo devuelve en numero romano
    """
    numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romanos = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L',
               'XL', 'X', 'IX', 'V', 'IV', 'I']
    numeral = ''
    posicion = 0

    while entero > 0:
        for x in range (entero // numeros[posicion]):
            numeral += romanos[posicion]
            entero -= numeros[posicion]

        posicion += 1
    return numeral


    
