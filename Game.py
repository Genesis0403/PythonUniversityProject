import pygame as pg
import sys
import random
from view.Window import Window
from entities.Entity import Entity
from entities.Bullet import Bullet
from entities.Player import Player
from entities.Enemy import Enemy
from logic.Statistic import Statistic

class Game:
	def __init__(self):
		self.window = Window()
		self.statistics = Statistic()
		self.clock = pg.time.Clock()
		pg.key.set_repeat(40, 30)
		self.size = [80,80]
		self.player = Player(self.size, "entities/bb.png")
		self.round = 0

		self.entities = pg.sprite.Group()
		self.enemies = pg.sprite.Group()
		self.bullets = pg.sprite.Group()

		self.entities.add(self.player)
		self.old_time = pg.time.get_ticks()
		self.new_time = pg.time.get_ticks()


	def gameUpdate(self):
		if len(self.enemies.sprites()) == 0:
			self.round += 1
			self.player.buffDamage()
			for amount in range(self.round % 25):
				dice = random.randrange(0, 4)
				spawn = None
				if (dice == 0):
					spawn = random.randrange(-100, 1400), random.randrange(-100, 0)
				elif (dice == 1):
					spawn = random.randrange(-100,0), random.randrange(0, 800)
				elif (dice == 2):
					spawn = random.randrange(0, 1400), random.randrange(800, 900)
				else:
					spawn = random.randrange(1400, 1500), random.randrange(0, 800)
				self.enemies.add(Enemy(self.size, "entities/aa.png", spawn))

	def collisions(self, group1, group2, kill1, kill2):
		collision = pg.sprite.groupcollide(group1, group2, kill1, kill2)
		for unit in collision:
			for second_unit in collision[unit]:
				self.statistics.plusKill(unit.getDamage(second_unit.dealDamage()))

	def enemies_collision(self, enemies):
		for enemy in enemies:
			for second_enemy in enemies:
				if pg.sprite.collide_rect(enemy, second_enemy):
					if (enemy == second_enemy):
						enemy.speed = 0.01
						continue
					enemy.speed = 0
				else:
					enemy.speed = 0.01

	def loop(self):
		pg.mixer.Channel(0).set_volume(0.25)
		pg.mixer.Channel(0).play(pg.mixer.Sound('music.wav'), 99999)
		running = True
		while running:
			
			self.gameUpdate()
			for event in pg.event.get():
				if event.type == pg.QUIT:
					sys.exit()
				
				self.player.move()
				
				if pg.mouse.get_pressed()[0]:
					self.new_time = pg.time.get_ticks()
					if (self.new_time - self.old_time >= 200):
						pg.mixer.music.load("shot.mp3")
						self.bullets.add(self.player.fire())
						pg.mixer.music.set_volume(0.4)
						pg.mixer.music.play()
						self.old_time = self.new_time
			
			self.collisions(self.enemies, self.bullets, False, True)
			self.collisions(self.entities, self.enemies, False, False)
			self.enemies_collision(self.enemies)

			self.window.update()
			self.entities.update()
			self.enemies.update(self.player.position())
			self.bullets.update()

			self.entities.draw(self.window.screen)
			self.enemies.draw(self.window.screen)
			self.bullets.draw(self.window.screen)
			
			self.clock.tick(60)
			pg.display.update()

def main():
	game = Game()
	game.loop()

main()