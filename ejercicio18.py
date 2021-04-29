def inversion_de_listas(lista):
    """
        Se ingresa un lista y la devuelve una nueva lista
        con el contenido invertido+
    """
    if not lista:
        return 1
    listainvertida = []
    for palabra in lista:
        listainvertida.insert(0, palabra)
    return listainvertida

def inversion_con_una_lista(lista):
    """
        Se ingresa un lista y la funcion te devuelve
        la misma lista invertida
    """
    if not lista:
        return 1
    
    for i in range (int(len(lista)/2)):
        lista[i], lista[-i-1] = lista[-i-1], lista[i]
        
    return lista
    
   
    
