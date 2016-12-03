import socket, select, pickle, time, Game_Functions

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
		self.functions = Game_Functions.Functions([1,2,3,4,5,6,7,8,9])
		self.server = socket.socket()
		self.server.bind(("", port))
		self.server.listen(2)
		self.turn = True

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

	def take_turn(self, msg):
		pos = msg[1]
		x = pos[0]
		y = pos[1]
		if x > 230 and x < 380:
				if y > 370 and y < 415:
					print("Reset")
		elif x > 50 and x < 350:
			if y > 50 and y < 350:
				if msg[0] == True and self.turn == True:
					print("X Turn")
					self.turn = not self.turn
					msgbytes = pickle.dumps(["Draw", "X", self.functions.placement_grid(x,y)])
					for connection in self.current_connections:
						connection.send(msgbytes)
				elif msg[0] == False and self.turn == False:
					print("O Turn")
					self.turn = not self.turn
					msgbytes = pickle.dumps(["Draw", "O", self.functions.placement_grid(x,y)])
					for connection in self.current_connections:
						connection.send(msgbytes)
				elif msg[0] == "Reset":
					pass
				elif msg[0] == "Message":
					pass

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
					msg = unpickle_message(msgbytes)
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
		server.send_message("brekfast")
		while True:
			server.poll()

	except KeyboardInterrupt:
		pass

	finally:
		print("Shutdown")
		server.shutdown()
