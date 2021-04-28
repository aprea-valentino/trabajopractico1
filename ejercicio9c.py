import time
elboleano = True
passwordVerdadera="islaballena"
password= input("Ingrese la contra: ")
def validar_contraseña(password):
    """
        Es una funcion que para validar si el usuario inicio sesion
        bien devuelve un booleano
    """
    if passwordVerdadera == password :
        elboleano = True
    else:
        for i in range (1, 6):
            if password != "islaballena":
                print ("Tiene " + str(5-i) + " intentos mas y "
                       + str(i*5)+ " segundos de espera")
                time.sleep(i*5)
                password = input("Intente otra vez: ")
                
            else:
                break
    if passwordVerdadera == password :
        print("Bienvenido Usuario")
        elboleano=True
    else:
        print ("Se quedo sin intentos")
        elboleano=False
    return elboleano
print (validar_contraseña(password))
