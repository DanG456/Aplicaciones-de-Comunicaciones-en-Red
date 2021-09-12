import socket
from random import randint
HOST = "192.168.0.16"
PORT = 65432
buffer_size = 1024

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

#Recopilacion del nivel del buscaminas elegido por el usuario
def nivel():
    if (data == b'1'):

        string = "que dificultad desea? Introduzca como se indica en parentesis"
        string2 = "1. principiante (p o principiante) "
        string3 = "2. avanzado (a o avanzado)"
        Client_conn.sendall(bytes(string,'utf-8'))
        Client_conn.sendall(bytes(string2,'utf-8'))
        Client_conn.sendall(bytes(string3,'utf-8'))

def tablero1():
    print("Recibido,", data, "   de ", Client_addr)
    stringP1 = "p"
    stringPrin = "principiante"
    stringA1 = "a"
    stringAvan = "avanzado"
    if data == (bytes(stringP1,'utf-8') or bytes(stringPrin,'utf-8')):
        tablero = matriz(9, 9)
        minas(9, 9, tablero, 10)
        return tablero, 9, 9
    elif data == (bytes(stringA1,'utf-8') or bytes(stringAvan,'utf-8')):
        tablero = matriz(16, 16)
        minas(16, 16, tablero, 40)
        return tablero, 16, 16
    else:
       print("Error")


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
                    Client_conn.sendall(bytes(tablero[i][j],'ascii'))
                elif (type(tablero[i][j]) == bool) and (tablero[i][j]):
                    Client_conn.send(bytes("*",ascii))
                else:

                    Client_conn.sendall(caracter,'ascii')
            else:
                if type(tablero[i][j]) == (int or str):
                    Client_conn.sendall(bytes(tablero[i][j],'ascii'))
                elif (type(tablero[i][j]) == bool) and (tablero[i][j]):
                    Client_conn.sendall(bytes("*",'ascii'))
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


#Abrir el socket y esperar por las solicitudes del cliente
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:
    TCPServerSocket.bind((HOST, PORT))
    TCPServerSocket.listen()
    print("El servidor TCP está disponible y en espera de solicitudes")

    Client_conn, Client_addr = TCPServerSocket.accept()
    with Client_conn:
        print("Conectado a", Client_addr)
        while True:
            print("Esperando a recibir datos... ")
            data = Client_conn.recv(buffer_size)
            print ("Recibido,", data,"   de ", Client_addr)

            if not data:
                break
            print("Enviando respuesta a", Client_addr)

            nivel()
            tablero,filas,columnas = tablero1()
            tablero = numeros(tablero,filas,columnas)
            jugar(tablero,filas,columnas)
