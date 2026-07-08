# 4.3.6   LAB   Día del año: escribiendo y usando tus propias funciones

# Tu tarea es escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes) y devuelve el día correspondiente del año, o devuelve None si cualquiera de los argumentos no es válido.

# Debes utilizar las funciones previamente escritas y probadas. Agrega algunos casos de prueba al código. Esta prueba es solo el comienzo.



def es_bisiesto(anio):
    #
    # Tu código del LAB anterior.
    #
    if anio % 4 != 0:
        return False
    elif anio % 100 != 0:
        return True
    elif anio % 400 != 0:
        return False
    else:
        return True

def dias_en_mes(anio, mes):
    #
    # Tu código del LAB anterior.
    #
    if anio < 1582 or mes < 1 or mes > 12:
        return None
    
    dias = [31,28,31,30,31,30,31,31,30,31,30,31]
        
    if mes == 2 and es_bisiesto(anio):
        return 29
    
    return dias[mes - 1]

def dia_del_anio(anio, mes, dia):
    #
    # Escribe tu código nuevo aquí.
    #

    dias = 0

    for m in range(1, mes):
        dm = dias_en_mes(anio, m)
        if dm == None:
            return None
        dias += dm

    dm = dias_en_mes(anio, mes)
    if dia >= 1 and dia <= dm:
        return dias + dia
    else:
        return None

print(dia_del_anio(2000, 12, 31))
