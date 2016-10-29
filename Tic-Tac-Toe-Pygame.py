import pygame	
class TicTacToe(object):
	def __init__(self):
		pygame.init()
		self.turn = True
		#store the font that will be used in the variable "font"
		self.font = pygame.font.SysFont("monospace", 300)
		#create the pygame root screen called "screen"
		self.screen = pygame.display.set_mode((600,600))
		#"gameState" stores the current state of the game in the format of a list
		self.gameState = [1,2,3,4,5,6,7,8,9]
		#define a few colours that we will use as variables
		self.white = [255,255,255]
		self.black = [000,000,000]
		#fill the background of the root screen with the color "white"
		self.screen.fill(self.white)
		#draw lines to build the TicTacToe grid
		pygame.draw.line(self.screen,(self.black),(200,0),(200,600), (5))
		pygame.draw.line(self.screen,(self.black),(400,0),(400,600), (5))
		pygame.draw.line(self.screen,(self.black),(0,200),(600,200), (5))
		pygame.draw.line(self.screen,(self.black),(0,400),(600,400), (5))
		#game mainloop which deals with the running of the game
		self.main_loop()
	
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
				#if the event is a QUIT event stop running the game 
				if event.type == pygame.QUIT:
					running = False

	def place_counter(self, x, y, n):
		print(self.gameState)
		if self.turn == True:
			label = self.font.render("X", 1, self.black)
			self.screen.blit(label, (x, y))
			for value in self.gameState:
				if value == n:
					self.gameState[value-1] = "X"
		else:
			label = self.font.render("O", 1, self.black)
			self.screen.blit(label, (x-4, y))
			for value in self.gameState:
				if value == n:
					self.gameState[value-1] = "O"
		print(self.gameState)


	"""This functions takes the "x" "y" variables and returns where the counter should be placed on the grid. This function also updates the "gameState" list which
	store the current state of the game """	
	def placement_grid(self, x, y):
		if x <= 200:
			if y < 200:
				self.place_counter(25, 12, 1)
			elif y >= 200 and y < 400:
				self.place_counter(25, 212, 4)
			elif y >= 400 and y <= 600:
				self.place_counter(25, 412, 7)
		elif x > 200 and x <= 400:
			if y < 200:
				self.place_counter(225, 12, 2)
			elif y >= 200 and y < 400:
				self.place_counter(225, 212, 5)
			elif y >= 400 and y <= 600:
				self.place_counter(225, 412, 8)
		elif x > 400 and x <= 600:
			if y < 200:
				self.place_counter(425, 12, 3)
			elif y >= 200 and y < 400:
				self.place_counter(425, 212, 6)
			elif y >= 400 and y <= 600:
				self.place_counter(425, 425, 9)
		#change bool value to opposite value to allow alternating between placing "X" and "O"
		if self.turn == True:
			self.turn = False
		else:
			self.turn = True

game = TicTacToe()