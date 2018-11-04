import pygame
from pygame.math import Vector2
import math
"""
	An abstract class for future use.
	Now it's using for testing purpose
	Angle formula: ->
	self.angle = math.degrees(-math.atan2(mouse_y - self.rect.centery, mouse_x - self.rect.centerx))
"""

class Entity(pygame.sprite.Sprite):
	
	def __init__(self, size):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface(size)
		self.image = pygame.image.load("entities/b.png")
		self.image = pygame.transform.scale(self.image, size)
		#self.image.fill([255,255,255])
		self.cpyimage = self.image.copy()
		self.rect = self.image.get_rect(center=(50,50))
		self.direction = Vector2(1,0)
		self.pos = Vector2(self.rect.centerx, self.rect.centery)
		self.angle = 0

	def move(self, x, y):
		self.rect = self.rect.move(x, y)

	def position(self):
		return self.rect.centerx, self.rect.centery;

	def image(self):
		return self.cpyimage

	def rect(self):
		return self.rect

	def angle(self):
		return self.angle

	def rotate(self):
		mouseVec = pygame.mouse.get_pos() - self.pos
		redius, self.angle = mouseVec.as_polar()
		self.cpyimage = pygame.transform.rotozoom(self.image, -self.angle, 1)
		print(-self.angle)
		self.rect = self.cpyimage.get_rect(center=self.rect.center)
		self.pos = Vector2(self.rect.centerx, self.rect.centery)

	def update(self):
		self.rotate()