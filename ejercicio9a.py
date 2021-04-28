""" El programa usa una password y si el usuario pone una password
    que no es la ingresado por el programa se le resta los intentos
"""
passwordVerdadera="islaballena"
password= input("Ingrese la contra: ")
if passwordVerdadera == password :
    print("Bienvenido Usuario")
else:
    for i in range (1, 6):
        if password != "islaballena":
            print ("Tiene " + str(5-i) + " intentos mas.")
            password = input("Intente otra vez: ")
        else:
            break
    if passwordVerdadera == password :
        print("Bienvenido Usuario")
    else:
        print ("Se quedo sin intentos")
