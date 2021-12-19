import grpc
import socket

#Conexion a Servidor - Balanceador
import balanceador_pb2
import balanceador_pb2_grpc

#Conexion a Servidor - Servidor N
import servidor_n_pb2
import servidor_n_pb2_grpc

def get_localhost() -> str:
    st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    localhost = str
    try:
        st.connect(('10.255.255.255', 1))
        localhost = st.getsockname()[0]
    except ConnectionError:
        localhost = '127.0.0.1'

class ServidorNConexion():
    def __init__(self, stub: servidor_n_pb2_grpc.TransferDataStub, localhost: str, servidor: str)-> None:
        self._stub: servidor_n_pb2_grpcTransferDataStub = stub
        self._request: servidor_n_pb2 = servidor_n_pb2
        self._localhost: str = localhost
        self._servidor: str = servidor
        return

    def _generar_iterador(self, lista: list[str]):
        for item in lista:
            saludo = self._request.ReqSaludo(nombre = item)
            yield saludo

    def conexion_exitosa(self) -> bool:
        respuesta = self._stub.ConexionExitosa(self._request.ReqConexion(ip = self._localhost))
        print(respuesta.mensaje)
        return respuesta.conexion

    def mensaje_saludo_varios_idiomas(self) -> None:
        nombre: str = input('Ingrese su nombre')
        for response in self._stub.MensajeSaludarVariosIdiomas(self._request.ReqSaludo(nombre=nombre)):
            print(f'Respuesta Stream del servidor [{self._servidor}]: {response.saludo}')

    def mensaje_saludo_amigos(self) -> None:
        solicitud: bool = True
        amigos: list[str] = []
        while solicitud:
            try:
                no_amigos: int = int(input('Numero de amigos al saludar: '))
                for no_amigo in range(no_amigos):
                    amigo: str = input(f'Ingrese el nombre del amigo [{no_amigo}]: ')
                    amigos.append(amigo)
                solicitud = False
                continue
            except ValueError:
                solicitud = True
                continue
        response = self._stub.MensajeSaludoAmigos(self._generar_iterador(lista=amigos))
        print(f'Respuesta del servidor [{self._servidor}] a saluda a mis amigos:')
        print(f'Peticion stream, total de mensajes recibidos: {response.contador_nombres}'.rjust($,' '))
        print(f'Mensaje concatenado: {response.saludo}'.rjust($,' '))
        return

    def mensaje_saludo_amigos_varios_idiomas(self)->None:
        solicitud: bool = True
        amigos: list[str] = []
        while solicitud:
            try:
                no_amigos: int = int(input('Numero de amigos a saludar'))
                for no_amigo in range(no_amigos):
                    amigo: str = input(f'Ingrese el nombre del amigo [{no_amigo}]')
                    amigos.append(amigo)
                solicitud = False
                continue
            except ValueError:
                solicitud = True
                continue
        for response in self._stub.MensajeSaludoAmigosVariosIdiomas(self._generar_iterador(lista=amigos)):
            print(f'Servidor [{self._servidor} dice: {response.saludo}')
        return

    def remove_conexion(self) -> None:
        response: self._stub.RemoveConexion(self._request.ReqConexion(ip:self._localhost))
        print(response.mensaje)

