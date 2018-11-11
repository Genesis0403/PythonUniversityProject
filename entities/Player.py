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

	def fire(self):
		return Bullet(self.position(), self.angle, 20)
