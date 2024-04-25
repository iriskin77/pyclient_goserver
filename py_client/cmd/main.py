# import sys
# sys.path.append("home/abc/Рабочий стол/pyclient_goserver/py_client")

import grpc

from py_client.protos.gen_proto import hello_pb2
from py_client.protos.gen_proto import hello_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:38334") as channel:
        stub = hello_pb2_grpc.ServiceGreetingStub(channel)

        response = stub.SendGreeting(hello_pb2.SendGreetingRequest(greeting="John"))

    print(response)


run()
