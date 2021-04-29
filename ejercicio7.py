def año_bisiesto_si_o_no(ano):
    """
        Verifica si el año ingresado es bisiesto
    """
    if ((ano%4 == 0 and ano % 100 != 0) or ano % 400 == 0):
        return True
    else:
        return False
            
def mes_a_dias(mes):
    if mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        return 28
    else:
        return 31

def validar_fecha(ano,mes,dia):
    validar = True
    if (0 > mes or mes > 12):
        validar = False
    if dia > 30 and mes in [4,6,9,11]:
        validar = False
    elif dia > 28 and mes == 2:
        validar = False     
    elif dia > 31:
        validar = False
    if validar == True:
        print ("fecha valida")
    else:
        print("fecha no valida")
        
def dias_faltantes(ano,mes,dia):
    """
        Esta funcion calcula la cantidad de dias
        para completar el mes
    """
    if mes in [4, 6, 9, 11]:
        diasfaltantes = 30 - dia
    elif mes == 2:
        diasfaltantes = 28 - dia
    else:
        diasfaltantes = 31 - dia
    return diasfaltantes


def dias_faltantes_años(ano,mes,dia):
    """
        Esta funcion calcula la cantidad de dias
        que faltan para completar el año
    """
    mes = int(mes)
    total = 0
    for mes in range (1, mes):
        total += mes_a_dias(mes)
    if año_bisiesto_si_o_no(año) == True:
        total = (366 - dia) - total
    else:
        total = (365 - dia) - total
    return total



    
        
    
   
