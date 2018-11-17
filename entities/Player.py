import pygame
from pygame.math import Vector2
from entities.Bullet import Bullet
from entities.Entity import Entity
import math

class Player(Entity):
	def __init__(self, size, image):
		Entity.__init__(self, size, image)
		#self.cpyimage.fill([255,255,255])
		self.health = 200
		self.speed = 5
		self.rect = self.cpyimage.get_rect(center=(200, 200))
		self.pos = Vector2(self.rect.centerx, self.rect.centery)

	def getDamage(self, damage):
		self.health -= damage
		if (self.health < 0):
			pass
			#pygame.sprite.Sprite.kill(self)

	def move(self):
		if pygame.key.get_pressed()[pygame.K_w]:
			self.rect = self.rect.move(0, -self.speed)
		if pygame.key.get_pressed()[pygame.K_s]:
			self.rect = self.rect.move(0, self.speed)
		if pygame.key.get_pressed()[pygame.K_d]:
			self.rect = self.rect.move(self.speed, 0)
		if pygame.key.get_pressed()[pygame.K_a]:
			self.rect = self.rect.move(-self.speed, 0)
		self.pos = Vector2(self.rect.centerx, self.rect.centery)

	def fire(self):
		return Bullet(self.position(), self.angle, 20)
