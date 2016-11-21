import socket, time
class Networking():
    """Init function for the networking object. This functions creates the server
    and binds it to the port 12345."""
    def __init__(self, port):
        self.current_connections = {}
        self.port = port
        self.server = socket.socket()
        self.uid = 0

        self.server.bind(("", self.port))
        self.server.listen(5)

    def port(self):
        return self.port

    def shutdown(self):
        for client, data in self.current_connections.items():
            data["socket"].close()
        self.server.shutdown(1)
        self.server.close()

    def number_of_clients(self):
        return len(self.current_connections)

    def send_move(self):
        pass

    def list_sockets():
        return [self.current_connections[i]["socket"] for i in self.current_connections]

    def poll(self):
        connections = self.list_sockets()
        read, write, error = select.select( connections+[self.__server], connections, connections, 0 )
        messages, connected, disconnected = [], [], []

        for connection in error:
            print("error", connection)

                

    if __name__ == "__main__":
        server = Networking()
        try:
            print("The server is running on port{}".format(server.port()))
        except KeyboardInterrupt:
            pass
    finally:
        print("Server is shutting down")
        server.shutdown