import pygame
from pygame.math import Vector2
from entities.Bullet import Bullet
from entities.Entity import Entity
import math

class Enemy(Entity):
	def __init__(self, size, images, spawn):
		Entity.__init__(self, size, images[0])
		self.size = size
		self.images = images
		self.old_time = pygame.time.get_ticks()
		self.health = 100
		self.damage = 10
		self.speed = 0.01
		self.attack = False
		self.index = 0
		self.rect = self.cpyimage.get_rect(center=spawn)
		self.pos = Vector2(spawn)
		self.diraction = Vector2(1,0)

	def rotate(self, player_pos):
		player = Vector2(player_pos)
		self.diraction = player_pos - self.pos
		redius, self.angle = self.diraction.as_polar()
		self.image = pygame.transform.rotozoom(self.cpyimage, -self.angle, 1).convert_alpha()
		self.rect = self.image.get_rect(center=self.rect.center)
		self.pos = Vector2(self.rect.center)

	def dealDamage(self):
		new_time = pygame.time.get_ticks()
		if new_time - self.old_time >= 1000:
			self.attack = True
			self.old_time = new_time
			return self.damage
		return 0

	def getDamage(self, damage):
		self.health -= damage
		if (self.health < 0):
			pygame.sprite.Sprite.kill(self)
			return True
		return False

	def follow_player(self):
		self.pos += self.diraction * self.speed
		self.rect.center = self.pos 

	def update(self, player_pos):
		self.animate()
		self.rotate(player_pos)
		self.follow_player()

	def animate(self):
		if self.attack and self.index < len(self.images):
			self.cpyimage = self.images[self.index]
			self.index += 1
		else:
			self.index = 0
			self.attack = False
			self.cpyimage = self.images[self.index]