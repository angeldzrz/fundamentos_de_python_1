# 4.3.8   LAB   Conversión del consumo de combustible

# El consumo de combustible de un automóvil se puede expresar de muchas maneras diferentes. Por ejemplo, en Europa, se muestra como la cantidad de combustible consumido por cada 100 kilómetros.

# En los EE. UU., se muestra como la cantidad de millas recorridas por un automóvil con un galón de combustible.

# Tu tarea es escribir un par de funciones que conviertan l/100km a mpg (milas por galón), y viceversa.

# Las funciones:

# se llaman litros_100km_a_millas_galon y millas_galon_a_litros_100km respectivamente;
# toman un argumento (el valor correspondiente a sus nombres)
# Complementa el código en el editor y ejecuta tu código y verifica si tu salida es la misma que la nuestra.

# Aquí hay información para ayudarte:

# 1 milla = 1609.344 metros.
# 1 galón = 3.785411784 litros.



def litros_100km_a_millas_galon(litros):
    #
    # Escribe tu código aquí.
    #
    galones = litros / 3.785411784
    millas = 100 / 1.609344

    consumo = millas / galones

    return consumo


def millas_galon_a_litros_100km(millas):
    #
    # Escribe tu código aquí.
    #

    litros = 3.785411784
    kilometros = millas * 1.609344

    consumo = litros / kilometros * 100

    return consumo


print(litros_100km_a_millas_galon(3.9))
print(litros_100km_a_millas_galon(7.5))
print(litros_100km_a_millas_galon(10.))
print(millas_galon_a_litros_100km(60.3))
print(millas_galon_a_litros_100km(31.4))
print(millas_galon_a_litros_100km(23.5))
