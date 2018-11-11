import pygame
from pygame.math import Vector2
from entities.Bullet import Bullet
from entities.Entity import Entity
import math

class Enemy(Entity):
	def __init__(self, size, image):
		Entity.__init__(self, size, image)
		self.health = 100
		self.speed = 0.01
		self.rect = self.cpyimage.get_rect(center=(100, 100))
		self.pos = Vector2(1, 0)
		self.diraction = Vector2(1,0)


	def rotate(self, player_pos):
		player = Vector2(player_pos)
		self.diraction = player_pos - self.pos

		redius, self.angle = self.diraction.as_polar()
		self.image = pygame.transform.rotozoom(self.cpyimage, -self.angle, 1)
		#print(-self.angle)
		self.rect = self.image.get_rect(center=self.rect.center)
		#self.pos = Vector2(self.rect.center)

	def follow_player(self):
		self.pos += self.diraction * self.speed
		self.rect.center = self.pos 

	def update(self, player_pos):
		self.rotate(player_pos)
		self.follow_player()

	def bite(self):
		pass