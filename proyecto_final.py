#  PROYECTO  Tic-Tac-Toe

# Tu tarea es escribir un simple programa que simule jugar a tic-tac-toe (nombre en inglés) con el usuario. Para hacerlo más fácil, hemos decidido simplificar el juego. Aquí están nuestras reglas:

# la maquina (por ejemplo, el programa) jugará utilizando las 'X's;
# el usuario (por ejemplo, tu) jugarás utilizando las 'O's;
# el primer movimiento es de la maquina - siempre coloca una 'X' en el centro del tablero;
# todos los cuadros están numerados comenzando con el 1 (observa el ejemplo para que tengas una referencia)
# el usuario ingresa su movimiento introduciendo el número de cuadro elegido - el número debe de ser valido, por ejemplo un valor entero mayor que 0 y menor que 10, y no puede ser un cuadro que ya esté ocupado;
# el programa verifica si el juego ha terminado - existen cuatro posibles veredictos: el juego continua, el juego termina en empate, tu ganas, o la maquina gana;
# la maquina responde con su movimiento y se verifica el estado del juego;
# no se debe implementar algún tipo de inteligencia artificial - la maquina elegirá un cuadro de manera aleatoria, eso es suficiente para este juego.
# El ejemplo del programa es el siguiente:

# +-------+-------+-------+
# |       |       |       |
# |   1   |   2   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   6   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   8   |   9   |
# |       |       |       |
# +-------+-------+-------+# 
# Ingresa tu movimiento: 1
# +-------+-------+-------+
# |       |       |       |
# |   O   |   2   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   6   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   8   |   9   |
# |       |       |       |
# +-------+-------+-------+
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   6   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   8   |   9   |
# |       |       |       |
# +-------+-------+-------+# 
# Ingresa tu movimiento: 8
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   6   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   O   |   9   |
# |       |       |       |
# +-------+-------+-------+
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   4   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   O   |   9   |
# |       |       |       |
# +-------+-------+-------+# 
# Ingresa tu movimiento: 4
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   3   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   O   |   9   |
# |       |       |       |
# +-------+-------+-------+
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   7   |   O   |   9   |
# |       |       |       |
# +-------+-------+-------+# 
# Ingresa tu movimiento: 7
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   O   |   X   |   X   |
# |       |       |       |
# +-------+-------+-------+
# |       |       |       |
# |   O   |   O   |   9   |
# |       |       |       |
# +-------+-------+-------+
# ¡Has Ganado!

# Requerimientos
# Implementa las siguientes características:

# el tablero debe ser almacenado como una lista de tres elementos, mientras que cada elemento es otra lista de tres elementos (la lista interna representa las filas) de manera que todos los cuadros puedas ser accedidos empleado la siguiente sintaxis:

# board[fila][columna]
 

# cada uno de los elementos internos de la lista puede contener 'O', 'X', o un digito representando el número del cuadro (dicho cuadro se considera como libre)
# la apariencia de tablero debe de ser igual a la presentada en el ejemplo.
# implementa las funciones definidas para ti en el editor.

# Para obtener un valor numérico aleatorio se puede emplear una función integrada de Python denominada randrange(). El siguiente ejemplo muestra como utilizarla (El programa imprime 10 números aleatorios del 1 al 8).

# Nota: la instrucción from-import provee acceso a la función randrange definida en un módulo externo de Python denominado random.

# from random import randrange
 
# for i in range(10):
#    print(randrange(8))




from random import randrange


def mostrar_tablero(tablero):
    print("+-------" * 3, "+", sep="")
    for fila in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(tablero[fila][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")


def ingresar_movimiento(tablero):
    ok = False
    while not ok:
        movimiento = input("Ingresa tu movimiento: ")
        ok = len(movimiento) == 1 and movimiento >= '1' and movimiento <= '9'
        if not ok:
            print("Movimiento erróneo, ingrésalo nuevamente")
            continue
        
        # Convierte el número del 1 al 9 ingresado por el usuario en coordenadas (fila, columna)
        movimiento = int(movimiento) - 1
        fila = movimiento // 3
        col = movimiento % 3
        
        marca = tablero[fila][col]
        ok = marca not in ['O', 'X']
        if not ok:
            print("¡Cuadro ocupado, ingresa nuevamente!")
            continue
    tablero[fila][col] = 'O'


def lista_de_campos_libres(tablero):
    libres = []
    for fila in range(3):
        for col in range(3):
            if tablero[fila][col] not in ['O', 'X']:
                libres.append((fila, col))
    return libres


def victoria_de(tablero, sgn):
    if sgn == "X":
        ganador = 'maquina'
    elif sgn == "O":
        ganador = 'usuario'
    else:
        ganador = None
        
    linea1 = linea2 = True  # Control para las dos diagonales
    for rc in range(3):
        if tablero[rc][0] == sgn and tablero[rc][1] == sgn and tablero[rc][2] == sgn:  # Filas
            return ganador
        if tablero[0][rc] == sgn and tablero[1][rc] == sgn and tablero[2][rc] == sgn:  # Columnas
            return ganador
        if tablero[rc][rc] != sgn:  # Diagonal principal
            linea1 = False
        if tablero[2 - rc][2 - rc] != sgn:  # Diagonal secundaria
            linea2 = False
    if linea1 or linea2:
        return ganador
    return None


def movimiento_maquina(tablero):
    libres = lista_de_campos_libres(tablero)
    cnt = len(libres)
    if cnt > 0:
        este = randrange(cnt)
        fila, col = libres[este]
        tablero[fila][col] = 'X'


# Inicializa el tablero con números del 1 al 9 y coloca la primera 'X' de la máquina en el centro
tablero = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
tablero[1][1] = 'X'
libres = lista_de_campos_libres(tablero)
turno_humano = True

while len(libres):
    mostrar_tablero(tablero)
    if turno_humano:
        ingresar_movimiento(tablero)
        ganador = victoria_de(tablero, 'O')
    else:
        movimiento_maquina(tablero)
        ganador = victoria_de(tablero, 'X')
    if ganador != None:
        break
    turno_humano = not turno_humano
    libres = lista_de_campos_libres(tablero)

mostrar_tablero(tablero)
if ganador == 'usuario':
    print("¡Has ganado!")
elif ganador == 'maquina':
    print("¡He ganado!")
else:
    print("¡Empate!")