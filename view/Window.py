import pygame
from win32api import GetSystemMetrics

"""
	An abstract class for future menu.
	Now it's also a test class.
"""

class Window:
	def __init__(self):
		self.size = GetSystemMetrics(0), GetSystemMetrics(1)
		self.screen = pygame.display.set_mode(self.size, pygame.FULLSCREEN)
		pygame.display.set_caption('Last Stand')

	def update(self):
		self.screen.fill([67,87,68])

	def get_size(self):
		return self.size

	def screen(self):
		return self.screen