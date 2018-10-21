import pygame

class Entity(pygame.sprite.Sprite):
	
	def __init__(self, size):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface(size)
		self.image.fill([0,0,0])
		self.rect = self.image.get_rect(center=(600,600))

	def move(self, x, y):
		self.rect = self.rect.move(x, y)

	def image(self):
		return image

	def rect(self):
		return rect
