def factorial_de_un_numero(numero):
    """
        Se ingresa un numero y la funcion devuelve
        el factorial del numero    
    """
    factorial = 1
    while numero > 1:
        factorial *= numero
        numero -= 1
    return factorial
