# 3.1.10   LAB   Operadores de comparación y ejecución condicional

# Espatifilo, más comúnmente conocida como la planta de Cuna de Moisés o flor de la paz, es una de las plantas para interiores más populares que filtra las toxinas dañinas del aire. Algunas de las toxinas que neutraliza incluyen benceno, formaldehído y amoníaco.

# Imagina que tu programa de computadora ama estas plantas. Cada vez que recibe una entrada en forma de la palabra Espatifilo, grite involuntariamente a la consola la siguiente cadena: "¡Espatifilo es la mejor planta de todas!"

# Escribe un programa que utilice el concepto de ejecución condicional, tome una cadena como entrada y que:
# - imprima el enunciado "Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!" en la pantalla si la cadena ingresada es "ESPATIFILO" (mayúsculas)
# - imprima "No, ¡quiero un gran Espatifilo!" si la cadena ingresada es "espatifilo" (minúsculas)
# - imprima "¡Espatifilo!, ¡No [entrada]!" de lo contrario. Nota: [entrada] es la cadena que se toma como entrada.

# Prueba tu código con los datos que te proporcionamos. ¡Y hazte de un Espatifilo también!# 

entrada = input("Introduce una cadena: ")

if entrada == "ESPATIFILO":
    print("Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!")
elif entrada == "espatifilo":
    print("No, ¡quiero un gran Espatifilo!")
else:
    print("¡Espatifilo!, ¡No", entrada, "!")