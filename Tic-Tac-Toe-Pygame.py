import pygame   
class TicTacToe(object):
	def __init__(self):
		pygame.init()
		title_icon = pygame.image.load("TitleIcon.png")
		pygame.display.set_caption("Tic-Tac-Toe")
		pygame.display.set_icon(title_icon)
		self.turn = True
		#store the font that will be used in the variable "font"
		self.font = pygame.font.SysFont("monospace", 100)
		#create the pygame root screen called "screen"
		self.screen = pygame.display.set_mode((400, 550))
		#"gameState" stores the current state of the game in the format of a list
		self.gameState = [1,2,3,4,5,6,7,8,9]
		#define a few colours that we will use as variables
		self.white = [255,255,255]
		self.black = [000,000,000]
		#fill the background of the root screen with the color "white"
		self.screen.fill(self.white)
		self.draw_grid()
		#game mainloop which deals with the running of the game
		self.main_loop()

	def draw_grid(self):
		pygame.draw.line(self.screen,(self.black),(50,50),(350,50), (5))
		pygame.draw.line(self.screen,(self.black),(50,150),(350,150), (5))
		pygame.draw.line(self.screen,(self.black),(50,250),(350,250), (5))
		pygame.draw.line(self.screen,(self.black),(50,350),(350,350), (5))
		pygame.draw.line(self.screen,(self.black),(50,50),(50,350), (5))
		pygame.draw.line(self.screen,(self.black),(150,50),(150,350), (5))
		pygame.draw.line(self.screen,(self.black),(250,50),(250,350), (5))
		pygame.draw.line(self.screen,(self.black),(350,50),(350,350), (5))
		pygame.draw.line(self.screen,(self.black),(50,400),(50,500), (5))
		pygame.draw.line(self.screen,(self.black),(50,400),(350,400), (5))
		pygame.draw.line(self.screen,(self.black),(50,500),(350,500), (5))
		pygame.draw.line(self.screen,(self.black),(350,400),(350,500), (5))

	def reset_game(self, x, y):
		if x <= 350 and x > 50:
			if y <= 500 and y > 400:
				self.gameState = [1,2,3,4,5,6,7,8,9]
				self.turn = True
				self.screen.fill(self.white)
				self.draw_grid()

	
			

	"""Mainloop function which is a While loop that runs the whole time the game is running. This function controls finding the location of the mouse when clicked
	     and where the counter should be placed"""
	def main_loop(self):
		#start the mainloop depending on the if the variable "running" is True 
		running = True
		while running:
			pygame.display.update()
			#for loop for all the events given from pygame
			for event in pygame.event.get():
				#when the player clicks on the screen
				if event.type == pygame.MOUSEBUTTONUP:
					x,y = event.pos
					#pass the "gameState" "x" and "x" arguments to grid function
					self.placement_grid(x, y)
					self.reset_game(x, y)
				#if the event is a QUIT event stop running the game 
				if event.type == pygame.QUIT:
					running = False

	def place_counter(self, x, y, n):
		if self.turn == True:
			label = self.font.render("X", 1, self.black)
			self.screen.blit(label, (x, y))
			for value in self.gameState:
				if value == n:
					self.gameState[value-1] = "X"
			self.check_for_win("X")
		else:
			label = self.font.render("O", 1, self.black)
			self.screen.blit(label, (x-4, y))
			for value in self.gameState:
				if value == n:
					self.gameState[value-1] = "O"
				self.check_for_win("O")

	def check_for_win(self, n):
		
		if self.gameState[0] == n and self.gameState[1] == n and self.gameState[2] == n:
			print(n, "Wins ")
			
		elif self.gameState[3] == n and self.gameState[4] == n and self.gameState[5] == n:
			print(n, "Wins ")
			
		elif self.gameState[6] == n and self.gameState[7] == n and self.gameState[8] == n:
			print(n, "Wins ")
			
		elif self.gameState[0] == n and self.gameState[4] == n and self.gameState[8] == n:
			print(n, "Wins ")
			
		elif self.gameState[0] == n and self.gameState[3] == n and self.gameState[6] == n:
			print(n, "Wins ")
			
		elif self.gameState[1] == n and self.gameState[4] == n and self.gameState[7] == n:
			print(n, "Wins ")
			
		elif self.gameState[2] == n and self.gameState[5] == n and self.gameState[8] == n:
			print(n, "Wins ")
			
		elif self.gameState[2] == n and self.gameState[4] == n and self.gameState[6] == n:
			print(n, "Wins")

	"""This functions takes the "x" "y" variables and returns where the counter should be placed on the grid. This function also updates the "gameState" list which
	store the current state of the game """ 
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
		#change bool value to opposite value to allow alternating between placing "X" and "O"
		if self.turn == True:
			self.turn = False
		else:
			self.turn = True

game = TicTacToe()
