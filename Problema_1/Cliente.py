import socket
import pickle
import os
import datetime
import threading
import sys
import speech_recognition as sr
import json
from portaudio import *
import pyaudio

personajes = []
BUFFER_SIZE = 1024
HOST = "127.0.0.1"
PORT = 65432

class Personaje():
    def __init__(self, nombre="", cabello="", ojos="", piel="", accesorio="", genero=""):
        self.CABELLO = 0
        self.OJOS = 1
        self.PIEL = 2
        self.ACCESORIO = 3
        self.GENERO = 4
        self.nombre = nombre
        self.caracteristicas = []
        self.caracteristicas.append(cabello)
        self.caracteristicas.append(ojos)
        self.caracteristicas.append(piel)
        self.caracteristicas.append(accesorio)
        self.caracteristicas.append(genero)

    def DescripcionPersonaje(self):
        print("\t" + self.nombre + " [" + "Cabello: " + self.caracteristicas[self.CABELLO] + ", Ojos: " +
              self.caracteristicas[self.OJOS] + ", Piel: " + self.caracteristicas[self.PIEL] + ", Accesorio: " +
              self.caracteristicas[self.ACCESORIO] + ",Genero: " + self.caracteristicas[self.GENERO] + "]\n")
        return

def CargarPersonajes():
    perso = "Personajes.json"
    with open(perso, "r") as crearPerso:
        personajeData = json.load(crearPerso)
        nombre = personajeData["nombre"]
        cabello = personajeData["cabello"]
        ojos = personajeData["ojos"]
        piel = personajeData["piel"]
        accesorio = personajeData["accesorio"]
        genero = personajeData["genero"]
        len_personajes = len(nombre)
        for i in range(len_personajes):
            personajes.append(Personaje(nombre[i], cabello[i], ojos[i], piel[i], accesorio[i], genero[i]))
        print(personajes)

def ObtenerMensajeVoz():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        os.system("clear")
        MostrarTiros(tiros_anteriores)
        print("Es tu turno de adivinar el personaje\nEscuchando ... ")
        audio = r.listen(source)

        try:
            return r.recognize_google(audio)
        except Exception as e:
            return ""


def ObtenerCaracteristica(texto):
    texto = texto.lower()
    accesorios = ["nada", "lentes", "sombrero", "corbata"]  # "tu personaje tiene <accesorio>"
    nombres = ["Carla", "Matilda", "Maria", "Samuel", "Eduardo", "Bob", "Patricio", "Jorge", "Jessica", "Camila",
               "Paulina"]  # "tu personaje es <genero_nombre>"
    generos = ["mujer", "hombre"]

    caracteristicas = [" ojo", " cabello", " piel", " genero"]

    i = 0
    for caracteristica in caracteristicas:
        if (caracteristica in texto):
            t = texto.split(caracteristica)
            color = t[1].split(" ")
            if (i == 0):
                caracteristica = caracteristica + "s"
            response = [caracteristica.replace(" ", ""), color[1]]
            return response

        i = i + 1

    if ("tiene" in texto):
        t = texto.split("tiene")
        acc = t[1]
        for accesorio in accesorios:
            if (accesorio in acc):
                return ["accesorio", accesorio]
        return ["accesorio", "nada"]
    else:
        for genero in generos:
            if (genero in texto):
                return ["genero", genero]

        for nombre in nombres:
            if (nombre.lower() in texto):
                return ["nombre", nombre]
    return ""


def MostrarTiros(tiros):
    if (len(tiros) > 0):
        print("\tTiros hasta el momento: ")
        for tiro in tiros:
            print("\t\t" + tiro[0] + " " + tiro[1] + ": " + tiro[2])


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
    TCPClientSocket.connect((HOST, int(PORT)))

    CargarPersonajes()

    while (True):
        jugadoresFaltantes = TCPClientSocket.recv(100)
        os.system("clear")
        if (jugadoresFaltantes.decode() == "0"):
            print("Todos los jugadores se han unido ...")
            break
        else:
            print("Esperando a " + jugadoresFaltantes.decode() + " jugadores ...")

    tiros_anteriores = []

    while (True):
        print("Esperando datos del servidor")
        dato = pickle.loads(TCPClientSocket.recv(BUFFER_SIZE))
        # [MI_TURNO?, QUIEN_TIENE_TURNO, TIRO_ANTERIOR, JUEGO_TERMINADO, RESULTADO, PERSONAJE]

        if (dato[3]):
            break

        if (dato[2] != ""):
            tiros_anteriores = dato[2]

        if (dato[0]):
            while (True):
                texto = ObtenerMensajeVoz()
                if (texto != ""):
                    tiroCliente = ObtenerCaracteristica(texto)
                    if (tiroCliente != ""):
                        TCPClientSocket.sendall(pickle.dumps(tiroCliente))
                        resultado = TCPClientSocket.recv(BUFFER_SIZE)
                        break
                print(texto)
                input("Intentalo de nuevo. Pulsa enter para continuar ...")
        else:
            os.system("clear")
            MostrarTiros(tiros_anteriores)
            print("Esperando a que el jugador " + str(dato[1]) + " termine su turno.")
    os.system("clear")
    print("El personaje era: " + dato[5])
    print(dato[4])
