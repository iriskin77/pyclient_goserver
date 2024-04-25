package main

import "github.com/iriskin77/pyclient_goserver/server"

func main() {

	port := 38334

	application := server.New(port)

	application.MustRun()
}
