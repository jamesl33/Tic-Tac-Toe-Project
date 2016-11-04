import random
class ai(object):
	def __init__(self, game):
		if game.ai_mode == "easy":
			self.random_ai(game)
	def random_ai(self, game):
			game.randomX = random.randint(1, 600)
			game.randomY = random.randint(1, 600)
			game.placement_grid(game.randomX,game.randomY)