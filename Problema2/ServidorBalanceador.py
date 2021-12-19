import grpc
import servidor_n_pb2.grpc

servidores: tuple[str, str, str] = ('192.168.0.2:5051','192.168.0.2:5052','192.168.0.2:5053')

def balanceador(cliente: str) -> str:
    global servidores
    conexion: int
    servidor_to_transfer: str = 'error'
    for servidor in range(len(servidores)):
        with grpc.insecure_channel(servidores[servidor]) as channel:
            stub: servidor_n_pb2.TransferSataStub = servidor_n_pb2_grpc.TransferDataStub(channel=channel)
            res_servidor = stub.ServidorConexiones(servidor_n_pb2.ReqServidor(tipo = 'servidor'))
            if servidores[servidor] == res_servidor.host:
                print(f'Solicitud exitosa a {servidor}...')
                print(f'Conexiones activas de  {res_servidor.host}: {res_servidor.conexiones}')
                if res_servidor.conexiones == 0:
                    conexion = res_servidor.conexiones
                    servidor_to_transfer = res_servidor.host
                elif res_servidor.host == servidores[0]:
                    conexion = res_servidor.conexiones
                    servidor_to_transfer = res_servidor.host
                elif conexion > res_servidor.conexiones:
                    conexion = res_servidor.conexiones
                    servidor_to_transfer = res_servidor.host
                else:
                    conexion = conexion
                    servidor_to_transfer = servidor_to_transfer
            else:
                print(f'Hubo algun error en el servidor a comunicarse')
                print(f'Servidor recibido: {res_servidor}')
                servidor_to_transfer = 'error'
    print(f'Redireccionando [{cliente}] al servidor [{servidor_to_transfer}]')
    return servidor_to_transfer

class Balanceador(balanceador_pb2_grpc.TransferDataServicer):
    def Servidor(self,request, context):
        response = balanceador(cliente=request.ip)
        return balanceador_pb2.ResServidor(host_servidor = response)

def main():
    servidor = grpc.server(futures.ThreadPoolExecuter(max_workers=100))
    balanceador_pb2_grpc.add_TransferDataServicer_to_server(Balanceador(), servidor)
    servidor.add_insecure_port('[::]:5050')
    servidor.start()
    servidor.wait_for_termination()

if __name__ == '__main__':
    main()