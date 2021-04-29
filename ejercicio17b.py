def punto_a_stop(texto,longitud, costopcorta, costoplarga):
    """
        Agarra todos los caracteres de un texto y los que se pasen del limite
        los reemplaza por un @ y si hay un "." se lo reemplaza por un STOP
        y al final de todo el texto siempre pone un STOPSTOP
    """
    lista = texto.split(' ')
    lista[-1]=lista[-1].rstrip(".")
    costopcortacant = 0
    costoplargacant = 0
    total = ""
    for i in range(len(lista)):
        if len(lista[i]) > longitud:
            total += lista[i][0:longitud]+"@" + " "
            costoplargacant = costoplargacant + 1
            
            for letra in lista[i]:
                if letra == ".":
                    print(lista[i][-1])
                    total = f"{total.strip()}{lista[i].replace(lista[i], 'STOP ')}"
        else:
            total += lista[i] + " "
            costopcortacant = costopcortacant + 1
            for letra in lista[i]:
                if letra == ".":
                    print(lista[i][-1])
                    total = f"{lista[i].replace(lista[i], 'STOP ')}" 
    total = total.strip() + "STOPSTOP"
    costototal = costopcortacant * costopcorta + costoplargacant * costoplarga
    print ("El telegrama queda ", total," con un costo de: ", costototal,
           " con ", costopcortacant," palabras cortas y con ", costoplargacant," palabras largas ")


