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
		print("Client poll")
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

	def RunClient(self):
		try:
			self.connect()
			print("Client Connected")
			try:
				while True:
					self.poll()
				# if len(serverMessage) != 0:
				# 	self.send_message(serverMessage)

			except KeyboardInterrupt:
				pass

			finally:
				print("Shutdown")
				self.shutdown()
		finally:
			pass