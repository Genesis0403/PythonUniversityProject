import pygame
from win32api import GetSystemMetrics

"""
	An abstract class for future menu.
	Now it's also a test class.
"""

pygame.init()

class Window:
	def __init__(self):
		self.size = GetSystemMetrics(0), GetSystemMetrics(1)
		self.screen = pygame.display.set_mode(self.size)

	def update(self):
		self.screen.fill([134,228,225])
	
	def flip(self, entity):
		self.screen.blit(entity.cpyimage, entity.rect)

	def screen(self):
		return self.screen