import socket
from _multiprocessing import recv
from random import randrange
def minasP():
    print("                 ")
    print("    1    2   3   ")
    print("   +---+---+---+   ")
    print("a  | %c | %c | %c | " % (M[0],M[1],M[2]))
    print("   +---+---+---+   ")
    print("b  | %c | %c | %c | " % (M[3],M[4],M[5]))
    print("   +---+---+---+   ")
    print("c  | %c | %c | %c | " % (M[6],M[7],M[8]))
    print("   +---+---+---+   ")
    print("                   ")
def ganar(M):
    ganador = True
    for i in range(9):
        if M[i] == '0':
            ganador = False
    return ganador
M=[0,0,0,0,0,0,0,0,0]
#Instancia de objeto para trabajar con el socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 65432

#Con el método bind se indica el puerto al que se va a escuchar y de quien espera la conexion
s.bind(('192.168.0.20',PORT))
print("Servidor en espera")

s.listen(1)
sc,addres = s.accept()
mensaje = "juguemos"

if(mensaje == 'juguemos'):
    print("Partida con el cliente en progreso")
    a = 0
    while(a < 0):
        K = randrange(0,9)
        if(M[K] == '0'):
            M[K] == '1'
            a=a+1
minasP()

while True:
    p = int.from_bytes(sc.recv(2),byteorder="little")
    if(M[p] == '1'):
        K = 'X'
    else:
        K = '*'
        M[p] = '-'
    sc.send(bytes(K,encoding = 'utf-8'))
    gana = ganar(M)
    sc.send(bytes(str(gana),encoding = 'utf-8'))
    if (K == 'X'):
        print("\n Has explotado una bomba")
        break
    elif(gana == True):
        print("\n Felicidades, ganaste el juego :D")
        break
print("\n Fin del juego")
sc.close()
s.close()

