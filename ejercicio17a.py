def procesamiento_de_telegramas(texto, longitud, costopcorta, costoplarga):
    """
        Se le ingresa a un texto con la longitud maxima
        y el costo de palabras cortos y largas, y la funcion
        transforma las palabras que exedan la longitud las acorta
        y les agrega un "@"
    """
    lista = texto.split(' ')
    costopcortacant = 0
    costoplargacant = 0
    for i in range(0, len(lista)):
        if len(lista[i]) > (longitud + 1):
            cadenanueva = lista[i]
            cadenanueva = cadenanueva[0:(longitud)] + "@"
            lista[i] = cadenanueva
            costopcortacant += 1
        else:
            costoplargacant += 1
    texto = ' '
    for i in range (0, len(lista)-1):
        texto += lista[i] + ' '
    texto += lista[len(lista)-1]
    total = [texto, (costopcorta * costopcortacant)
             + (costoplarga * costoplargacant)]
    return total            
            
