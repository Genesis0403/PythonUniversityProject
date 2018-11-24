import pygame
from pygame.math import Vector2
from entities.Bullet import Bullet
from entities.Entity import Entity
import math

class Player(Entity):
	def __init__(self, size, image):
		image = pygame.transform.scale(pygame.image.load(image), size)
		Entity.__init__(self, size, image)
		self.size = size
		self.isAlive = True
		self.health = 200
		self.speed = 5
		self.damage = 30
		self.rect = self.cpyimage.get_rect(center=(600, 400))
		self.pos = Vector2(self.rect.centerx, self.rect.centery)

	def getHealth(self):
		return self.health

	def buffDamage(self):
		if self.damage <= 80:
			self.damage += self.damage * 0.1

	def getDamage(self, damage):
		self.health -= damage
		if (self.health <= 0):
			self.isAlive = False
		return False

	def move(self):
		if pygame.key.get_pressed()[pygame.K_w]:
			if self.rect.y >= 0:
				self.rect = self.rect.move(0, -self.speed)
		if pygame.key.get_pressed()[pygame.K_s]:
			if self.rect.y + self.size[0] <= 730:
				self.rect = self.rect.move(0, self.speed)
		if pygame.key.get_pressed()[pygame.K_d]:
			if self.rect.x + self.size[0] <= 1350:
				self.rect = self.rect.move(self.speed, 0)
		if pygame.key.get_pressed()[pygame.K_a]:
			if self.rect.x >= 0:
				self.rect = self.rect.move(-self.speed, 0)
		self.pos = Vector2(self.rect.centerx, self.rect.centery)

	def fire(self):
		return Bullet(self.position(), self.damage, 20)
