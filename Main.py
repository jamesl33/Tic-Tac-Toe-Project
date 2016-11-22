import Game_Functions
import Game_AI
import pygame
#import Server
pygame.init()
class Game_Window:
		def __init__(self):
				pygame.display.set_caption("Tic Tac Toe")
				self.display = pygame.display.set_mode((400, 600))
				self.functions = Game_Functions.Functions([1,2,3,4,5,6,7,8,9])
				self.ai = Game_AI.Game_Ai()
				self.font = pygame.font.SysFont("monospace", 80)
				self.font2 = pygame.font.SysFont("Verdana", 20)
				self.font3 = pygame.font.SysFont("Verdana", 35)
				self.font4 = pygame.font.SysFont("Verdana", 25)

		def play_game(self):
				self.display.fill([255,255,255])
				self.draw_grid()
				pygame.display.update()
				while True:
					x,y = self.event_checker()
					if x >= 50 and x <= 150:
						if y >= 500 and y <= 550:
							self.main_menu()
							break
					if self.functions.take_turn(self.functions.placement_grid(x,y)) == True and self.functions.isRunning == True:
						if self.ai.mode == "computer":
							if self.ai.ai_diff == "easy":
								self.functions.take_turn(self.ai.random_ai(self.functions.game_state))
					if self.functions.reset_game(x,y) == True:
						self.display.fill([255,255,255])
						self.draw_grid()
					self.update_display()
					pygame.display.update()
		
		def event_checker(self):
				while True:
						for event in pygame.event.get():
								if event.type == pygame.MOUSEBUTTONUP:
										x,y = event.pos
										return(x,y)
								elif event.type == pygame.QUIT:
										pygame.display.quit()
										pygame.quit()
										break

		def main_menu(self):
				self.draw_menu()
				pygame.display.update()
				while True:
						x,y = self.event_checker()
						if x >= 100 and x <= 300:
								if y >= 200 and y <= 250:
										self.play_game()
										break
								elif y >= 300 and y <= 350:
										self.options()
										break
								elif y >= 400 and y <= 450:
										pygame.display.quit()
										pygame.quit()
										break

		def options(self):
				self.draw_options()
				mode_list = ["human","multiplayer","computer"]
				ai_diff_list = ["easy","hard"]
				while True:
						x,y = self.event_checker()
						if x >= 100 and x <= 300:
								if y >= 170 and y <= 320:
										self.ai.mode_i += 1
										if self.ai.mode_i == 3:
												self.ai.mode_i = 0
										self.ai.mode = mode_list[self.ai.mode_i]
										self.draw_options()

						if self.ai.mode == "computer":
								if x >= 100 and x <= 300:
										if y >= 400 and y <= 450:
												self.ai.ai_diff_i += 1
												if self.ai.ai_diff_i == 2:
														self.ai.ai_diff_i = 0
												self.ai.ai_diff = ai_diff_list[self.ai.ai_diff_i]
												self.draw_options()
										
						if x >= 50 and x <= 150:
								if y >= 500 and y <= 550:
										self.main_menu()
										break

		def draw_options(self):
				self.display.fill([255,255,255])
				exit_label = self.font4.render(("Back"), 1, [0,0,0])
				option1_label = self.font4.render(("Player"), 1, [0,0,0])
				option2_label = self.font4.render(("vs."), 1, [0,0,0])
				title_label = self.font3.render(("Options"), 1, [0,0,0])
				mode_label = self.font4.render(("Mode"), 1, [0,0,0])
				self.display.blit(title_label, (50,50))
				self.display.blit(mode_label, (165,140))
				self.display.blit(option1_label, (163,185))
				self.display.blit(option2_label, (185,225))
				self.display.blit(exit_label, (70,510))

				drawList = [[[0,0,0], (100, 170), (300, 170), (3)], [[0,0,0], (100, 170), (100, 320), (3)], [[0,0,0], (100, 320), (300, 320), (3)], [[0,0,0], (300, 170), (300, 320), (3)], [[0,0,0], (50, 500), (150, 500), (3)],
				[[0,0,0], (50, 500), (50, 550), (3)], [[0,0,0], (50, 550), (150, 550), (3)], [[0,0,0], (150, 500), (150, 550), (3)]]

				for num in range(0, 8):
					self.draw_line(drawList[num])

				if self.ai.mode == "human":
					option_local_label = self.font4.render(("Player (local)"), 1, [0,0,0])
					self.display.blit(option_local_label, (123,265))

				elif self.ai.mode == "multiplayer":
					option_mp_label = self.font4.render(("Player (online)"), 1, [0,0,0])
					self.display.blit(option_mp_label, (113,265))
						
				elif self.ai.mode == "computer":
						option3_label = self.font4.render(("Computer"), 1, [0,0,0])
						self.display.blit(option3_label, (140,265))
						diff_label = self.font4.render(("AI Difficulty"), 1, [0,0,0])
						self.display.blit(diff_label, (130,370))

						pygame.draw.line(self.display,([0,0,0]),(100,400),(300,400), (3))
						pygame.draw.line(self.display,([0,0,0]),(100,400),(100,450), (3))
						pygame.draw.line(self.display,([0,0,0]),(100,450),(300,450), (3))
						pygame.draw.line(self.display,([0,0,0]),(300,400),(300,450), (3))

						if self.ai.ai_diff == "easy":
								easy_ai_label = self.font4.render(("Easy"), 1, [0,0,0])
								self.display.blit(easy_ai_label, (170,410))

						if self.ai.ai_diff == "hard":
								hard_ai_label = self.font4.render(("Hard"), 1, [0,0,0])
								self.display.blit(hard_ai_label, (170,410))
				pygame.display.update()

		def update_display(self):
				"""Docstring Here"""
				lst = [(75, 55), (175, 55), (275, 55), (75, 155), (175, 155),\
				(275, 155), (75, 255), (175, 255), (275, 255)]

				for num in range(1,10):
						if self.functions.game_state[num - 1] == "X":
								label = self.font.render("X", 1, [0,0,0])
								self.display.blit(label, lst[num - 1])
								self.win_line("X")
						elif self.functions.game_state[num - 1] == "O":
								label = self.font.render("O", 1, [0,0,0])
								self.display.blit(label, lst[num - 1])
								self.win_line("O")

		def draw_menu(self):
				self.display.fill([255,255,255])

				title_label = self.font3.render(("Tic Tac Toe"), 1,([0,0,0]))
				play_label = self.font4.render(("Play the Game"), 1,([0,0,0]))
				options_label = self.font4.render(("Settings"), 1,([0,0,0]))
				exit_label = self.font4.render(("Quit Game"), 1,[0,0,0])
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

		def draw_line(self, position):
			pygame.draw.line(self.display, (position[0]), (position[1]), (position[2]), (position[3]))

		def draw_grid(self):
				"""Docstring Here"""
				drawList = [[[0,0,0], (50, 50), (350, 50), (5)], [[0,0,0], (50, 150), (350, 150), (5)], [[0,0,0], (50, 250), (350, 250), (5)], [[0,0,0], (50, 350), (350, 350), (5)], [[0,0,0], (50, 50), (50, 350), (5)],
				[[0,0,0], (150, 50), (150, 350), (5)], [[0,0,0], (250, 50), (250, 350), (5)], [[0,0,0], (350, 50), (350, 350), (5)], [[0,0,0], (230, 370), (380, 370), (1)], [[0,0,0], (230, 370), (230, 415), (1)],
				[[0,0,0], (230, 415), (380, 415), (1)], [[0,0,0], (380, 370), (380, 415), (1)], [[0,0,0], (50,500),(150,500), (3)], [[0,0,0], (50,500),(50,550), (3)], [[0,0,0], (50,550),(150,550), (3)],
				[[0,0,0], (150,500),(150,550), (3)]]

				for num in range(0, 16):
					self.draw_line(drawList[num])

				resetLabel = self.font4.render(("Reset Game"), 1, [0,0,0])    
				self.display.blit(resetLabel, (230, 380))
				exit_label = self.font4.render(("Back"), 1, [0,0,0])
				self.display.blit(exit_label, (70,510))

				pygame.display.update()

		def win_line(self, n):
				 if self.functions.game_state[0] == n and self.functions.game_state[1] == n and self.functions.game_state[2] == n:
						 self.functions.isRunning = False
						 pygame.draw.line(self.display, ([0,0,0]), (80, 100), (320,100), (5))
				 elif self.functions.game_state[3] == n and self.functions.game_state[4] == n and self.functions.game_state[5] == n:
						 self.functions.isRunning = False
						 pygame.draw.line(self.display, ([0,0,0]), (80, 200), (320, 200), (5))
				 elif self.functions.game_state[6] == n and self.functions.game_state[7] == n and self.functions.game_state[8] == n:
						 self.functions.isRunning = False
						 pygame.draw.line(self.display, ([0,0,0]), (80, 300), (320, 300), (5))
				 elif self.functions.game_state[0] == n and self.functions.game_state[4] == n and self.functions.game_state[8] == n:
						 self.functions.isRunning = False
						 pygame.draw.line(self.display, ([0,0,0]), (80, 80), (320, 320), (8)) 
				 elif self.functions.game_state[0] == n and self.functions.game_state[3] == n and self.functions.game_state[6] == n:
						 self.functions.isRunning = False
						 pygame.draw.line(self.display, ([0,0,0]), (100, 80), (100, 320), (5))
				 elif self.functions.game_state[1] == n and self.functions.game_state[4] == n and self.functions.game_state[7] == n:
						 self.functions.isRunning = False
						 pygame.draw.line(self.display, ([0,0,0]), (200, 80), (200, 320), (5))
				 elif self.functions.game_state[2] == n and self.functions.game_state[5] == n and self.functions.game_state[8] == n:
						 self.functions.isRunning = False
						 pygame.draw.line(self.display, ([0,0,0]), (300, 80), (300, 320), (5))
				 elif self.functions.game_state[2] == n and self.functions.game_state[4] == n and self.functions.game_state[6] == n:
						 self.functions.isRunning = False
						 pygame.draw.line(self.display, ([0,0,0]), (100, 300), (300, 100), (8))  

if __name__ == '__main__':
		app = Game_Window()
		app.main_menu()