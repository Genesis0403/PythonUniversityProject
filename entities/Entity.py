import pygame
from pygame.math import Vector2
from entities.Bullet import Bullet
import math
"""
	An abstract class for future use.
	Now it's using for testing purpose
	Angle formula: ->
	self.angle = math.degrees(-math.atan2(mouse_y - self.rect.centery, mouse_x - self.rect.centerx))
"""

class Entity(pygame.sprite.Sprite):
	
	def __init__(self, size, image):
		pygame.sprite.Sprite.__init__(self)

		self.cpyimage = pygame.Surface(size)
		self.cpyimage = image
		self.cpyimage = self.cpyimage
		self.image = self.cpyimage.copy()
		#self.rect = self.cpyimage.get_rect(center=(200, 200))
		#self.pos = Vector2(self.rect.centerx, self.rect.centery)
		self.angle = 0

	def getDamage(self, damage):
		pass

	def position(self):
		return self.pos

	def image(self):
		return self.image

	def rect(self):
		return self.rect

	def angle(self):
		return self.angle

	def rotate(self):
		mouseVec = pygame.mouse.get_pos() - self.pos
		redius, self.angle = mouseVec.as_polar()
		self.image = pygame.transform.rotozoom(self.cpyimage, -self.angle, 1)
		self.rect = self.image.get_rect(center=self.rect.center)
		self.pos = Vector2(self.rect.centerx, self.rect.centery)

	def update(self):
		self.rotate()