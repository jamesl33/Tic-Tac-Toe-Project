import pygame
pygame.init()

class Functions:
        def __init__(self, gameState):
                """Instantiation function initialises all of the variables needed for the functionality of the game.
                This include a gameState argument which is passed in the Main classes instantiation when an instance of this object
                is created."""
                self.bool_turn = True
                self.game_state = gameState
                self.isRunning = True
                self.move_count = 0

        def take_turn(self, n, multiplayerTurn=None):
                """This function handles the logic behind taking a move in the game. It will only allow the player to make a turn
                if several conditions are met. These conditions include not having a players move already in that position and it also being 
                that players turn."""
                if multiplayerTurn == None:
                        if self.bool_turn == True:
                                player = "X"
                        else:
                                player = "O"
                else:
                        player = multiplayerTurn

                for num in range(1,10):
                        if num == n:
                                if type(self.game_state[num - 1]) == int and self.isRunning == True and self.move_count < 9:
                                        self.game_state[num - 1] = player
                                        self.bool_turn = not self.bool_turn
                                        self.move_count += 1
                                        return True

        def placement_grid(self, x, y):
                """Function which takes an two arguments x,y these will be processed and then the function will return a value from
                1, 9 This references where on the board the person clicked."""
                if x > 50 and x < 350:
                        if y > 50 and y < 350:
                                if x >= 50 and x < 150:
                                        if y >= 50 and y < 150:
                                                return(1)
                                        elif y >= 150 and y < 250:
                                                return(4)
                                        elif y >= 250 and y <= 350:
                                                return(7)
                                elif x >= 150 and x < 250:
                                        if y >= 50 and y < 150:
                                                return(2)
                                        elif y >= 150 and y < 250:
                                                return(5)
                                        elif y >= 250 and y <= 350:
                                                return(8)
                                elif x >= 250 and x <= 350:
                                        if y >= 50 and y < 150:
                                                return(3)
                                        elif y >= 150 and y < 250:
                                                return(6)
                                        elif y >= 250 and y <= 350:
                                                return(9)

        def reset_game(self, x, y):
                """Method which will reset the game to the state that it was in when the game was first started."""
                if x > 230 and x < 380:
                        if y > 370 and y < 415:
                                self.bool_turn = True
                                self.game_state = [1,2,3,4,5,6,7,8,9]
                                self.isRunning = True
                                self.move_count = 0
                                return True
