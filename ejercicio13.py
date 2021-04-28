def palabras_capitalizadas(palabra1,palabra2):
    """
        Se ingresan dos palabras y la funcion las compara para saber si
        una palabra era la palabra capitalizada de la otra ingresada
    """
    validar=True
    if palabra1.upper()==palabra2.upper():
        validar=True
    else:
        validar=False
    return validar
palabra1=input("ingresa la primera palabra:  ")
palabra2=input("ingresa la segunda palabra:  ")
print (palabras_capitalizadas(palabra1, palabra2))
