# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import Solicitudes_pb2 as Solicitudes__pb2


class CommandsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.User = channel.unary_unary(
                '/practica5.Commands/User',
                request_serializer=Solicitudes__pb2.simple_Request.SerializeToString,
                response_deserializer=Solicitudes__pb2.Response.FromString,
                )
        self.Password = channel.unary_unary(
                '/practica5.Commands/Password',
                request_serializer=Solicitudes__pb2.simple_Request.SerializeToString,
                response_deserializer=Solicitudes__pb2.Response2.FromString,
                )
        self.Create = channel.unary_unary(
                '/practica5.Commands/Create',
                request_serializer=Solicitudes__pb2.Request2.SerializeToString,
                response_deserializer=Solicitudes__pb2.Response.FromString,
                )
        self.Read = channel.unary_unary(
                '/practica5.Commands/Read',
                request_serializer=Solicitudes__pb2.Request2.SerializeToString,
                response_deserializer=Solicitudes__pb2.Response.FromString,
                )
        self.Write = channel.unary_unary(
                '/practica5.Commands/Write',
                request_serializer=Solicitudes__pb2.Request3.SerializeToString,
                response_deserializer=Solicitudes__pb2.Response.FromString,
                )
        self.Rename = channel.unary_unary(
                '/practica5.Commands/Rename',
                request_serializer=Solicitudes__pb2.Request3.SerializeToString,
                response_deserializer=Solicitudes__pb2.Response.FromString,
                )
        self.Remove = channel.unary_unary(
                '/practica5.Commands/Remove',
                request_serializer=Solicitudes__pb2.Request2.SerializeToString,
                response_deserializer=Solicitudes__pb2.Response.FromString,
                )
        self.MkDir = channel.unary_unary(
                '/practica5.Commands/MkDir',
                request_serializer=Solicitudes__pb2.Request2.SerializeToString,
                response_deserializer=Solicitudes__pb2.Response.FromString,
                )
        self.RmDir = channel.unary_unary(
                '/practica5.Commands/RmDir',
                request_serializer=Solicitudes__pb2.Request2.SerializeToString,
                response_deserializer=Solicitudes__pb2.Response.FromString,
                )
        self.ReadDir = channel.unary_stream(
                '/practica5.Commands/ReadDir',
                request_serializer=Solicitudes__pb2.Request.SerializeToString,
                response_deserializer=Solicitudes__pb2.Response.FromString,
                )
        self.CD = channel.unary_unary(
                '/practica5.Commands/CD',
                request_serializer=Solicitudes__pb2.Request.SerializeToString,
                response_deserializer=Solicitudes__pb2.Response.FromString,
                )


class CommandsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def User(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Password(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Write(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Rename(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Remove(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MkDir(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RmDir(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadDir(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CD(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CommandsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'User': grpc.unary_unary_rpc_method_handler(
                    servicer.User,
                    request_deserializer=Solicitudes__pb2.simple_Request.FromString,
                    response_serializer=Solicitudes__pb2.Response.SerializeToString,
            ),
            'Password': grpc.unary_unary_rpc_method_handler(
                    servicer.Password,
                    request_deserializer=Solicitudes__pb2.simple_Request.FromString,
                    response_serializer=Solicitudes__pb2.Response2.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=Solicitudes__pb2.Request2.FromString,
                    response_serializer=Solicitudes__pb2.Response.SerializeToString,
            ),
            'Read': grpc.unary_unary_rpc_method_handler(
                    servicer.Read,
                    request_deserializer=Solicitudes__pb2.Request2.FromString,
                    response_serializer=Solicitudes__pb2.Response.SerializeToString,
            ),
            'Write': grpc.unary_unary_rpc_method_handler(
                    servicer.Write,
                    request_deserializer=Solicitudes__pb2.Request3.FromString,
                    response_serializer=Solicitudes__pb2.Response.SerializeToString,
            ),
            'Rename': grpc.unary_unary_rpc_method_handler(
                    servicer.Rename,
                    request_deserializer=Solicitudes__pb2.Request3.FromString,
                    response_serializer=Solicitudes__pb2.Response.SerializeToString,
            ),
            'Remove': grpc.unary_unary_rpc_method_handler(
                    servicer.Remove,
                    request_deserializer=Solicitudes__pb2.Request2.FromString,
                    response_serializer=Solicitudes__pb2.Response.SerializeToString,
            ),
            'MkDir': grpc.unary_unary_rpc_method_handler(
                    servicer.MkDir,
                    request_deserializer=Solicitudes__pb2.Request2.FromString,
                    response_serializer=Solicitudes__pb2.Response.SerializeToString,
            ),
            'RmDir': grpc.unary_unary_rpc_method_handler(
                    servicer.RmDir,
                    request_deserializer=Solicitudes__pb2.Request2.FromString,
                    response_serializer=Solicitudes__pb2.Response.SerializeToString,
            ),
            'ReadDir': grpc.unary_stream_rpc_method_handler(
                    servicer.ReadDir,
                    request_deserializer=Solicitudes__pb2.Request.FromString,
                    response_serializer=Solicitudes__pb2.Response.SerializeToString,
            ),
            'CD': grpc.unary_unary_rpc_method_handler(
                    servicer.CD,
                    request_deserializer=Solicitudes__pb2.Request.FromString,
                    response_serializer=Solicitudes__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'practica5.Commands', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Commands(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def User(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/practica5.Commands/User',
            Solicitudes__pb2.simple_Request.SerializeToString,
            Solicitudes__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Password(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/practica5.Commands/Password',
            Solicitudes__pb2.simple_Request.SerializeToString,
            Solicitudes__pb2.Response2.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/practica5.Commands/Create',
            Solicitudes__pb2.Request2.SerializeToString,
            Solicitudes__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/practica5.Commands/Read',
            Solicitudes__pb2.Request2.SerializeToString,
            Solicitudes__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Write(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/practica5.Commands/Write',
            Solicitudes__pb2.Request3.SerializeToString,
            Solicitudes__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Rename(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/practica5.Commands/Rename',
            Solicitudes__pb2.Request3.SerializeToString,
            Solicitudes__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Remove(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/practica5.Commands/Remove',
            Solicitudes__pb2.Request2.SerializeToString,
            Solicitudes__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MkDir(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/practica5.Commands/MkDir',
            Solicitudes__pb2.Request2.SerializeToString,
            Solicitudes__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RmDir(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/practica5.Commands/RmDir',
            Solicitudes__pb2.Request2.SerializeToString,
            Solicitudes__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadDir(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/practica5.Commands/ReadDir',
            Solicitudes__pb2.Request.SerializeToString,
            Solicitudes__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CD(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/practica5.Commands/CD',
            Solicitudes__pb2.Request.SerializeToString,
            Solicitudes__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)