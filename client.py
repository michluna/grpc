import grpc
import messaging_pb2
import messaging_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = messaging_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(messaging_pb2.HelloRequest(name='user'))
        print("Greeter client received: " + response.message)

if __name__ == '__main__':
    run()
