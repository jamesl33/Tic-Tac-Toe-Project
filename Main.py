import Game_Functions
import Game_AI
import pygame

class Game_Window(object):
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((400, 600))
        self.functions = Game_Functions.Functions()
        self.ai = Game_AI.Game_Ai()
        self.ai_mode = "none"

    def run(self):
        self.display.fill([255,255,255])
        self.update_display()
        pygame.display.update()
        while True:
            self.draw_grid()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if self.functions.take_turn(self.functions.placement_grid(x,y)) == True:
                        if self.functions.bool_turn == False:
                            self.win("X")
                        else:
                            self.win("O")
                    if self.functions.move_count < 8:
                        if self.ai_mode == "easy":
                            self.functions.take_turn(self.ai.random_ai(self.functions.game_state))
                        elif self.ai_mode == "hard":
                            pass
                    if self.functions.reset_game(x,y) == True:
                        self.display.fill([255,255,255])
                        self.draw_grid()
                elif event.type == pygame.QUIT:
                    exit()
            self.update_display()
            pygame.display.update()

    def update_display(self):
        """Docstring Here"""
        font = pygame.font.SysFont("monospace", 80)

        lst = [(75, 55), (175, 55), (275, 55), (75, 155), (175, 155),\
        (275, 155), (75, 255), (175, 255), (275, 255)]

        for num in range(1,10):
            if self.functions.game_state[num - 1] == "X":
                label = font.render("X", 1, [0,0,0])
                self.display.blit(label, lst[num - 1])
            elif self.functions.game_state[num - 1] == "O":
                label = font.render("O", 1, [0,0,0])
                self.display.blit(label, lst[num - 1])

    def draw_grid(self):
        """Docstring Here"""
        font = pygame.font.SysFont("monospace", 25)
        pygame.draw.line(self.display, ([0,0,0]), (50, 50), (350, 50), (5))
        pygame.draw.line(self.display, ([0,0,0]), (50, 150), (350, 150), (5))
        pygame.draw.line(self.display, ([0,0,0]), (50, 250), (350, 250), (5))
        pygame.draw.line(self.display, ([0,0,0]), (50, 350), (350, 350), (5))
        pygame.draw.line(self.display, ([0,0,0]), (50, 50), (50, 350), (5))
        pygame.draw.line(self.display, ([0,0,0]), (150, 50), (150, 350), (5))
        pygame.draw.line(self.display, ([0,0,0]), (250, 50), (250, 350), (5))
        pygame.draw.line(self.display, ([0,0,0]), (350, 50), (350, 350), (5))

        pygame.draw.line(self.display, ([0,0,0]), (230, 370), (380, 370), (1))
        pygame.draw.line(self.display, ([0,0,0]), (230, 370), (230, 415), (1))
        pygame.draw.line(self.display, ([0,0,0]), (230, 415), (380, 415), (1))
        pygame.draw.line(self.display, ([0,0,0]), (380, 370), (380, 415), (1))
        resetLabel = font.render(("Reset Game"), 1, [0,0,0])
        self.display.blit(resetLabel, (230, 380))

    def win(self, n):
        """Docstring Here"""
        font = pygame.font.SysFont("monospace", 25)
        label = font.render((n + " Wins"), 1, [0,0,0])
        self.display.blit(label, (50, 380))

if __name__ == '__main__':
	app = Game_Window()
	app.run()