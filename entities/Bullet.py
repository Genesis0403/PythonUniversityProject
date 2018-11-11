import pygame
from pygame.math import Vector2

size = [5,3]

class Bullet(pygame.sprite.Sprite):
	def __init__(self, position, angle, speed):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface(size)
		self.pos = Vector2(position)
		self.rect = self.image.get_rect(center=position)
		self.image.fill([0,0,0])
		self.rotate()
		self.speed = speed
		self.direction = pygame.mouse.get_pos() - self.pos  	
		self.direction = self.direction.normalize()

	def rotate(self):
		mouseVec = pygame.mouse.get_pos() - self.pos
		redius, self.angle = mouseVec.as_polar()
		self.image = pygame.transform.rotate(self.image, self.angle)
		#print(-self.angle)
		self.rect = self.image.get_rect(center=self.rect.center)

	def update(self):
		self.pos += self.direction * self.speed
		self.rect.center = self.pos