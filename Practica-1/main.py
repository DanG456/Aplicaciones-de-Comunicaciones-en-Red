import socket
socket.getaddrinfo('127.0.0.1',65432)
from datetime import datetime

buffer_size = 1024
#Funciones del codigo

#Numero de días que he vivido (el alumno)
def obtenerEdad():
    limite_compara = datetime(2021,8,26) #Fecha limite para comparar cuanto tiempo ha vivido el alumno
    nacimiento = datetime(1998,11,19) #Fecha de nacimiento del alumno
    diferencia = nacimiento - limite_compara #El dato de los días vividos se devuelve como número con signo negativo
    posdif = -diferencia
    print("Has vivido " + str(posdif.days) + " dias")
    print("Por lo tanto el juego que te toca es: ")
    dias = diferencia.days
    modulo = dias % 3

    if(modulo == 0):
        print("Buscaminas, por favor ingresa los datos solicitados para iniciar el juego")
    elif (modulo == 1):
        print("Gato dummy, por favor ingresa los datos solicitados para iniciar el juego")
    elif (modulo == 2):
        print ("Memoria, por favor ingresa los datos solicitados para iniciar el juego")
    else:
        print("Error")

obtenerEdad()

print("este es el clasico juego buscaminas.")
print("el juego consiste en descubrir todas las fichas que no tengan minas(las cuales estan representadas por \"*\"")
print("los numeros que aparecen en la pantalla indica cuantas bomas aparecen al rededor.")
print("cuando aparece el numero 0 es porque no hay ninguna bomba al rededor.")
print("para seleccionar la ficha a destapar tendra que especificar la fila y la columna.")
print("que empieze el juego.")

def modo():
    opcion = input("quiere un juego aleatorio (si = 1)(no = 0): ")
    TCPClientSocket.sendall(bytes(opcion, 'utf-8'))
    print("Esperando una respuesta...")
    data = TCPClientSocket.recv(buffer_size)
    print("El servidor pregunta,", repr(data))
    data = TCPClientSocket.recv(buffer_size)
    print(repr(data))
    opcion = input()
    TCPClientSocket.sendall(bytes(opcion, 'utf-8'))

HOST = input("Ingresa la direccion a la que te quieres conectar \n") #IP que usa el servidor
PORT = input("Ingresa el puerto al que te quieres conectar\n") #Puerto que usa el servidor
print("La direccion seleccionada es: " + HOST)
print("El puerto seleccionado es: " + PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
    TCPClientSocket.connect((HOST, int(PORT)))
    modo()
