def contar_vocales(cadena):
    """
        Se ingresa una cadena y la funcion devuelve
        la cantidad de vocales que hay.
    """
    cadena.lower()
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    for letra in cadena:
        if letra == "a":
            a += 1
        elif letra == "e":
            e += 1
        elif letra == "i":
            i += 1
        elif letra == "o":
            i += 1
        elif letra == "u":
            u += 1
    print (f"""Cantidad de a: , {a}
Cantidad de e: , {e}
Cantidad de i: , {i}
Cantidad de o: , {o}
Cantidad de u: , {u}""")
