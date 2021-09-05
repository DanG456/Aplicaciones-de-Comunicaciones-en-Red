import socket
import tkinter as tk
from tkinter import ttk
from tkinter import Label
from datetime import datetime

buffer_size = 1024
#Funciones del codigo

#Numero de días que he vivido (el alumno)
def obtenerEdad():
    limite_compara = datetime(2020,2,20) #Fecha limite para comparar cuanto tiempo ha vivido el alumno
    nacimiento = datetime(1998,11,19) #Fecha de nacimiento del alumno
    diferencia = nacimiento - limite_compara #El dato de los días vividos se devuelve como número con signo negativo
    posdif = -diferencia
    print("Has vivido " + str(posdif.days))
    print("Por lo tanto el juego que te toca es: ")
    dias = diferencia.days
    modulo = dias % 3

    if(modulo == 0):
        print("Te toca buscaminas, por favor ingresa los datos solicitados para iniciar el juego")
    elif (modulo == 1):
        print("Te toca gato dummy, por favor ingresa los datos solicitados para iniciar el juego")
    elif (modulo == 2):
        print ("Te toca memoria, por favor ingresa los datos solicitados para iniciar el juego")
    else:
        print("Error")

obtenerEdad()

#
HOST = input("Ingresa la direccion a la que te quieres conectar")
PORT = input("Ingresa el puerto al que te quieres conectar")
print("La direccion seleccionada es: " + HOST)
print("El puerto seleccionado es: " + PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
    TCPClientSocket.connect((HOST, int(PORT)))
    print("Enviando mensaje...")
    TCPClientSocket.sendall(b"1")
    print("Esperando una respuesta...")
    data = TCPClientSocket.recv(buffer_size)
    print("Recibido,", repr(data), " de", TCPClientSocket.getpeername())



