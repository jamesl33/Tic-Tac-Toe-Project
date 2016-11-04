import random
class ai(object):
	def __init__(self, game):
		if game.ai_mode == "easy":
			self.random_ai(game)
	def random_ai(self, game):
		randomX = random.randint(1,3)
		randomY = random.randint(1,3)
		randomX = randomX * 100
		randomY = randomY * 100
		for index in game.ai_turns:
			if index == [randomX,randomY]:
				game.ai_turns.remove(index)
				game.placement_grid(randomX,randomY)






	
