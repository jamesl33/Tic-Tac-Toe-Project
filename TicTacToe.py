import pygame 
import ai
class TicTacToe(object):
	def __init__(self):
		pygame.init()
		self.gameState = True
		self.available_turns = [1,2,3,4,5,6,7,8,9]
		self.ai_mode = "easy"
		self.bool_turn = True
		self.count = 0
		self.white = [255,255,255]
		self.black = [000,000,000]
		self.screen = pygame.display.set_mode((400,600))
		self.screen.fill(self.white)
		self.font = pygame.font.SysFont("monospace", 80)
		self.font2 = pygame.font.SysFont("monospace", 25)
		self.main_loop()

	def main_loop(self):
		running = True
		while running:
			self.draw_grid()
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONUP:
					x,y = event.pos
					if self.gameState == True:
						self.placement_grid(x,y)
						if self.count < 8:
							self.take_turn(ai.ai.random_ai(self))
					if x <= 380 and x > 230:
						if y <= 415 and y > 370:
							self.reset_game()
				elif event.type == pygame.QUIT:
					pygame.display.quit()
					pygame.quit()
					running = False

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
						self.take_turn( 6)
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
		self.available_turns = [1,2,3,4,5,6,7,8,9]
		self.count = 0
		self.bool_turn = True
		self.gameState = True
		self.screen.fill(self.white)
		self.draw_grid()

	def take_turn(self, n):
		if self.bool_turn == True:
			turn = "X"
		else:
			turn = "O"
		
		if self.count == 9:
			self.win("none")
		
		if type(self.available_turns[n-1]) == int:
			if n == 1:
				label = self.font.render(turn, 1, self.black)
				self.screen.blit(label, (75, 55))
			elif n == 2:
				label = self.font.render(turn, 1, self.black)
				self.screen.blit(label, (175, 55))
			elif n == 3:
				label = self.font.render(turn, 1, self.black)
				self.screen.blit(label, (275, 55))
			elif n == 4:
				label = self.font.render(turn, 1, self.black)
				self.screen.blit(label, (75, 155))
			elif n == 5:
				label = self.font.render(turn, 1, self.black)
				self.screen.blit(label, (175, 155))
			elif n == 6:
				label = self.font.render(turn, 1, self.black)
				self.screen.blit(label, (275, 155))
			elif n == 7:
				label = self.font.render(turn, 1, self.black)
				self.screen.blit(label, (75, 255))
			elif n == 8:
				label = self.font.render(turn, 1, self.black)
				self.screen.blit(label, (175, 255))
			elif n == 9:
				label = self.font.render(turn, 1, self.black)
				self.screen.blit(label, (275, 255))
			self.available_turns[n-1] = turn
			print(self.available_turns)
			self.check_for_win(turn)
			self.bool_turn = not self.bool_turn
			self.count += 1

		elif type(self.available_turns[n-1]) == str:
			self.take_turn(ai.ai.random_ai(self))

	def win(self, n):
		if n == "none":
			label = self.font2.render(("No Winner"), 1, self.black)
		else:
			label = self.font2.render((n + " Wins"), 1, self.black)
		
		self.screen.blit(label,(50, 380))
		self.gameState = False

if __name__ == "__main__":
	game = TicTacToe()	