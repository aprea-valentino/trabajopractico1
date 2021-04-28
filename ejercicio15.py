def cadena_primera_palabra(cadena):
    """
        Se ingresa un cadena y la funcion devuelve
        solo la primera letra de cada palabra
    """
    lista = cadena.split(" ")
    for palabra in lista:
        print (palabra[0],end="")
    print()
    
def cadena_mayuscula(cadena):
    """
        Se ingresa una cadena y la funcion devuelve la cadena
        pero con mayusculas al principio de cada palabra
    """
    lista = ""
    lista = cadena[0].upper()
    for i in range(1, len(cadena)):
        if cadena[i-1]==" ":
            lista += cadena[i].upper()
        else:
            lista += cadena[i]
    return lista
	
def cadena_palabras_con_a(cadena):
    """
        Se ingresa una cadena y la funcion devuelve
        solo las palabras que comiencen con a/A
    """
    lista=cadena.split(" ")
    total = ""
    for palabra in lista:
        if palabra.startswith("a") or palabra.startswith("A"):
            total += palabra + " "
    return total
    
