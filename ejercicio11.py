def revision_de_examenes(cantidad, porcentaje):
    """
        Se ingresa la cantidad de ejercicios que completa un alumno
        y dependiendo del porcentaje para aprobar la funcion devuelve
        si aprobo o no
    """
    valorcentinela  = ""
    cantidadporcentaje = (cantidad*porcentaje)//100
    numerosdealumnos = 0
    while valorcentinela != "termine":
        cantidadresueltos=int(input("Ingrese la cantidad de ejercicios resueltos:  "))
        if cantidadresueltos >= cantidadporcentaje:
            examen = "Aprobado"
        else:
            examen = "Desaprobado"
        numerosdealumnos += 1
        print("El alumno ", numerosdealumnos, " ha ", examen)
        valorcentinela = input("Ingrese 'termine' si desea terminar el examen:  ")
    
