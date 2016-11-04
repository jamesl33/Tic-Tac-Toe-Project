import random
class ai(object):
	def __init__(self, game):
		if game.ai_mode == "easy":
			self.random_ai(game)
	def random_ai(self, game):
			game.randomX = random.randint(50, 350)
			game.randomY = random.randint(50, 350)
			game.placement_grid(game.randomX,game.randomY)
