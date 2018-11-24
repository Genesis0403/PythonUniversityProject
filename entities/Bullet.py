import pygame
from pygame.math import Vector2

size = [5,3]

class Bullet(pygame.sprite.Sprite):
	def __init__(self, position, damage, speed):
		pygame.sprite.Sprite.__init__(self)

		self.damage = damage
		self.image = pygame.Surface(size)
		self.pos = Vector2(position)
		self.rect = self.image.get_rect(center=position)
		self.image.fill([255,204,0])
		self.rotate()
		self.speed = speed
		self.direction = pygame.mouse.get_pos() - self.pos  	
		self.direction = self.direction.normalize()

	def dealDamage(self):
		return self.damage

	def rotate(self):
		mouseVec = pygame.mouse.get_pos() - self.pos
		redius, self.angle = mouseVec.as_polar()
		self.image = pygame.transform.rotate(self.image, self.angle)
		self.rect = self.image.get_rect(center=self.rect.center)

	def update(self):
		self.pos += self.direction * self.speed
		self.rect.center = self.pos