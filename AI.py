import random

class Game_Ai(object):
        def __init__(self, game):
                self.usedNumbers = {1: [], 2: [], 3: [], 4: [], 5:[], 6: [], 7: [], 8: [], 9: []}
                if game.ai_mode == "easy":
                        self.Easy_AI(game)
        def Easy_AI(self, game):
                if game.turn == False:
                        randomX = random.randint(1, 3)
                        randomY = random.randint(1, 3)
                        randomX = (randomX * 2) * 100
                        randomY = (randomY * 2) * 100
                        game.placement_grid(randomX, randomY)















              

