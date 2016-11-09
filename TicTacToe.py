import pygame
class TicTacToe(object):
    """Docstring Here"""
    def __init__(self):
        pygame.init()
        self.gameState = True
        self.available_turns = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
        self.ai_mode = "easy"
        self.bool_turn = True
        self.white = [255, 255, 255]
        self.black = [000, 000, 000]
        self.display = pygame.display.set_mode((400, 600))
        self.display.fill(self.white)
        self.font = pygame.font.SysFont("monospace", 80)
        self.font2 = pygame.font.SysFont("monospace", 25)
        self.main_loop()

    def main_loop(self):
        """Docstring Here"""
        self.draw_grid()
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    x, y = event.pos
                    if self.gameState == True:
                        self.placement_grid(x, y)
                        self.bool_turn = not self.bool_turn
                        self.update_board()
                        pygame.display.update()
                    if x <= 380 and x > 230:
                        if y <= 415 and y > 370:
                            self.reset_game()
                elif event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.QUIT()

    def draw_grid(self):
        """Docstring Here"""
        pygame.draw.line(self.display, (self.black), (50, 50), (350, 50), (5))
        pygame.draw.line(self.display, (self.black), (50, 150), (350, 150), (5))
        pygame.draw.line(self.display, (self.black), (50, 250), (350, 250), (5))
        pygame.draw.line(self.display, (self.black), (50, 350), (350, 350), (5))
        pygame.draw.line(self.display, (self.black), (50, 50), (50, 350), (5))
        pygame.draw.line(self.display, (self.black), (150, 50), (150, 350), (5))
        pygame.draw.line(self.display, (self.black), (250, 50), (250, 350), (5))
        pygame.draw.line(self.display, (self.black), (350, 50), (350, 350), (5))
        pygame.draw.line(self.display, (self.black), (230, 370), (380, 370), (1))
        pygame.draw.line(self.display, (self.black), (230, 370), (230, 415), (1))
        pygame.draw.line(self.display, (self.black), (230, 415), (380, 415), (1))
        pygame.draw.line(self.display, (self.black), (380, 370), (380, 415), (1))
        resetLabel = self.font2.render(("Reset Game"), 1, self.black)
        self.display.blit(resetLabel, (230, 380))

    def placement_grid(self, x, y):
        if x > 50 and x < 350:
            if y > 50 and y < 350:
                if x >= 50 and x < 150:
                    if y >= 50 and y < 150:
                        self.take_turn(1)
                    elif y >= 150 and y < 250:
                        self.take_turn(4)
                    elif y >= 250 and y <= 350:
                        self.take_turn(7)
                elif x >= 150 and x < 250:
                    if y >= 50 and y < 150:
                        self.take_turn(2)
                    elif y >= 150 and y < 250:
                        self.take_turn(5)
                    elif y >= 250 and y <= 350:
                        self.take_turn(8)
                elif x >= 250 and x <= 350:
                    if y >= 50 and y < 150:
                        self.take_turn(3)
                    elif y >= 150 and y < 250:
                        self.take_turn(6)
                    elif y >= 250 and y <= 350:
                        self.take_turn(9)

    def check_for_win(self, n):
         if self.available_turns[0] == n and self.available_turns[1] == n and self.available_turns[2] == n:
             self.win(n)
         elif self.available_turns[3] == n and self.available_turns[4] == n and self.available_turns[5] == n:
             self.win(n)
         elif self.available_turns[6] == n and self.available_turns[7] == n and self.available_turns[8] == n:
             self.win(n)
         elif self.available_turns[0] == n and self.available_turns[4] == n and self.available_turns[8] == n:
             self.win(n)
         elif self.available_turns[0] == n and self.available_turns[3] == n and self.available_turns[6] == n:
             self.win(n)
         elif self.available_turns[1] == n and self.available_turns[4] == n and self.available_turns[7] == n:
             self.win(n)
         elif self.available_turns[2] == n and self.available_turns[5] == n and self.available_turns[8] == n:
             self.win(n)
         elif self.available_turns[2] == n and self.available_turns[4] == n and self.available_turns[6] == n:
             self.win(n)

    def reset_game(self):
        self.available_turns = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
        self.bool_turn = True
        self.gameState = True
        self.display.fill(self.white)
        self.draw_grid()

    def take_turn(self, n):
        """Docstring Here"""
        if self.bool_turn == True:
            for num in range(1,10):
                if num == n:
                    self.available_turns[num - 1] = "X"
                    self.check_for_win("X")
        if self.bool_turn == False:
            for num in range(1,10):
                if num == n:
                    self.available_turns[num - 1] = "O"
                    self.check_for_win("O")
                    
    def update_board(self):
        """Docstring Here"""
        lst = [(75, 55), (175, 55), (275, 55), (75, 155), (175, 155),\
        (275, 155), (75, 255), (175, 255), (275, 255)]

        for num in range(1, 10):
            if self.available_turns[num - 1] == "X":
                label = self.font.render("X", 1, self.black)
                self.display.blit(label, lst[num - 1])
            elif self.available_turns[num - 1] == "O":
                label = self.font.render("O", 1, self.black)
                self.display.blit(label, lst[num - 1])

    def win(self, n):
        """Docstring Here"""
        label = self.font2.render((n + " Wins"), 1, self.black)
        self.display.blit(label, (50, 380))
        self.gameState = False

if __name__ == "__main__":
    game = TicTacToe()	