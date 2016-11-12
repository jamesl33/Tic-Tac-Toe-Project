import random
class Game_Ai(object):
    def __init__(self):
        pass
    def random_ai(self, lst):
        while True:
            num = random.choice(lst)
            if type(num) == int:
                return num 
                break
    def hardened_ai(self):
        pass