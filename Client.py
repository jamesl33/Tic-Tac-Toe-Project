#Module in charge of handling all client related functions. (Inspired by David's code)
import socket, select, sys, time, pickle

def unpickle_message(msgbytes):
    """Function that turns messages sent from the server in bits into their original values, so as to maintain their data types"""
    return pickle.loads(msgbytes)

def pickle_message(message):
    """Function that turns data into bits to be able to send it over to the server and keep the data type information intact"""
    msgbytes = pickle.dumps(message)
    return (msgbytes)

class AlreadyConnected(Exception):
    pass

class NotConnected(Exception):
    pass

class Client:
    def __init__(self, host=None, port=12345):
        """Initalizes all the variables used in the rest of the module. (Setting host and port to default values if none are provided)."""
        if host == None:
            host = "127.0.0.1"
        self.__host = host
        self.__port = port
        self.client = None
        self.turn = None
        self.last_message = None        

    def connect(self):
        """Function in charge of connecting the client to the server."""
        if self.connected():
            raise AlreadyConnected()
        self.__sendBuffer = []
        self.__recvBuffer = ""

        self.client = socket.socket()
        self.client.connect((self.__host, self.__port))

    def connected(self):
        """Function that returns wether or not the client is already connected."""    
        return self.client != None

    def shutdown(self):
        """Function that shuts down the client and resets variables used by the client."""
        if not self.connected():
            return
        self.client.close()
        self.client = None
        self.__recvBuffer = ""

    def send_message(self, msg):
        """Function that receives an input, pickles that input and adds it to a buffer."""
        msgbytes = pickle.dumps(msg)
        self.__sendBuffer.append(msgbytes)

    def poll(self):
        """Function that handles receiving and sending messages to and from the client."""
        if not self.connected():
            raise NotConnected()

        read, write, error = select.select( [self.client], [self.client], [self.client], 0 )

        messages = []

        if error != []:
            pass

        try:
            if write != []:
                while len(self.__sendBuffer) != 0:
                    msg = self.__sendBuffer[0]

                    self.client.send(msg)
                    self.__sendBuffer.pop(0)

            if read != []:
                msgbytes = self.client.recv(2048)
                msg = unpickle_message(msgbytes)
                if msg == True or msg == False:
                    self.turn = msg
                else:
                    print(msg)
                    self.last_message = msg

                if not msgbytes:
                    print("Connection disconnected")

        except ConnectionResetError:
            self.shutdown()

    def RunClient(self):
        """Function in charge of connecting the client, while giving a message confirming it. (Mostly used for debugging)"""
        try:
            self.connect()
            print("Client Connected")
        except KeyboardInterrupt:
            pass
        finally:
            pass