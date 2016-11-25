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
		self.port = port

		self.server = socket.socket()
		self.server.bind(("", port))
		self.server.listen(2)

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

				print("Got connection from {}".format(address))

			else:
				msgbytes = connection.recv(1024)
				msgbytes = unpickle_message(msgbytes)
				print(msgbytes)
				if not msgbytes:
					print("Connection disconnected")

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
