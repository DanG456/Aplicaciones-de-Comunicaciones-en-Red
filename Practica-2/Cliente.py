#!/usr/bin/env python3
from time import time
from Tablero import *
import socket
HOST = "192.168.0.5"
PORT = 65432
bufferSize = 1024
TCPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCPClientSocket.connect((HOST, PORT))
print("Conectado al Servidor")

Dificultad=input ("\n1.Facil\n2.Dificil.\n\nIngresa la dificultad: ")
TCPClientSocket.send(Dificultad.encode('utf-8'))
Buscaminas=Tablero(int(Dificultad),0)
tiempo_inicial = time()
print("Bienvenido al juego del busca minas\n\n")
while Buscaminas.Estado==1:
          print()
          print()
          Buscaminas.imprimir()
          XY = input("\nIngresa las cordenadas de la casilla que quieres destapar: (X Y):  ")
          X, Y = XY.split(' ')
          TCPClientSocket.send(X.encode('utf-8'))
          TCPClientSocket.send(Y.encode('utf-8'))
          Respuesta = TCPClientSocket.recv(bufferSize)
          if int(Respuesta) == 1:
                  Buscaminas.Estado = 0
                  Buscaminas.destaparM(int(XY[0]), int(XY[2]))
                  Buscaminas.Ganador == 0;
          elif int(Respuesta) == 0:
                  Buscaminas.destapar(int(XY[0]), int(XY[2]))
                  Buscaminas.abiertas += 1
                  if Buscaminas.libres == Buscaminas.abiertas:
                      Buscaminas.Estado = 0
                      Buscaminas.destaparM(int(XY[0]), int(XY[2]))
                      Buscaminas.Ganador == 1



tiempo_final = time()
print("Juego Terminado")
Buscaminas.imprimir()
if Buscaminas.Ganador==1:
    print("Felicitaciones, has ganado el juego")
else:
    print("Lo siento, has perdido, mas suerte para la proxima")
tiempo_ejecucion = tiempo_final - tiempo_inicial
print ("El tiempo de juego: ",tiempo_ejecucion)
TCPClientSocket.close()