"""
    Se genera un numero de 4 cifras distintas y el jugador tiene que adivinarlo
    con los menos intentos posibles, en cada intento el programa
    te devuelve las condiciencias y los aciertos
    del numero que ingresaste con el numero a adivinar
"""
import random
digitos = ('0','1','2','3','4','5','6','7','8','9')
codigo=''
# Este for genera el codigo sin digitos repetidos
for i in range(4):
    numero= random.choice(digitos)
    while numero in codigo:
        numero=random.choice(digitos)
    codigo= codigo + numero

print("tiene que adivinar un numero de", 4,"cifras distintas")
codigo2=input("Ingresa un codigo:  ")
intentos = 1

while codigo2 != codigo:
    intentos = intentos +1
    aciertos = 0
    coincidencias = 0

    for i in range(4):
        if codigo2[i] == codigo[i]:
            aciertos = aciertos + 1
        elif codigo2[i] in codigo:
            coincidencias = coincidencias + 1
    print ("Tu propuesta(", codigo2, ") tiene", aciertos, " aciertos y "
           , coincidencias, "coincidencias.")

    codigo2= input("ingresa otro codigo:  ")

print ("has acertado en", intentos, " intentos")
           
