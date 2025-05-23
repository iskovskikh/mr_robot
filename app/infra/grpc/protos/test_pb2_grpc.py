# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import infra.grpc.protos.test_pb2 as test__pb2


class MyServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.my_remote_call_procedure = channel.unary_unary(
                '/MyService/my_remote_call_procedure',
                request_serializer=test__pb2.MyRequestSchema.SerializeToString,
                response_deserializer=test__pb2.MyResponseSchema.FromString,
                )


class MyServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def my_remote_call_procedure(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MyServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'my_remote_call_procedure': grpc.unary_unary_rpc_method_handler(
                    servicer.my_remote_call_procedure,
                    request_deserializer=test__pb2.MyRequestSchema.FromString,
                    response_serializer=test__pb2.MyResponseSchema.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MyService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MyService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def my_remote_call_procedure(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MyService/my_remote_call_procedure',
            test__pb2.MyRequestSchema.SerializeToString,
            test__pb2.MyResponseSchema.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
