# 3.2.10   LAB   La sentencia continue – el Feo Devorador de Vocales

# La sentencia continue se usa para omitir el bloque actual y avanzar a la siguiente iteración, sin ejecutar las sentencias dentro del bucle.

# Se puede usar tanto con bucles while y for.

# Tu tarea aquí es muy especial: ¡Debes diseñar un devorador de vocales! Escribe un programa que use:
# - un bucle for;
# - el concepto de ejecución condicional (if-elif-else).
# - la sentencia continue.

# Tu programa debe:
# - pedir al usuario que ingrese una palabra.
# - utiliza palabra = palabra.upper() para convertir la palabra ingresada por el usuario a mayúsculas; hablaremos sobre los llamados métodos de cadena y el método upper() muy pronto, no te preocupes
# - utiliza la ejecución condicional y la instrucción continue para "devorar" las siguientes vocales A, E, I, O, U de la palabra ingresada.
# - imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada

# Prueba tu programa con los datos que le proporcionamos.

# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable palabra.
palabra = input("Introduce una palabra: ")

palabra = palabra.upper()

for letra in palabra:
    # Completa el cuerpo del bucle for.
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
        print(letra)
