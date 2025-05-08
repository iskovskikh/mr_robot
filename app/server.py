from concurrent.futures.thread import ThreadPoolExecutor

import grpc

from infra.grpc.protos.test_pb2_grpc import MyServiceStub, add_MyServiceServicer_to_server, MyServiceServicer

from infra.grpc.protos.test_pb2 import MyRequestSchema, MyResponseSchema



class My(MyServiceServicer):
    def my_remote_call_procedure(self, request: MyRequestSchema, context):
        return MyResponseSchema(message=f'Hello {request.name}!')


def serve():
    server = grpc.server(thread_pool=ThreadPoolExecutor(max_workers=4))
    add_MyServiceServicer_to_server(
        servicer=My(),
        server=server,
    )
    server.add_insecure_port('[::]:50051')
    server.start()
    print('server started!')
    server.wait_for_termination()

if __name__ == '__main__':
    serve()