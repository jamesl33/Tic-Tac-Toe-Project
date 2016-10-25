import pygame	
class TicTacToe(object):
	def __init__(self):
		pygame.init()
		#store the font that will be used in the variable "font"
		font = pygame.font.SysFont("monospace", 15)
		#create the pygame root screen called "screen"
		screen = pygame.display.set_mode((600,600))
		#"gameState" stores the current state of the game in the format of a list
		gameState = []
		#define a few colours that we will use as variables
		white = [255,255,255]
		black = [000,000,000]
		#fill the background of the root screen with the color "white"
		screen.fill(white)
		#draw lines to build the TicTacToe grid
		pygame.draw.line(screen,(black),(200,0),(200,600), (5))
		pygame.draw.line(screen,(black),(400,0),(400,600), (5))
		pygame.draw.line(screen,(black),(0,200),(600,200), (5))
		pygame.draw.line(screen,(black),(0,400),(600,400), (5))
		#game mainloop which deals with the running of the game
		self.main_loop(gameState,font)
	"""Mainloop function which is a While loop that runs the whole time the game is running. This function controls finding hte location of the mouse when click
	and where the counter should be placed"""	
	def main_loop(self,gameState,font):
		#start the mainloop depending on the if the variable "running" is True 
		running = True
		while running:
			#update the "screen"
			pygame.display.update()
			#for loop for all the events given from pygame
			for event in pygame.event.get():
				#when the player clicks on the screen
				if event.type == pygame.MOUSEBUTTONUP:
					#store the x and y value of the mouse in the variables "x" and "y"
					x,y = event.pos
					#pass the "gameState" "x" and "x" arguments to grid function
					self.placement_grid(x, y, gameState)
					print(gameState)
				#if the event is a QUIT event stop running the game 
				if event.type == pygame.QUIT:
					running = False
				for num in gameState:
					pass
	"""This functions takes the "x" "y" variables and returns where the counter should be placed on the grid. This function also updates the "gameState" list which
	store the current state of the game """	
	def placement_grid(self, x, y, gameState):
		location = 0
		if x <= 200:
			if y < 200:
				gameState.append(1)
				location = 1
			elif y >= 200 and y < 400:
				gameState.append(4)
				location = 2
			elif y >= 400 and y <= 600:
				gameState.append(7)
				location = 3
		elif x > 200 and x <= 400:
			if y < 200:
				gameState.append(2)
				location = 4
			elif y >= 200 and y < 400:
				gameState.append(5)
				location = 5
			elif y >= 400 and y <= 600:
				gameState.append(8)
				location = 6
		elif x > 400 and x <= 600:
			if y < 200:
				gameState.append(3)
				location = 7
			elif y >= 200 and y < 400:
				gameState.append(6)
				location = 8
			elif y >= 400 and y <= 600:
				gameState.append(9)
				location = 9
		return location


game = TicTacToe()