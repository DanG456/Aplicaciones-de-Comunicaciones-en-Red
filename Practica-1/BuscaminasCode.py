#Archivo donde se construye el juego del buscaminas

from random import randint

# crear matriz, esta funcion no invoca ninguna otra funcion del programa
def matriz(filas, columnas, caracter=False):
    tablero = []
    for i in range(0, filas):
        v = [caracter] * columnas
        tablero.append(v)
    return tablero


# poner minas aleatoriamente, esta funcion no invoca ninguna otra funcion del programa
def minas(filas, columnas, tablero, minaz):
    mi = 1
    while mi <= minaz:
        fil = randint(0, filas - 1)
        col = randint(0, columnas - 1)
        if not tablero[fil][col]:
            tablero[fil][col] = True
            mi += 1
    return tablero


# se crea el tablero de acuerdo a las especificaciones del jugador esta funcion invoca
# a la funcion matriz(es para crear una matriz dado el numero de filas y columnas)
# y a la funcion minas(es para colocar las pistas. las pistas son los numeros que aparecen en el juego)
def tablero1():
    opcion = input("quiere un juego aleatorio (si = 1)(no = 0): ")
    if opcion:
        while True:
            print("que dificultad desea?")
            print("\t1. principiante")
            print("\t2. avanzado")

            opcion = input("elija una opcion(p o principiante)(a o avanzado): ")
            if opcion.lower() == ("p" or "principiante"):
                tablero = matriz(9, 9)
                minas(9, 9, tablero, 10)
                return tablero, 9, 9
            elif opcion.lower() == ("a" or "avanzado"):
                tablero = matriz(16, 16)
                minas(16, 16, tablero, 40)
                return tablero, 16, 16
            else:
                print("debe escoger una de las opciones del menu.")
    else:
        filas = input("ingresa el numero de filas que deseas: ")
        columnas = input("ingresa el numero de columnas que desea: ")
        while True:
            mina = input("ingresa el numero de minas que desea: ")
            if mina <= filas * columnas:
                break
            print("el numero de minas debe ser menor que %d." % (filas * columnas))
        tablero = matriz(filas, columnas)
        minas(filas, columnas, tablero, mina)
        return tablero, filas, columnas


# poner las pistas que son los numeros que aparecen en el tablero
# esta funcion solo hace uso de la funcion matriz
def numeros(tablero, filas, columnas):
    nueva = matriz(filas, columnas, ".")
    for i in range(0, filas):
        for j in range(0, columnas):
            # calcular el numero de vecinos de la celula que se esta vicitando
            n = 0
            if i > 0 and j > 0 and tablero[i - 1][j - 1]:
                n += 1
            if j > 0 and tablero[i][j - 1]:
                n += 1
            if i < filas - 1 and j > 0 and tablero[i + 1][j - 1]:
                n += 1
            if i > 0 and tablero[i - 1][j]:
                n += 1
            if i < filas - 1 and tablero[i + 1][j]:
                n += 1
            if i > 0 and j < columnas - 1 and tablero[i - 1][j + 1]:
                n += 1
            if j < columnas - 1 and tablero[i][j + 1]:
                n += 1
            if i < filas - 1 and j < columnas - 1 and tablero[i + 1][j + 1]:
                n += 1
            if not tablero[i][j]:
                nueva[i][j] = n
            else:
                nueva[i][j] = True
    tablero = nueva
    return tablero


# mostrar el tablero de juego, esta funcion no hace uso de ninguna otra funcion
def mostrar(tablero, filas, columnas, caracter):
    for i in range(0, filas):
        for j in range(0, columnas):
            if j != columnas - 1:
                if type(tablero[i][j]) == (int or str):
                    print(tablero[i][j],)
                elif (type(tablero[i][j]) == bool) and (tablero[i][j]):
                    print("*",)
                else:

                    print(caracter,)
            else:
                if type(tablero[i][j]) == (int or str):
                    print(tablero[i][j])
                elif (type(tablero[i][j]) == bool) and (tablero[i][j]):
                    print("*")
                else:

                    print(caracter)


