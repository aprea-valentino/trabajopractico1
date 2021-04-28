import random
"""
    Se genera un numero aleatorio del 0-1000
    y el usuario tiene que adivinarlo ingresando numeros
"""
numerosecreto=int(random.randrange(0,1000))
numero=int(input("ingrese un numero de 0 al 1000:  "))
print (numerosecreto)
if numero == numerosecreto:
    print("has acertado a la primera")
else:
    while numero != numerosecreto :
        if str(int(numero)) < str(int(numerosecreto)) :
            numero = int(input("El numero secreto es mayor, ingrese otro numero:  "))
        elif str(int(numero)) > str(int(numerosecreto)):
            numero = int(input("El numero secreto es menor, ingrese otro numero:  "))
    print("Has acertado")
