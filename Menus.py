#Module in charge of drawing all the menus and other graphics
import pygame
pygame.init()

class user_interface:
    def __init__(self):
        """This function sets the default game mode of the game, as well as the different fonts used in it."""

        self.mode = "human"
        self.ai_diff = "easy"
        self.mode_i = 0
        self.ai_diff_i = 0
        self.font = pygame.font.SysFont("monospace", 80)
        self.font2 = pygame.font.SysFont("Verdana", 35)
        self.font3 = pygame.font.SysFont("Verdana", 25)

    def draw_menu(self, display):
        """Function in charge of drawing the main menu. The display input uses a value set in Main.py ( __init__ function) for creating the game window. To actually draw everything, a for loop and
            a list with all the values used to create lines is used to draw all the different lines that make up the "buttons" (The same is done in all other functions in this module)"""   

        self.display = display
        self.display.fill([255,255,255])
        title_label = self.font2.render(("Tic Tac Toe"), 1,([0,0,0]))
        play_label = self.font3.render(("Play the Game"), 1,([0,0,0]))
        options_label = self.font3.render(("Settings"), 1,([0,0,0]))
        exit_label = self.font3.render(("Quit Game"), 1,[0,0,0])
        self.display.blit(title_label, (110, 70))
        self.display.blit(play_label, (110,210))
        self.display.blit(options_label, (150,310))
        self.display.blit(exit_label, (140,410))

        drawList = [[[0,0,0], (100, 200), (300, 200), (3)], [[0,0,0], (100, 200), (100, 250), (3)], [[0,0,0], (100, 250), (300, 250), (3)], [[0,0,0], (300, 200), (300, 250), (3)], 
        [[0,0,0], (100, 300), (300, 300), (3)], [[0,0,0], (100, 300), (100, 350), (3)], [[0,0,0], (100, 350), (300, 350), (3)], [[0,0,0], (100, 350), (300, 350), (3)], [[0,0,0], (300, 300), (300, 350), (3)],
        [[0,0,0], (100, 400), (300, 400), (3)], [[0,0,0], (100, 400), (100, 450), (3)], [[0,0,0], (100, 450), (300, 450), (3)], [[0,0,0], (300, 400), (300, 450), (3)]]
                
        for num in range(0, 13):
            self.draw_line(drawList[num])
            pygame.display.update()

    def draw_options(self):
        """This function draws the options menu. The buttons change depending on the different game modes and AI difficulties."""
        
        self.display.fill([255,255,255])
        exit_label = self.font3.render(("Back"), 1, [0,0,0])
        option1_label = self.font3.render(("Player"), 1, [0,0,0])
        option2_label = self.font3.render(("vs."), 1, [0,0,0])
        title_label = self.font2.render(("Options"), 1, [0,0,0])
        mode_label = self.font3.render(("Mode"), 1, [0,0,0])
        self.display.blit(title_label, (50,50))
        self.display.blit(mode_label, (165,140))
        self.display.blit(option1_label, (163,185))
        self.display.blit(option2_label, (185,225))
        self.display.blit(exit_label, (70,510))

        drawList = [[[0,0,0], (100, 170), (300, 170), (3)], [[0,0,0], (100, 170), (100, 320), (3)], [[0,0,0], (100, 320), (300, 320), (3)], [[0,0,0], (300, 170), (300, 320), (3)], [[0,0,0], (50, 500), (150, 500), (3)],
                    [[0,0,0], (50, 500), (50, 550), (3)], [[0,0,0], (50, 550), (150, 550), (3)], [[0,0,0], (150, 500), (150, 550), (3)]]

        for num in range(0, 8):
            self.draw_line(drawList[num])

        if self.mode == "human":
            option_local_label = self.font3.render(("Player (local)"), 1, [0,0,0])
            self.display.blit(option_local_label, (123,265))

        elif self.mode == "multiplayer":
            option_mp_label = self.font3.render(("Player (online)"), 1, [0,0,0])
            self.display.blit(option_mp_label, (113,265))
                        
        elif self.mode == "computer":
            option3_label = self.font3.render(("Computer"), 1, [0,0,0])
            self.display.blit(option3_label, (140,265))
            diff_label = self.font3.render(("AI Difficulty"), 1, [0,0,0])
            self.display.blit(diff_label, (130,370))

            pygame.draw.line(self.display,([0,0,0]),(100,400),(300,400), (3))
            pygame.draw.line(self.display,([0,0,0]),(100,400),(100,450), (3))
            pygame.draw.line(self.display,([0,0,0]),(100,450),(300,450), (3))
            pygame.draw.line(self.display,([0,0,0]),(300,400),(300,450), (3))

            if self.ai_diff == "easy":
                easy_ai_label = self.font3.render(("Easy"), 1, [0,0,0])
                self.display.blit(easy_ai_label, (170,410))

            if self.ai_diff == "hard":
                hard_ai_label = self.font3.render(("Hard"), 1, [0,0,0])
                self.display.blit(hard_ai_label, (170,410))
        pygame.display.update()

    def draw_line(self, position):
        """Function that uses the values in the drawLists to draw the lines."""
        
        pygame.draw.line(self.display, (position[0]), (position[1]), (position[2]), (position[3]))

    def draw_grid(self):
        """Function that draws the game board."""
        
        drawList = [[[0,0,0], (50, 50), (350, 50), (5)], [[0,0,0], (50, 150), (350, 150), (5)], [[0,0,0], (50, 250), (350, 250), (5)], [[0,0,0], (50, 350), (350, 350), (5)], [[0,0,0], (50, 50), (50, 350), (5)],
        [[0,0,0], (150, 50), (150, 350), (5)], [[0,0,0], (250, 50), (250, 350), (5)], [[0,0,0], (350, 50), (350, 350), (5)], [[0,0,0], (230, 370), (380, 370), (1)], [[0,0,0], (230, 370), (230, 415), (1)],
        [[0,0,0], (230, 415), (380, 415), (1)], [[0,0,0], (380, 370), (380, 415), (1)], [[0,0,0], (50,500),(150,500), (3)], [[0,0,0], (50,500),(50,550), (3)], [[0,0,0], (50,550),(150,550), (3)],
        [[0,0,0], (150,500),(150,550), (3)]]

        for num in range(0, 16):
            self.draw_line(drawList[num])

            resetLabel = self.font3.render(("Reset Game"), 1, [0,0,0])    
            self.display.blit(resetLabel, (230, 380))
            exit_label = self.font3.render(("Back"), 1, [0,0,0])
            self.display.blit(exit_label, (70,510))

            pygame.display.update()
