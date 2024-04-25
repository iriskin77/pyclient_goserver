# Makefile
# "пропущен разделитель" - использовать tab

start-goserver:
	go go_server.cmd.main

start-pyserver: 
	python3	-m py_client.cmd.main

gen-pygrpc:
	python3 -m grpc_tools.protoc --python_out=./protos/gen_proto --grpc_python_out=./protos/gen_proto --pyi_out=. --proto_path=. ./protos/
	proto/*.proto

gen-gogrpc:
	protoc -I proto proto/*.proto --go_out=./gen_proto --go_opt=paths=source_relative --go-grpc_out=./gen_proto/ --go-grpc_opt=paths=source_relative




