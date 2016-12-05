import pygame, Menus, Game_Functions, Game_AI, Client
pygame.init()

class Main:
		def __init__(self):
				self.ai = Game_AI.Game_Ai()
				self.functions = Game_Functions.Functions([1,2,3,4,5,6,7,8,9])
				self.ui = Menus.user_interface()
				self.client = Client.Client()
				self.display = pygame.display.set_mode((400, 600))
				pygame.display.set_caption("Tic Tac Toe")
				self.display.fill([255,255,255])

		def event_checker(self):
			while True:
				self.update_display()
				try:
					for event in pygame.event.get():
						if event.type == pygame.MOUSEBUTTONUP:
						  x,y = event.pos
						  return(x,y)
						elif event.type == pygame.QUIT:
						  self.shutdown()
						  break
				except:
					pass

		def main_menu(self):
				self.ui.draw_menu(self.display)
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
							self.shutdown()
							break

		def options(self):
				self.ui.draw_options()
				mode_list = ["human","multiplayer","computer"]
				ai_diff_list = ["easy","hard"]
				while True:
						x,y = self.event_checker()
						if x >= 100 and x <= 300:
								if y >= 170 and y <= 320:
										self.ui.mode_i += 1
										if self.ui.mode_i == 3:
												self.ui.mode_i = 0
										self.ui.mode = mode_list[self.ui.mode_i]
										self.ui.draw_options()

						if self.ui.mode == "computer":
								if x >= 100 and x <= 300:
										if y >= 400 and y <= 450:
												self.ui.ai_diff_i += 1
												if self.ui.ai_diff_i == 2:
														self.ui.ai_diff_i = 0
												self.ui.ai_diff = ai_diff_list[self.ui.ai_diff_i]
												self.ui.draw_options()

						if self.ui.mode == "multiplayer":
							if self.client.connected() == True:
								pass
							else:
								self.client.RunClient()
								self.client.poll()
							  
						if x >= 50 and x <= 150:
								if y >= 500 and y <= 550:
										if self.ui.mode != "multiplayer":
											pass
										self.main_menu()
										break

		def play_game(self):
				self.display.fill([255,255,255])
				self.ui.draw_grid()
				pygame.display.update()
				while True:
						x,y = self.event_checker()
						if x >= 50 and x <= 150:
								if y >= 500 and y <= 550:
										self.main_menu()
										break

						if self.ui.mode == "multiplayer" and self.functions.isRunning == True:
							if x > 230 and x < 380:
									if y > 370 and y < 415:
										self.client.send_message(["Reset", (x,y)])
							self.client.send_message(([self.client.turn, (x,y)]))

						elif self.functions.take_turn(self.functions.placement_grid(x,y)) == True and self.functions.isRunning == True:
								if self.ui.mode == "computer":
										if self.ui.ai_diff == "easy":
												if self.functions.move_count < 8:
														self.functions.take_turn(self.ai.random_ai(self.functions.game_state))
												else:
														pass

						self.update_display()
						if self.functions.reset_game(x,y) == True:
								self.display.fill([255,255,255])
								self.ui.draw_grid()

		def update_display(self):
				if self.client.connected() == True:
					self.client.poll()
					if self.client.last_message == None:
						pass
					elif self.client.last_message[0] == "Draw":
						self.functions.take_turn(self.client.last_message[2], self.client.last_message[1])

				self.win_line()

				lst = [(75, 55), (175, 55), (275, 55), (75, 155), (175, 155),\
						   (275, 155), (75, 255), (175, 255), (275, 255)]

				for num in range(1,10):
						if self.functions.game_state[num - 1] == "X":
								label = self.ui.font.render("X", 1, [0,0,0])
								self.display.blit(label, lst[num - 1])
						elif self.functions.game_state[num - 1] == "O":
								label = self.ui.font.render("O", 1, [0,0,0])
								self.display.blit(label, lst[num - 1])
				pygame.display.update()

		def win_line(self):
			for n in ["X", "O"]:
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

			pygame.display.update()

		def shutdown(self):
			pygame.quit()
			pygame.display.quit()

if __name__ == '__main__':
	app = Main()
	app.main_menu()
