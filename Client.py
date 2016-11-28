import socket, select, sys, time, pickle

def unpickle_message(msgbytes):
	return pickle.loads(msgbytes)


def pickle_message(message):
	msgbytes = pickle.dumps(message)
	return (msgbytes)

class AlreadyConnected(Exception):
	pass

class NotConnected(Exception):
	pass

class Client:
	def __init__(self, host=None, port=12345):
		if host == None:
			host = "127.0.0.1"
		self.__host = host
		self.__port = port

		self.client = None
		self.connect()

	def connect(self):
		if self.connected():
			raise AlreadyConnected()
		self.__sendBuffer = []
		self.__recvBuffer = ""

		self.client = socket.socket()
		self.client.connect((self.__host, self.__port))

	def connected(self):
		return self.client != None

	def shutdown(self):
		if not self.connected():
			return
		self.client.close()
		self.client = None
		self.__recvBuffer = ""

	def send_message(self, msg):
		msgbytes = pickle.dumps(msg)
		self.__sendBuffer.append(msgbytes)

	def poll(self):
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
				msgbytes = unpickle_message(msgbytes)
				print(msgbytes)
				if not msgbytes:
					print("Connection disconnected")

		except ConnectionResetError:
			self.shutdown()

		return messages

if __name__ == "__main__":
	try:
		client = Client()

	except ConnectionRefusedError:
		print("Connection failed")
		sys.exit(1)

	try:
		print("Client connected")

		client.send_message([1,2,3,4,5,6,7,8,9])

		while True:
			messages = client.poll()

			for message in messages:
				print("Recieved \"{}\"".format(message))

	except (KeyboardInterrupt, NotConnected) as e:
		pass

	finally:
		print("Shutdown")
		client.shutdown()