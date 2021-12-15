import socket
import pickle
import os
import datetime
import threading
import sys
import speech_recognition as sr
from Personaje import *

personajes = []
BUFFER_SIZE = 1024
HOST, PORT = sys.argv[1:3]

def CargarPersonajes():
    personajes.append( Personaje("Daniel", "Negro", "Cafes", "Morena", "Lentes", "Hombre") )
    personajes.append( Personaje("Norman", "Negro", "Cafes", "Morena", "Nada", "Hombre") )
    personajes.append( Personaje("Jassiel", "Cafe", "Cafes", "Blanca", "Lentes", "Hombre") )
    personajes.append( Personaje("Alejandra", "Negro", "Cafes", "Morena", "Lentes", "Mujer") )
    personajes.append( Personaje("Carlos", "Blanco", "Cafes", "Blanca", "Sombrero", "Hombre") )
    personajes.append( Personaje("Cameron", "Rubio", "Azules", "Blanca", "Corbata", "Hombre") )
    personajes.append( Personaje("Lizbeth", "Rojo", "Cafes", "Blanca", "Nada", "Mujer") )
    personajes.append( Personaje("Diego", "Rubio", "Verdes", "Morena", "Sombrero", "Hombre") )
    personajes.append( Personaje("Giselle", "Cafe", "Grises", "Morena", "Nada", "Mujer") )
    personajes.append( Personaje("Erick", "Blanco", "Cafes", "Morena", "Sombrero", "Hombre") )
    personajes.append( Personaje("Amanda", "Rojo", "Azules", "Blanca", "Sombrero", "Mujer") )

def MostrarPersonajes():
    for personaje in personajes:
        personaje.DescripcionPersonaje()

def ObtenerMensajeVoz():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        os.system( "clear" )
        MostrarPersonajes()
        MostrarTiros(tiros_anteriores)
        print( "Es tu turno de adivinar el personaje\nEscuchando ... ")
        audio = r.listen(source)

        try:    
            return r.recognize_google(audio)	
        except Exception as e:
            return ""

def ObtenerCaracteristica( texto ):
    texto = texto.lower()
    accesorios = ["nada", "lentes", "sombrero", "corbata"] # La frase debe ser "tu personaje tiene <nombre_accesorio>"
    nombres = ["Daniel","Norman","Jassiel","Alejandra","Carlos","Cameron","Lizbeth","Diego","Giselle", "Erick", "Amanda"] # La frase debe ser "tu personaje es <nombre_personaje>"
    generos = ["mujer", "hombre"]

    caracteristicas = [" ojo", " cabello", " piel", " genero"]
    
    i = 0
    for caracteristica in caracteristicas:
        if( caracteristica in texto):
            t = texto.split( caracteristica )
            color = t[1].split(" ")
            if( i == 0):
                caracteristica = caracteristica + "s"
            response = [caracteristica.replace(" ",""), color[1]]
            return response

        i = i + 1
    
    if( "tiene" in texto):
        t = texto.split("tiene")
        acc = t[1]
        for accesorio in accesorios:           
            if( accesorio in acc):
             return ["accesorio", accesorio]             
        return ["accesorio", "nada"]
    else:
        for genero in generos:
            if( genero in texto):
                return ["genero", genero]
        
        for nombre in nombres:
            if( nombre.lower() in texto):
                return ["nombre", nombre]
    return ""

def MostrarTiros(tiros):
    if(len(tiros) > 0):
        print( "\tTiros hasta el momento: ")
        for tiro in tiros:
            print( "\t\t" + tiro[0] + " " + tiro[1] + ": " + tiro[2] )

if len(sys.argv) != 3:
    print( "usage:", sys.argv[0], "<host> <port>" )
    sys.exit(1)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:    
    TCPClientSocket.connect((HOST, int(PORT) ))

    CargarPersonajes()

    while(True):
        jugadoresFaltantes = TCPClientSocket.recv(100)
        os.system( "clear" )
        if(  jugadoresFaltantes.decode() == "0"):
            print( "Todos los jugadores se han unido ..." )
            break
        else:
            print( "Esperando a " + jugadoresFaltantes.decode() + " jugadores ..." )
    
    tiros_anteriores = []
    
    while(True):
        print( "Esperando datos del servidor" )
        dato = pickle.loads( TCPClientSocket.recv(BUFFER_SIZE) ) # [MI_TURNO?, QUIEN_TIENE_TURNO, TIRO_ANTERIOR, JUEGO_TERMINADO, RESULTADO, PERSONAJE]

        if ( dato[3] ):
            break
        
        if( dato[2] != ""):
            tiros_anteriores = dato[2]
        
        if( dato[0] ):            
            while(True):
                texto = ObtenerMensajeVoz()
                if (texto != ""):
                    tiroCliente = ObtenerCaracteristica( texto )
                    if( tiroCliente != ""):
                        TCPClientSocket.sendall( pickle.dumps(tiroCliente) )
                        resultado = TCPClientSocket.recv(BUFFER_SIZE)
                        break
                print(texto)
                input( "Intentalo de nuevo. Pulsa enter para continuar ..." )
        else:
            os.system( "clear" )
            MostrarPersonajes()
            MostrarTiros(tiros_anteriores)
            print( "Esperando a que el jugador " + str(dato[1]) + " termine su turno." )
    os.system( "clear" )
    MostrarPersonajes()
    print( "El personaje era: " + dato[5] )
    print( dato[4] )
