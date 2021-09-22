import socket


def buscar():
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

M=[0,0,0,0,0,0,0,0,0]

HOST = input("Ingrese la dirección del servidor al que se desea conectar")
PORT = input("Ingrese el puerto al que se va a conectar")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, int(PORT)))
mensaje="juguemos"
s.send(bytes(mensaje,encoding = 'utf-8'))

buscar()

while True:
    while True:
        f = input("Fila: ")
        if(f == 'a'):
            f = 1
        elif(f == 'b'):
            f = 2
        elif(f=='c'):
            f = 3
        else:
            f = 0
        if(f>0 and f<4):
            c = input("Columna: ")
            if(int(c)>0 and int(c)<4):
                p = 3 * (f-1)+(int(c)-1)
                s.send(p.to_bytes(1,"little"))
                break
        print("\nIngrese el rango correcto")
        k = s.recv(2)
        if(k=='X'):
            M[p]='X'
        else:
            M[p]='*'
        buscar()
        gana = s.recv(1024)
        if(k=='X'):
            print("Has explotado una bomba")
            break
        elif(gana==True):
            print("Felicidades, ganaste el juego :D")
            break
print("Fin del juego")
s.close()





