# 3.4.6   LAB   Los fundamentos de las listas

# Había una vez un sombrero. El sombrero no contenía conejo, sino una lista de cinco números: 1, 2, 3, 4, y 5.

# Tu tarea es:
# - escribir una línea de código que solicite al usuario que reemplace el número central en la lista con un número entero ingresado por el usuario (Paso 1)
# - escribir una línea de código que elimine el último elemento de la lista (Paso 2)
# - escribir una línea de código que imprima la longitud de la lista existente (Paso 3).

lista_sombrero = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

# Paso 1: escribe una línea de código que solicite al usuario
# reemplazar el número de en medio con un número entero ingresado por el usuario.
numero = int(input("Introduce el número a cambiar: "))
lista_sombrero [2] = numero
# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del lista_sombrero[-1]
# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print("Longitud de la lista: ", len(lista_sombrero))
print(lista_sombrero)

