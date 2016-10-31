import pygame
import random
class TicTacToe(object):
        def __init__(self):
                pygame.init()
                self.turn = True
                self.count = 1
                self.white = [255,255,255]
                self.black = [000,000,000]
                self.gameState = [1,2,3,4,5,6,7,8,9]
                self.screen = pygame.display.set_mode((600,1000))
                self.screen.fill(self.white)
                self.font = pygame.font.SysFont("monospace", 300)
                self.font2 = pygame.font.SysFont("monospace", 40)
                self.draw_grid()
                self.main_loop()
        """Mainloop that handles running the game.This function calls
        the other function when needed.When this loop ends the game 
        has ended."""
        def main_loop(self):
                running = True
                while running:
                        if self.turn == False:
                                self.random_ai()
                                self.reset_game(x,y)
                        pygame.display.update()
                        for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONUP:
                                        x,y = event.pos
                                        self.placement_grid(x,y)
                                        self.reset_game(x,y)
                                elif event.type == pygame.QUIT:
                                        running = False
        """draw grid function which is were each of the lines used to make the grid are
        declared and drawn. Each line has a beggining and end point and width.
        "pygame.draw.line("Display",(Color),(X,Y),(X,Y),(With Value))" This is an example 
        of how the pygame.draw.function is used."""
        def draw_grid(self):
                pygame.draw.line(self.screen,(self.black),(200,0),(200,600), (5))
                pygame.draw.line(self.screen,(self.black),(400,0),(400,600), (5))
                pygame.draw.line(self.screen,(self.black),(0,200),(600,200), (5))
                pygame.draw.line(self.screen,(self.black),(0,400),(600,400), (5))
                pygame.draw.line(self.screen,(self.black),(0,0),(0,600), (5))
                pygame.draw.line(self.screen,(self.black),(0,0),(600,0), (5))
                pygame.draw.line(self.screen,(self.black),(600,0),(600,600), (5))
                pygame.draw.line(self.screen,(self.black),(0,600),(600,600), (5))
                pygame.draw.line(self.screen,(self.black),(400,620),(400,670), (1))
                pygame.draw.line(self.screen,(self.black),(400,670),(600,670), (1))
                pygame.draw.line(self.screen,(self.black),(400,620),(600,620), (1))
                label = self.font2.render(("Reset Game"), 1, self.black)
                self.screen.blit(label,(420, 632))
        """Reset game function. This function resets all of the values back to the same
        values that the game has when it is first initialised. This function also redraws
        the grid and buttons."""
        def reset_game(self, x, y):
                if x <= 600 and x > 400:
                        if y <= 670 and y > 620:
                                self.gameState = [1,2,3,4,5,6,7,8,9]
                                self.turn = True
                                self.screen.fill(self.white)
                                self.draw_grid()
        """This function checks the current "gameState" to see if there has been a winner. It does this
        by checking each direction on the board depending on the argument "n" N is the either "O" or "X"
        """
        def check_for_win(self, n):
                if self.gameState[0] == n and self.gameState[1] == n and self.gameState[2] == n:
                        self.win(n)
                elif self.gameState[3] == n and self.gameState[4] == n and self.gameState[5] == n:
                        self.win(n)
                elif self.gameState[6] == n and self.gameState[7] == n and self.gameState[8] == n:
                        self.win(n)
                elif self.gameState[0] == n and self.gameState[4] == n and self.gameState[8] == n:
                        self.win(n)
                elif self.gameState[0] == n and self.gameState[3] == n and self.gameState[6] == n:
                        self.win(n)
                elif self.gameState[1] == n and self.gameState[4] == n and self.gameState[7] == n:
                        self.win(n)
                elif self.gameState[2] == n and self.gameState[5] == n and self.gameState[8] == n:
                        self.win(n)
                elif self.gameState[2] == n and self.gameState[4] == n and self.gameState[6] == n:
                        self.win(n)
        """Placement grid function determine where the "O" or "X" should be drawn on the screen
        this is done by comparing the "X" and "Y" values"""
        def placement_grid(self, x, y):
                if x <= 200:
                        if y < 200:
                                self.place_counter(25, 12, 1)
                        elif y >= 200 and y < 400:
                                self.place_counter(25, 212, 4)
                        elif y >= 400 and y <= 600:
                                self.place_counter(25, 412, 7)
                elif x > 200 and x <= 400:
                        if y < 200:
                                self.place_counter(225, 12, 2)
                        elif y >= 200 and y < 400:
                                self.place_counter(225, 212, 5)
                        elif y >= 400 and y <= 600:
                                self.place_counter(225, 412, 8)
                elif x > 400 and x <= 600:
                        if y < 200:
                                self.place_counter(425, 12, 3)
                        elif y >= 200 and y < 400:
                                self.place_counter(425, 212, 6)
                        elif y >= 400 and y <= 600:
                                self.place_counter(425, 412, 9)
        """This function handles the blitting of the "X" or "O" on the board. This is done
        by blitting the label to the grid at the "x" and "y" coords give by the arguments "x" and 
        "y"."""
        def place_counter(self, x, y, n):
                count =+ 1
                if self.turn == True:
                        for value in self.gameState:
                                if value == n and type(value) == int:
                                        label = self.font.render("X", 1, self.black)
                                        self.screen.blit(label, (x+2, y))
                                        self.gameState[value-1] = "X"
                                        self.check_for_win("X")
                                        self.turn = not self.turn
                else:
                        for value in self.gameState:
                                if value == n and type(value) == int:
                                        label = self.font.render("O", 1, self.black)
                                        self.screen.blit(label, (x-6, y))
                                        self.gameState[value-1] = "O"
                                        self.check_for_win("O")
                                        self.turn = not self.turn
        def win(self, n):
                label = self.font2.render((n + " Wins"), 1, self.black)
                self.screen.blit(label,(5, 620))
                self.gameState = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]

        def random_ai(self):
                randomX = random.randint(1, 600)
                randomY = random.randint(1, 600)
                self.placement_grid(randomX, randomY)
game = TicTacToe()
