import socket, select, pickle, time

def unpickle_message(msgbytes):
	return pickle.loads(msgbytes)


def pickle_message(message):
	msgbytes = pickle.dumps(message)
	return (msgbytes)


class Server:
	def __init__(self, port=12345):
		self.current_connections = []
		self.current_sockets = []
		self.sendBuffer = ""
		self.port = port

		self.server = socket.socket()
		self.server.bind(("", port))
		self.server.listen(2)

	def send_message(self, msg, client=None):
		msgbytes = pickle.dumps(msg)
		if client == None:
			for client in self.current_connections:
				client.send(msgbytes)
		else:
			print("Done know that client")

	def shutdown(self):
		for client in self.current_connections:
			client.close()

		self.server.shutdown(1)
		self.server.close()

	def poll(self):
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
					msgbytes = unpickle_message(msgbytes)
					print(msgbytes)
					if not msgbytes:
						print("Connection disconnected")

		for connection in write:
			if write != []:
				pass

if __name__ == "__main__":
	server = Server()

	try:
		print("Server is running on port {}".format(server.port))
		server.send_message("brekfast")
		while True:
			server.poll()
			time.sleep(1)

	except KeyboardInterrupt:
		pass

	finally:
		print("Shutdown")
		server.shutdown()
