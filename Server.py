#This modules holds all the methods and data to run a server for the game.(Inspired by David's code)
import socket, select, pickle, time, Game_Functions

class Server:
    def __init__(self, port=12345):
        """This sets the default values for the variables that are to be used by the server."""
                
        self.current_connections = []
        self.current_sockets = []
        self.sendBuffer = ""
        self.port = port
        self.functions = Game_Functions.Functions([1,2,3,4,5,6,7,8,9])
        self.server = socket.socket()
        self.server.bind(("", port))
        self.server.listen(2)
        self.turn = True

    def shutdown(self):
        """Function that closes all connections to any clients that are connected and then shuts down the server itself."""
        for client in self.current_connections:
            client.close()
        self.server.shutdown(1)
        self.server.close()

    def take_turn(self, msg):
        """Function that handles turn taking in multiplayer mode."""
        print(msg)
        pos = msg[1]
        x = pos[0]
        y = pos[1]
        if x > 230 and x < 380:
                if y > 370 and y < 415:
                    msgbytes = pickle.dumps(["Reset", (x,y)])
                    for connection in self.current_connections:
                        connection.send(msgbytes)
        if msg[0] == True and self.turn == True:
            msgbytes = pickle.dumps(["Draw", "X", self.functions.placement_grid(x,y)])
            self.turn = not self.turn
            for connection in self.current_connections:
                connection.send(msgbytes)
        elif msg[0] == False and self.turn == False:
            msgbytes = pickle.dumps(["Draw", "O", self.functions.placement_grid(x,y)])
            self.turn = not self.turn
            for connection in self.current_connections:
                connection.send(msgbytes)

    def poll(self):
        """Function that takes care of receiving and sending messages to and from the server"""
        read, write, error = select.select(self.current_connections+[self.server], self.current_connections, self.current_connections, 0)

        for connection in read:
            if connection is self.server:
                client, address = connection.accept()
                self.current_connections.append(client)
                turn = True
                if len(self.current_connections) == 2:
                    for client in self.current_connections:
                        msgbytes = pickle.dumps(turn)
                        client.send(msgbytes)
                        turn = not turn

                print("Got connection from {}".format(address))

            else:
                msgbytes = connection.recv(2048)
                if len(msgbytes) != 0:
                    msg = pickle.loads(msgbytes)
                    self.take_turn(msg)
                    if not msgbytes:
                        print("Connection disconnected")

        for connection in write:
            if write != []:
                pass

if __name__ == "__main__":
    server = Server()

    try:
        print("Server is running on port {}".format(server.port))
        while True:
            server.poll()

    except KeyboardInterrupt:
        pass

    finally:
        print("Shutdown")
        server.shutdown()
