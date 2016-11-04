import pygame
import ai
class TicTacToe(object):
    def __init__(self):
        pygame.init()
        self.ai_mode = "easy"
        self.inMenu = False
        self.turn = True
        self.count = 1
        self.white = [255,255,255]
        self.black = [000,000,000]
        self.gameState = [1,2,3,4,5,6,7,8,9]
        self.screen = pygame.display.set_mode((400,600))
        self.screen.fill(self.white)
        self.font = pygame.font.SysFont("monospace", 80)
        self.font2 = pygame.font.SysFont("monospace", 25)
        self.font3 = pygame.font.SysFont("monospace", 25)
        self.main_loop()
        """Mainloop that handles running the game.This function calls
        the other function when needed.When this loop ends the game 
        has ended."""

    def main_loop(self):
        running = True
        while running:
            if self.inMenu == True:
                self.draw_main_menu()
                pygame.display.update()
            else:
                self.draw_grid()
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        x,y = event.pos
                        self.placement_grid(x,y)
                        ai.ai(self)
                        self.reset_game(x,y)
                    elif event.type == pygame.QUIT:
                        pygame.display.quit()
                        pygame.quit()
                        running = False
        """draw grid function which is were each of the lines used to make the grid are
        declared and drawn. Each line has a beggining and end point and width.
        "pygame.draw.line("Display",(Color),(X,Y),(X,Y),(With Value))" This is an example 
        of how the pygame.draw.function is used."""

    def draw_grid(self):
        pygame.draw.line(self.screen,(self.black),(50,50),(350,50), (5))
        pygame.draw.line(self.screen,(self.black),(50,150),(350,150), (5))
        pygame.draw.line(self.screen,(self.black),(50,250),(350,250), (5))
        pygame.draw.line(self.screen,(self.black),(50,350),(350,350), (5))
        pygame.draw.line(self.screen,(self.black),(50,50),(50,350), (5))
        pygame.draw.line(self.screen,(self.black),(150,50),(150,350), (5))
        pygame.draw.line(self.screen,(self.black),(250,50),(250,350), (5))
        pygame.draw.line(self.screen,(self.black),(350,50),(350,350), (5))
        pygame.draw.line(self.screen,(self.black),(230,370),(380,370), (1))
        pygame.draw.line(self.screen,(self.black),(230,370),(230,415), (1))
        pygame.draw.line(self.screen,(self.black),(230,415),(380,415), (1))
        pygame.draw.line(self.screen,(self.black),(380,370),(380,415), (1))
        resetLabel = self.font2.render(("Reset Game"), 1, self.black)
        self.screen.blit(resetLabel,(230, 380))
        """This function will draw the main menu which allows the user to define which mode they would
        like to play. This includes choosing which Ai they would like to play against."""

    def draw_main_menu(self):
        label = self.font3.render("Main Menu", 1, self.black)
        self.screen.blit(label, (220, 50))

        """Reset game function. This function resets all of the values back to the same
        values that the game has when it is first initialised. This function also redraws
        the grid and buttons."""

    def reset_game(self, x, y):
        if x <= 380 and x > 230:
            if y <= 415 and y > 370:
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
        if x >= 50 and x < 150:
            if y >= 50 and y < 150:
                self.place_counter(75, 55, 1)
            elif y >= 150 and y < 250:
                self.place_counter(75, 155, 4)
            elif y >= 250 and y <= 350:
                self.place_counter(75, 255, 7)
        elif x >= 150 and x < 250:
            if y >= 50 and y < 150:
                self.place_counter(175, 55, 2)
            elif y >= 150 and y < 250:
                self.place_counter(175, 155, 5)
            elif y >= 250 and y <= 350:
                self.place_counter(175, 255, 8)
        elif x >= 250 and x <= 350:
            if y >= 50 and y < 150:
                self.place_counter(275, 55, 3)
            elif y >= 150 and y < 250:
                self.place_counter(275, 155, 6)
            elif y >= 250 and y <= 350:
                self.place_counter(275, 255, 9)
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
        self.screen.blit(label,(50, 380))
        self.gameState = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]
    



if __name__ == "__main__":
    game = TicTacToe()
