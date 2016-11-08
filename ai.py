import random
class ai(object):
	# def __init__(self, game):
	# 	if game.ai_mode == "easy":
			# self.random_ai(game)
	def random_ai(self):
		num = random.randint(1, 9)
		return num