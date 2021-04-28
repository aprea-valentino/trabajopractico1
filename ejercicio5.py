def fahrenheit_a_celsius(fahrenheit):
    '''
        Convierte un valor dado en Fahrenheit a Celsius.
    '''
    celsius =(fahrenheit - 32) * 5/9
    return int(celsius)

print ("Fahrenheit  |  Celsius")
print ('------------|----------')

for i in range (0, 130):
    if (i % 10) == 0:
        if i == 0:
            print ( '      ' + str(i) + '     |    ' + str (fahrenheit_a_celsius(i)))
        elif i >= 100:
            print ( '     ' + str(i) + '    |    ' + str (fahrenheit_a_celsius(i)))
        else:
            print ( '     ' + str(i) + '     |    ' + str(fahrenheit_a_celsius(i)))
        print ('------------|----------')
