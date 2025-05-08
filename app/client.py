import grpc

from  infra.grpc.protos.test_pb2 import MyRequestSchema, MyResponseSchema
import infra.grpc.protos.test_pb2_grpc


def main():
    channel = grpc.insecure_channel('localhost:50051')
    stub = infra.grpc.protos.test_pb2_grpc.MyServiceStub(channel)

    response: MyResponseSchema = stub.my_remote_call_procedure(MyRequestSchema(name='123'))
    print(response.message)

if __name__ == '__main__':
    main()