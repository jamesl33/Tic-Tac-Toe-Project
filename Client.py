import socket, pickle, time

class Client:
	def __init__(self):
		self.server = socket.socket()
		self.server.connect(("127.0.0.1", 12345))

	def send_message(self, message):
		data = pickle.dumps(message)
		self.server.send(data)

user = Client()

while True:
	user.send_message("Hello")
	time.sleep(1)

