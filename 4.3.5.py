# LAB   Cuántos días: escribiendo y usando tus propias funciones

# Tu tarea es escribir y probar una función que toma dos argumentos (un año y un mes) y devuelve el número de días del mes/año dado (mientras que solo febrero es sensible al valor year, tu función debería ser universal).

# La parte inicial de la función está lista. Ahora, haz que la función devuelva None si los argumentos no tienen sentido.

# Por supuesto, puedes (y debes) utilizar la función previamente escrita y probada (LAB 4.3.1.6). Puede ser muy útil. Te recomendamos que utilices una lista con los meses. Puedes crearla dentro de la función - este truco acortará significativamente el código.

# Hemos preparado un código de prueba. Amplíalo para incluir más casos de prueba.


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
    # Escribe tu código nuevo aquí.
    #
    if anio < 1582 or mes < 1 or mes > 12:
        return None
    
    dias = [31,28,31,30,31,30,31,31,30,31,30,31]
        
    if mes == 2 and es_bisiesto(anio):
        return 29
    
    return dias[mes - 1]



prueba_anios = [1900, 2000, 2016, 1987]
prueba_meses = [2, 2, 1, 11]
resultados_pruebas = [28, 29, 31, 30]
for i in range(len(prueba_anios)):
    yr = prueba_anios[i]
    mo = prueba_meses[i]
    print(yr, mo, "->", end="")
    result = dias_en_mes(yr, mo)
    if result == resultados_pruebas[i]:
        print("OK")
    else:
        print("Fallido")
