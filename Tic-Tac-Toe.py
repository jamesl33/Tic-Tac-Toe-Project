import pygame
import ai
import math
class TicTacToe(object):
	def __init__(self):
		pygame.init()
		self.ai_turns = [[100,100], [100,200], [100,300], [200,100], [200,200], [200,300], [300,100], [300,200], [300,300]]
		self.ai_mode = "easy"
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

	def main_loop(self):
		running = True
		while running:
			self.draw_grid()
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONUP:
					x,y = event.pos
					self.placement_grid(x,y)
					# ai.ai(self)
					self.reset_game(x,y)
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
						self.take_turn(75, 55, 1)
					elif y >= 150 and y < 250:
						self.take_turn(75, 155, 4)
					elif y >= 250 and y <= 350:
						self.take_turn(75, 255, 7)
				elif x >= 150 and x < 250:
					if y >= 50 and y < 150:
						self.take_turn(175, 55, 2)
					elif y >= 150 and y < 250:
						self.take_turn(175, 155, 5)
					elif y >= 250 and y <= 350:
						self.take_turn(175, 255, 8)
				elif x >= 250 and x <= 350:
					if y >= 50 and y < 150:
						self.take_turn(275, 55, 3)
					elif y >= 150 and y < 250:
						self.take_turn(275, 155, 6)
					elif y >= 250 and y <= 350:
						self.take_turn(275, 255, 9)
		print(x)
		print(y)
		for index in self.ai_turns:
			print(index)
			if index == [x,y]:
				self.ai_turns.remove(index)

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

	def reset_game(self, x, y):
		if x <= 380 and x > 230:
			if y <= 415 and y > 370:
				self.gameState = [1,2,3,4,5,6,7,8,9]
				self.turn = True
				self.screen.fill(self.white)
				self.draw_grid()


	def take_turn(self, x, y, n):
		if self.turn == True:
			if type(self.gameState[n-1]) == int:
				self.gameState[n-1] = "X"
				label = self.font.render("X", 1, self.black)
				self.screen.blit(label, (x, y))
				self.check_for_win("X")
		else:
			if type(self.gameState[n-1]) == int:
				self.gameState[n-1] = "O"
				label = self.font.render("O", 1, self.black)
				self.screen.blit(label, (x, y))
				self.check_for_win("O")	
		self.turn = not self.turn

	def win(self, n):
		label = self.font2.render((n + " Wins"), 1, self.black)
		self.screen.blit(label,(50, 380))
		self.gameState = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]	

if __name__ == "__main__":
	game = TicTacToe()