import pygame
class TicTacToe(object):
	def __init__(self):
		pygame.init()
		title_icon = pygame.image.load("TitleIcon.png")
		pygame.display.set_icon(title_icon)
		pygame.display.set_caption("Tic-Tac-Toe")
		self.turn = True
		self.white = [255,255,255]
		self.black = [000,000,000]
		self.gameState = [1,2,3,4,5,6,7,8,9]
		self.screen = pygame.display.set_mode((400,550))
		self.screen.fill(self.white)
		self.font = pygame.font.SysFont("monospace", 100)
		self.font2 = pygame.font.SysFont("monospace", 15)
		self.font3 = pygame.font.SysFont("monospace", 30)
		self.draw_grid()
		self.main_loop()
	"""Mainloop that handles running the game.This function calls
	the other function when needed.When this loop ends the game 
	has ended."""
	def main_loop(self):
		running = True
		while running:
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONUP:
					x,y = event.pos
					self.placement_grid(x,y)
					self.reset_game(x,y)
				if event.type == pygame.QUIT:
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
		pygame.draw.line(self.screen,(self.black),(250,375),(350,375), (1))
		pygame.draw.line(self.screen,(self.black),(250,375),(250,400), (1))
		pygame.draw.line(self.screen,(self.black),(250,400),(350,400), (1))
		pygame.draw.line(self.screen,(self.black),(350,375),(350,400), (1))

		label = self.font2.render(("Reset Game"), 1, self.black)
		self.screen.blit(label,(255,378))
	"""Reset game function. This function resets all of the values back to the same
	values that the game has when it is first initialised. This function also redraws
	the grid and buttons."""
	def reset_game(self, x, y):
		if x <= 350 and x > 250:
			if y <= 400 and y > 375:
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
		if x <= 150:
			if y < 150:
				self.place_counter(70, 45, 1)
			elif y >= 150 and y < 250:
				self.place_counter(70, 145, 4)
			elif y >= 250 and y <= 350:
				self.place_counter(70, 245, 7)
		elif x > 150 and x <= 250:
			if y < 150:
				self.place_counter(170, 45, 2)
			elif y >= 150 and y < 250:
				self.place_counter(170, 145, 5)
			elif y >= 250 and y <= 350:
				self.place_counter(170, 245, 8)
		elif x > 250 and x <= 350:
			if y < 150:
				self.place_counter(270, 45, 3)
			elif y >= 150 and y < 250:
				self.place_counter(270, 145, 6)
			elif y >= 250 and y <= 350:
				self.place_counter(270, 245, 9)
	"""This function handles the blitting of the "X" or "O" on the board. This is done
	by blitting the label to the grid at the "x" and "y" coords give by the arguments "x" and 
	"y"."""
	def place_counter(self, x, y, n):
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
		label = self.font3.render((n + " Wins!"), 1, self.black)
		self.screen.blit(label,(145, 475))
		self.gameState = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]

game = TicTacToe()
