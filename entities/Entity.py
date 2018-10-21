import pygame
import math
"""
	An abstract class for future use.
	Now it's using for testing purpose
"""

class Entity(pygame.sprite.Sprite):
	
	def __init__(self, size):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface(size)
		self.image = pygame.image.load("entities/a.png")
		self.image = pygame.transform.scale(self.image, (100, 100))
		#self.image.fill([255,255,255])
		self.cpyimage = self.image.copy()
		self.rect = self.image.get_rect(center=(50,50))
		self.angle = 0

	def move(self, x, y):
		self.rect = self.rect.move(x, y)

	def image(self):
		return self.cpyimage

	def rect(self):
		return self.rect

	def rotate(self):
		mouse_x, mouse_y = pygame.mouse.get_pos()
		old = self.rect.center
		self.angle = math.degrees(math.atan2(self.rect.centerx - mouse_x, self.rect.centery - mouse_y))
		self.cpyimage = pygame.transform.rotozoom(self.image, self.angle, 1)
		self.rect = self.cpyimage.get_rect(center=self.rect.center)

