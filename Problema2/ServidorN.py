from concurrent import futures
import grpc
import logging
import socket
import sys

#Trabajo servidor
import servidor_n_pb2
import servidor_n_pb2_grpc

conectados: int = 0
puerto: int
localhost: str
lista_saludos: list[str] = {'Hello','Salut', 'Hola','Hallo'}

def get_localhost() -> str:
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    localhost = str
    try:
        st.connect(('10.255.255.255',1))
        localhost = st.getsockname()[0]
    except ConnectionError:
        localhost = '127.0.0.1'
    finally:
        st.close()
    return localhost


def servidor_conexiones(tipo:str)->tuple[str, int]:
    global puerto, conectados, localhost
    respuesta: tuple[str, int]
    if tipo == 'servidor':
        print('Peticion del servidor balanceador correcta')
    else:
        print('Peticion del servidor balanceador incorrecta')
    respuesta = (localhost, conectados)
    return respuesta

def conexion_exitosa(ip:str) -> tuple[bool,str]:
    respuesta: tuple[bool, str]
    global conectados, localhost
    print(f'El cliente [{ip}] ha solicitado unirse')
    if conectados == 100:
        conectados += 1
        print(f'El cliente [{ip}] se ha unido de manera correcta')
        print(f'Cliente conectado: {conectados}')
        respuesta = (True, f'conexion exitosa con el servidor [{localhost}]')
    else:
        respuesta = (False, f'conexion fallida con el servidor [{localhost}]')
    return respuesta

def remove_conexion(ip:str)->tuple[bool, int]:
    respuesta: tuple[bool, str]
    global conectados, localhost
    conectados -= 1
    if conectados > 0:
        print(f'El cliente [{ip}] se ha desconectado de manera correcta')
        print(f'Gente conectada: {conectados}')
    else:
        print(f'Ha ocurrido un error')
        print(f'Gente conectada: {conectados}')
        conectados = 0
    respuesta = (True, f'Se ha desconectado de forma correcta del servidor [{localhost}]')
    return respuesta

class ServidorN(servidor_n_pb2_grpc.TransferDataServicer):
    def ServidorConexiones(self,request, context):
        response = servidor_conexiones(tipo=request.tipo)
        return servidor_n_pb2.ResConexion(host = response[0], conexiones = response [1])

    def ConexionExitosa(self,request,context):
        response = conexion_exitosa(ip=request.ip)
        return servidor_n_pb2.ResConexion(conexion=response[0], mensaje=response[1])

    #operaciones de saludos
    def MensajeSaludo(self, request, context):
        return servidor_n_pb2.ResSaludo(saludo=f'Hola {request.nombre}')

    def MensajeSaludoVariosIdiomas(self,request, context):
        global lista_saludos
        for idioma in lista_saludos:
            yield servidor_n_pb2_grpc.ResSaludo(saludo=f'{idioma}, {request.nombre}')

    def MensajeSaludoAmigos(self,request_iterator,context):
        contador: int = 0
        saludos: str = 'Hola'
        for request in request_iterator:
            contador += 1
            saludos += f', {request.nombre}'
        return servidor_n_pb2.ResResumenSaludo(contador_nombres = contador, saludo = saludos)

    def MensajeSaludoAmigosVariosIdiomas(self,request_iterator,context):
        global lista_saludos
        for request in request_iterator:
            for idioma in lista_saludos:
                yield servidor_n_pb2.ResSaludo(saludo=f'{idioma}, {request.nombre}')

    def RemoveConexion(self, request, context):
        response = remove_conexion(ip=request.ip)
        return servidor_n_pb2.ResConexion(conexion=response[0],mensaje = response[1])

def main() -> None:
    global localhost, puerto
    if(len(sys.argv)) != 2:
        print(f'Usar: {sys.argv[0]} <Puerto: int>')
        sys.exit(1)
    try:
        puerto =  int(sys.argv[1])
    except ValueError:
        print(f'Usar: {sys.argv[0]} <Puerto: int>')
        sys.exit(1)
    host: str = f'[::]:{puerto}'
    localhost = f'{get_localhost()}:{puerto}'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=102))
    servidor_n_pb2_grpc.add_TransferDataServicer_to_server(ServidorN(),server)
    server.add_insecure_port(host)
    server.start()
    server.wait_for_termination()
    return

if __name__ == '__main__':
    logging.basicConfig()
    main()