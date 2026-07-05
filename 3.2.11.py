# 3.2.11   LAB   La sentencia continue – el Lindo Devorador de Vocales

# Tu tarea aquí es aún más especial que antes: ¡Debes rediseñar el devorador de vocales (feo) del laboratorio anterior y crear un mejor devorador de vocales (lindo) mejorado! Escribe un programa que use:

# un bucle for.
# el concepto de ejecución condicional (if-elif-else).
# la instrucción continue.

# Tu programa debe:
# - pedir al usuario que ingrese una palabra.
# - utilizar palabra = palabra.upper() para convertir la palabra ingresada por el usuario a mayúsculas; hablaremos sobre los llamados métodos de cadena y el upper() muy pronto, no te preocupes.
# - emplea la ejecución condicional y la instrucción continue para "devorar" las siguientes vocales A , E , I , O , U de la palabra ingresada.
# - asigna las letras no consumidas a la variable palabra_sin_vocales e imprime la variable en la pantalla.
# Analiza el código en el editor. Hemos creado palabra_sin_vocales y le hemos asignado una cadena vacía. Utiliza la operación de concatenación para pedirle a Python que combine las letras seleccionadas en una cadena más larga durante los siguientes giros de bucle, y asignarlo a la variable word_without_vowels.

# Prueba tu programa con los datos que le proporcionamos.



palabra_sin_vocales = ""

# Indicar al usuario que ingrese una palabra
# y asignarla a la variable palabra.
palabra = input("Introduce una palabra: ")

palabra = palabra.upper()

for letra in palabra:
    # Completa el cuerpo del bucle.
    if letra == "A":
        continue
    elif letra == "E":
        continue
    elif letra == "I":
        continue
    elif letra == "O":
        continue
    elif letra == "U":
        continue
    else:
        palabra_sin_vocales += letra

# Imprimir la palabra asignada a palabra_sin_vocales.
print(palabra_sin_vocales)
