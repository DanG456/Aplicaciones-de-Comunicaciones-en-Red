import socket

HOSTClient = "127.0.0.1"
PORTClient = 65432
buffer_size = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:
    TCPServerSocket.bind((HOSTClient, PORTClient))
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
            Client_conn.sendall(data)
