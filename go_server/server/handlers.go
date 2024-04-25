package server

import (
	"context"
	"fmt"

	grpc_go "github.com/iriskin77/pyclient_goserver/protos/gen_proto"
	"google.golang.org/grpc"
)

type serverAPI struct {
	grpc_go.UnimplementedServiceGreetingServer
}

func Register(gRPC *grpc.Server, serv serverAPI) {
	grpc_go.RegisterServiceGreetingServer(gRPC, &serverAPI{})
}

func (s *serverAPI) SendGreeting(ctx context.Context, req *grpc_go.SendGreetingRequest) (*grpc_go.SendGreetingResponse, error) {
	return &grpc_go.SendGreetingResponse{Greeting: fmt.Sprintf("Hello, %s", req.Greeting)}, nil
}
