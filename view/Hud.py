import pygame

pygame.font.init()

font_link = 'd:/laststand/view/commando.ttf'
myfont = pygame.font.Font(font_link, 30)

class Hud:
	def __init__(self, screen, size):
		self.size = size
		self.screen = screen

	def update(self, statistics, health):
		self.display_text(statistics, health)

	def display_kills(self, statistics, player, surface):
		kills = myfont.render("Kills: " + str(statistics.getKills()), False, (255,255,255))
		surface.blit(kills,(50, 25))

	def display_health(self, statistics, player, surface):
		health = myfont.render("Health: " + str(player.getHealth()), False, (255,255,255))
		surface.blit(health,(self.size[1] + 400, self.size[0]/2 + 25))

	def display_waves(self, statistics, player, surface):
		rounds = myfont.render("Wave: " + str(statistics.getRound()), False, (255,255,255))
		surface.blit(rounds,(self.size[1] + 425, 25))

	def display_gameOver(self, surface):
		endFont =  pygame.font.SysFont(font_link, 50)
		gameEnd = endFont.render("Game Over", False, (255,255,255))
		surface.blit(gameEnd,(self.size[0] // 2 - 100, self.size[1] // 2))

	def display_text(self,statistics, player):
		surface = pygame.Surface(self.size, pygame.SRCALPHA, 32)
		self.display_kills(statistics, player, surface)
		self.display_waves(statistics, player, surface)
		if not player.isAlive:
			self.display_gameOver(surface)
		self.display_health(statistics, player, surface)		
		self.screen.blit(surface, (0,0))
