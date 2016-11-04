import random
class ai(object):
	def __init__(self, game):
		if game.ai_mode == "easy":
			self.random_ai(game)
	def random_ai(self, game):
		randomX = random.randint(1,3)
		randomY = random.randint(1,3)
		randomX = (randomX *2 ) * 100
		randomY = (randomY * 2) * 100
		game.placement_grid(randomX,randomY)
			# for num in game.gameState:
			# 	if type(num) == str:
			# 		pass
			# 	else:
			# 		game.available_moves.append(num)
			# print(game.gameState)
			# randomNum = random.randint(1, len(game.available_moves))
			# number = game.available_moves[randomNum]

			# if number == 1:
			# 	game.place_counter(75, 55, 1)
			# elif number == 2:
			# 	game.place_counter(175, 55, 2)
			# elif number == 3:
			# 	game.place_counter(275, 55, 3)
			# elif number == 4:
			# 	game.place_counter(75, 155, 4)
			# elif number == 5:
			# 	game.place_counter(175, 155, 5)
			# elif number == 6:
			# 	game.place_counter(275, 155, 6)
			# elif number == 7:
			# 	game.place_counter(75, 255, 7)
			# elif number == 8:
			# 	game.place_counter(175, 255, 8)
			# elif number == 9:
			# 	game.place_counter(275, 255, 9)