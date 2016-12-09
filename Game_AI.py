import random
class Game_Ai(object):
    def __init__(self):
        pass
    def random_ai(self, lst):
        while True:
            num = random.choice(lst) #choose number from avaiable moves list
            if type(num) == int:
                return num #return the number 
                break #end the loop