# esta es la funcion que desapa el tablero
def destapar(filas, columnas, fila, columna, tablero, nuevo):
    nuevo[fila][columna] = tablero[fila][columna]
    if tablero[fila][columna] == 0:
        if fila > 0:
            if (not tablero[fila - 1][columna]) and (nuevo[fila - 1][columna] != 0):
                destapar(filas, columnas, fila - 1, columna, tablero, nuevo)
            else:
                nuevo[fila - 1][columna] = tablero[fila - 1][columna]
        if fila < filas - 1:
            if (not tablero[fila + 1][columna]) and (nuevo[fila + 1][columna] != 0):
                destapar(filas, columnas, fila + 1, columna, tablero, nuevo)
            else:
                nuevo[fila + 1][columna] = tablero[fila + 1][columna]
        if columna > 0:
            if (not tablero[fila][columna - 1]) and (nuevo[fila][columna - 1] != 0):
                destapar(filas, columnas, fila, columna - 1, tablero, nuevo)
            else:
                nuevo[fila][columna - 1] = tablero[fila][columna - 1]
        if columna < columnas - 1:
            if (not tablero[fila][columna + 1]) and (nuevo[fila][columna + 1] != 0):
                destapar(filas, columnas, fila, columna + 1, tablero, nuevo)
            else:
                nuevo[fila][columna + 1] = tablero[fila][columna + 1]


# esta funcion toma la jugada del jugador, esta funcion no hace uso de ninguna otra funcion
def jugada(filas, columnas):
    print("para hacer su jugada debe especificar tanto la fila como la columna.")
    while True:
        fila = input("ingrese la fila: ")
        columna = input("ingrese la columna: ")
        if (1 <= int(fila) <= int(filas)) and (1 <= int(columna) <= int(columnas)):
            break
        print("debe escoger una ficha que este dentro del rango de fila y columna.")
    return fila, columna


# esta es la funcion principal en la que corre el juego. esta funcion hace uso de las siguientes funciones
# matriz : cre una matriz dado el numero de filas y de columnas
# mostrar : esta funcion muestra cualquier matriz en forma de tablero
# jugada : esta funcion toma la jugada que hace el jugador
def jugar(tablero, filas, columnas):
    nueva = matriz(filas, columnas, ".")
    while True:
        mostrar(nueva, filas, columnas, ".")
        fila, columna = jugada(filas, columnas)
        if type(tablero[int(fila) - 1][int(columna) - 1]) == int:
            nueva[int(fila) - 1][int(columna) - 1] = tablero[int(fila) - 1][int(columna) - 1]
            if tablero[int(fila) - 1][int(columna) - 1] == 0:
                destapar(filas, columnas, int(fila) - 1, int(columna) - 1, tablero, nueva)
        else:
            mostrar(tablero, filas, columnas, " ")
            print("has perdido!!!")
            print("eso te pasa por destapar la ficha en la posicion (%d,%d)." % (int(fila), int(columna)))
            break
        acabar = True
        for i in range(0, filas):
            for j in range(0, columnas):
                if nueva[i][j] == ".":
                    acabar = False
                    break
                if not acabar:
                    break
        if acabar:
            print("Ganaste el juego.")
            print("felicitaciones!!!")


print("este es el clasico juego buscaminas.")
print("el juego consiste en descubrir todas las fichas que no tengan minas(las cuales estan representadas por \"*\"")
print("los numeros que aparecen en la pantalla indica cuantas bomas aparecen al rededor.")
print("cuando aparece el numero 0 es porque no hay ninguna bomba al rededor.")
print("para seleccionar la ficha a destapar tendra que especificar la fila y la columna.")
print("que empieze el juego.")

jugar1 = True

while jugar1:
    tablero, filas, columnas = tablero1()
    tablero = numeros(tablero, filas, columnas)
    jugar(tablero, filas, columnas)

    jugar1 = input("desea jugar ora vez (si = 1)(no = 0)")