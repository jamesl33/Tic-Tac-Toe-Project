import pygame

class TicTacToe(object):
	def __init__(self):
		pygame.init()
		width, height = 400, 500
		self.screen = pygame.display.set_mode((width, height))
		pygame.display.set_caption("Tic-Tic-Toe")

game = TicTacToe()