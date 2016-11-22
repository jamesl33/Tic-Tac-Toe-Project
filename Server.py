import socket, pickle, sys, time

class Server:
	def __init__(self):
		self.clientList = []
		self.socketList = []

		self.create_server("", 12345)
		self.start_server()

	def create_server(self, ip, port):
		self.server = socket.socket()
		self.server.bind((ip, port))
		self.server.listen(1)

	# def send_message(self, message, user=None):
	# 	data = pickle.loads(message)
	# 	if user == None:
	# 		for client in self.socketList:
	# 			self.server.send(data)
	# 	elif client in self.socketList:
	# 		pass

	def start_server(self):
		while len(self.clientList) != 1:
			print("waiting for one or more connections")
			(csocket, caddress) = self.server.accept()
			self.clientList.append(caddress)
			self.socketList.append(csocket)
		else:
			print("Two people have now connected")
			try:
				while True:
					for client in self.socketList:
						data = client.recv(2048)
						data = pickle.loads(data)
						print(data)
				time.sleep(2)
			except EOFError:
				pass

	def close_server(self):
		self.server.shutdown(1)
		self.server.close()

server = Server()