def cadena_con_consonantes(cadena):
    """
        Se ingresa una cadena y la funcion devuelve
        solo las consonantes
    """
    for letra in cadena:
        if letra in 'aeiouAEIOU':
            cadena = cadena.replace(letra,"")
    return cadena


def cadena_sin_consonantes(cadena):
    """
        Se ingresa una cadena y te la devuelve sin consonantes
    """
    for letra in cadena:
        if letra not in "aeiouAEIOU":
            cadena=cadena.replace(letra,"")       
    return cadena


def cadena_siguiente_vocal(cadena):
    """
        Se ingresa una cadena y te la devuelve
        cambiando las vocales a su siguente vocal
    """
    vocales = ("a", "e", "i", "o", "u")
    cadenaparaconvertir = []
    cadena = cadena.lower()
    for letra in cadena:
        if letra in vocales:
            if letra == "u":
                cadenaparaconvertir.append(vocales[0])
            else:
                vocalsiguiente = vocales[vocales.index(letra) + 1]
                cadenaparaconvertir.append(vocalsiguiente)
        else:
            cadenaparaconvertir.append(letra)
    return "".join(cadenaparaconvertir)
                


def cadena_palindromo(cadena):
    """
        Se ingresan una cadena y la funcion devuelve si
        la cadena es palindromo o no
    """
    cadena = str(cadena).lower().replace(" ","")
    return cadena == cadena[::-1]
        
    
