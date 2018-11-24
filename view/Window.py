import pygame
from win32api import GetSystemMetrics

"""
	An abstract class for future menu.
	Now it's also a test class.
"""

pygame.font.init()

myfont = pygame.font.SysFont('Comic Sans MS', 30)

class Window:
	def __init__(self):
		self.size = GetSystemMetrics(0), GetSystemMetrics(1)
		self.screen = pygame.display.set_mode(self.size)
		pygame.display.set_caption('Last Stand')

	def update(self, statistics, health):
		self.screen.fill([67,87,68])
		self.display_text(statistics, health)

	def display_text(self,statistics, player):
		kills = myfont.render("Kills: " + str(statistics.getKills()), False, (255,255,255))
		self.screen.blit(kills,(0, 0))
		rounds = myfont.render("Wave: " + str(statistics.getRound()), False, (255,255,255))
		self.screen.blit(rounds,(self.size[1] + 415, 0))
		if not player.isAlive:
			endFont =  pygame.font.SysFont('Comic Sans MS', 50)
			gameEnd = endFont.render("Game End", False, (255,255,255))
			self.screen.blit(gameEnd,(self.size[0] // 2 - 100, self.size[1] // 2))	
		health = myfont.render("Health: " + str(player.getHealth()), False, (255,255,255))
		self.screen.blit(health,(self.size[1] + 400, self.size[0]/2))

	def get_size(self):
		return self.size

	def screen(self):
		return self.screen