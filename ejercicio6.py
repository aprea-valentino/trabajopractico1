def mayor_multiplo():
    """
        Dados cuatro numeros retorna la multiplicacion mayor
        entre dos de ellos
    """	
    lista=[]
    for posicion in range(4):
	    numero = input("Ingrese uno de los numeros para la cuenta: ")
	    numerox = int(numero)
	    lista.append(numerox)

    lista.sort()
    mayor=lista[3]
    mayor*=lista[2]

    return mayor 
print (mayor_multiplo())
