import pygame
from pygame.math import Vector2

size = [5,3]

class Bullet(pygame.sprite.Sprite):
	def __init__(self, position, angle, speed):
		pygame.sprite.Sprite.__init__(self)

		self.bullet = pygame.Surface(size)
		self.bullet = pygame.transform.rotate(self.bullet, angle)
		self.rectangle = self.bullet.get_rect(center=position)
		self.bullet.fill([0,0,0])
		self.speed = speed
		self.pos = Vector2(position)
		self.direction = pygame.mouse.get_pos() - self.pos	
		self.direction = self.direction.normalize()
	
	def update(self):
		self.pos += self.direction * self.speed
		self.rectangle.center = self.pos