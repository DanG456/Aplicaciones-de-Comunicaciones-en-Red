import socket
from main import pedirPuerto, pedirDireccion
HOSTServer = pedirDireccion()
PORTServer = pedirPuerto()
buffer_size = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
    TCPClientSocket.connect((HOSTServer, PORTServer))
    print("Enviando mensaje...")
    TCPClientSocket.sendall(b"Hello TCP server")
    print("Esperando una respuesta...")
    data = TCPClientSocket.recv(buffer_size)
    print("Recibido,", repr(data), " de", TCPClientSocket.getpeername())