import time
"""
    En este programa cada vez que el usuario ingresa una contraseña incorrecto
    se le restan los intentos y se le pone una penalizacion de tiempo
"""
passwordVerdadera="islaballena"
password= input("Ingrese la contra: ")
if passwordVerdadera == password :
    print("Bienvenido Usuario")
else:
    for i in range (1, 6):
        if password != "islaballena":
            print ("Tiene " + str(5-i) + " intentos mas y "+ str(i*5)+ " segundos de espera")
            time.sleep(i*5)
            password = input("Intente otra vez: ")
        else:
            break
    if passwordVerdadera == password :
        print("Bienvenido Usuario")
    else:
        print ("Se quedo sin intentos")
