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

#Funcion para mostrar el puerto a conectarse del campo entry
#def pedirPuerto():
  #  print("El puerto seleccionado es: " + entryP.get())
 #   PORT = int(entryP.get())

#Funcion para iniciar el proceso de comunicación de forma cliente
def cliente():
    HOST = str(entryD.get())
    PORT = int(entryP.get())
    print("La direccion seleccionada es: " + HOST)
    print("El puerto seleccionado es: " + PORT)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
        TCPClientSocket.connect((HOST, PORT))
        print("Enviando mensaje...")
        TCPClientSocket.sendall(b"Hello TCP server")
        print("Esperando una respuesta...")
        data = TCPClientSocket.recv(buffer_size)
        print("Recibido,", repr(data), " de", TCPClientSocket.getpeername())

obtenerEdad()

#Crear ventana para pedir datos con tkinter para recopilar Direccion del socket
rootD = tk.Tk()
rootD.config(width=300, height=200)
labelD = Label(rootD, text = "Ingresa la dirección del servidor al que te quieres conectar")
labelD.grid(column = 0,row = 0)
#Poner botones para enviar el dato
enviar_datoD =ttk.Button(text = "Enviar", command = cliente)
enviar_datoD.place(x = 100, y = 100)
# Crear caja de texto.
entryD = ttk.Entry(rootD)
# Posicionarla en la ventana.
entryD.place(x=50, y=50)

rootD.mainloop()

#Crear ventana para pedir datos con tkinter para recopilar Puerto del socket
rootP = tk.Tk()
rootP.config(width=300, height=200)
labelP = Label(rootP, text = "Ingresa el puerto al que te quieres conectar")
labelP.grid(column = 0, row = 0)
#Poner botones para enviar el dato
enviar_datoP =ttk.Button(text = "Enviar", command = cliente)
enviar_datoP.place(x = 100, y = 100)
# Crear caja de texto.
entryP = ttk.Entry(rootP)
# Posicionarla en la ventana.
entryP.place(x=50, y=50)

rootP.mainloop()

