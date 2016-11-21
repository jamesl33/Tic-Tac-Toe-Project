import random
class Game_Ai(object):
    def __init__(self):
        self.mode = "human"
        self.ai_diff = "easy"
        self.mode_i = 0
        self.ai_diff_i = 0
    def random_ai(self, lst):
        while True:
            num = random.choice(lst)
            if type(num) == int:
                return num 
                break
    def hardened_ai(self):
        pass