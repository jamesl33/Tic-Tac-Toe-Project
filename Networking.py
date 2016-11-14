import socket, time
class Networking(object):
    def __init__(self):
        self.socket = socket.socket()
        port = 12346
        self.socket.bind(("", port))
        self.socket.listen(5)
        print("Server is running on port {}".format(port))
        self.handle_connection()
    def handle_connection(self):
        try:
            while True:
                client, address = self.socket.accept()
                print("Got connection from", address)
                while True:
                    rawmsg = client.recv(1024)
                    message = rawmsg.decode('utf-8').rstrip('\r\n')
                    message = message + "\r\n"
                    client.send(message.encode("utf-8"))
                print("Disconnected")
                self.socket.close()
        except KeyboardInterrupt:
            pass
        finally:
            self.shutdown()
    def shutdown(self):
        print("shutting down the server")
        self.socket.shutdown(1)
        self.socket.close()

network = Networking()