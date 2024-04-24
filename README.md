

## Создание прото файлов

protoc -I proto proto/sso/*.proto --go_out=./gen/go --go_opt=paths=source_relative --go-grpc_out=./gen/go/ --go-grpc_opt=paths=source_relative

Где:

    -I proto - это папка, где находятся все прото файлы;
    proto/sso/sso.proto - путь до конкретного прото файла, который необходимо скомпилировать;
    --go_out=./gen/go - путь, куда будут сохраняться скомпилированные файлы;
    --go-grpc_out=./gen/go/ - путь, куда будет сохраняться go-grpc код;

python3 -m grpc_tools.protoc --python_out=. --grpc_python_out=. --pyi_out=. --proto_path=. ./protos/*.proto

python3 -m grpc_tools.protoc --python_out=./protos/gen_proto --grpc_python_out=./protos/gen_proto --pyi_out=. --proto_path=. ./protos/
proto/*.proto

protoc -I proto proto/*.proto --go_out=./gen_proto --go_opt=paths=source_relative --go-grpc_out=./gen_proto/ --go-grpc_opt=paths=source_relative