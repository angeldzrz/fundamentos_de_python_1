# 4.3.4   LAB   Un año bisiesto: escribiendo tus propias funciones

# Tu tarea es escribir y probar una función que toma un argumento (un año) y devuelve True si el año es un año bisiesto, o False si no lo es.

# La semilla de la función ya se muestra en el código esqueleto del editor.

# Nota: también hemos preparado un breve código de prueba, que puedes utilizar para probar tu función.

# El código utiliza dos listas - una con los datos de prueba y la otra con los resultados esperados. El código te dirá si alguno de tus resultados no es válido.


def es_bisiesto(anio):
    #
    # Escribe tu código aquí.
    #
    if anio % 4 != 0:
        return False
    elif anio % 100 != 0:
        return True
    elif anio % 400 != 0:
        return False
    else:
        return True


datos_prueba = [1900, 2000, 2016, 1987]
resultado_pruebas = [False, True, True, False]
for i in range(len(datos_prueba)):
    yr = datos_prueba[i]
    print(yr,"->",end="")
    resultado = es_bisiesto(yr)
    if resultado == resultado_pruebas[i]:
        print("OK")
    else:
        print("Fallido")