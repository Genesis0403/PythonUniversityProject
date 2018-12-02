import pygame
import sys
import random
from view.Window import Window
from view.Hud import Hud
from entities.Entity import Entity
from entities.Bullet import Bullet
from entities.Player import Player
from entities.Enemy import Enemy
from logic.Statistic import Statistic

def load_image(link):
	return pygame.transform.scale(pygame.image.load(link).convert_alpha(),(80,80))

pygame.init()

class Game:
	def __init__(self):
		self.window = Window()
		self.hud = Hud(self.window.screen, self.window.size)
		self.statistics = Statistic()
		self.clock = pygame.time.Clock()
		pygame.key.set_repeat(40, 30)
		self.size = [80,80]
		self.player = Player(self.size, "entities/bb.png")
		self.enemies_buffer = 15

		self.knifeAnimation = load_image('entities/attack/a0.png'), load_image('entities/attack/a1.png'),load_image('entities/attack/a2.png'),\
						load_image('entities/attack/a3.png'), load_image('entities/attack/a4.png'),load_image('entities/attack/a5.png'),\
						load_image('entities/attack/a6.png'), load_image('entities/attack/a7.png'),load_image('entities/attack/a8.png'),\
						load_image('entities/attack/a9.png'), load_image('entities/attack/a10.png'),load_image('entities/attack/a11.png'),\
						load_image('entities/attack/a12.png'), load_image('entities/attack/a13.png'),load_image('entities/attack/a14.png')

		self.entities = pygame.sprite.Group()
		self.enemies = pygame.sprite.Group()
		self.bullets = pygame.sprite.Group()

		self.entities.add(self.player)
		self.old_time = pygame.time.get_ticks()
		self.new_time = pygame.time.get_ticks()


	def gameUpdate(self):
		if len(self.enemies.sprites()) == 0:
			self.statistics.plusRound()
			round = self.statistics.getRound()
			self.player.buffDamage()
			for amount in range(round % self.enemies_buffer):
				if (round % 15 == 0):
					self.enemies_buffer += 5

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
				self.enemies.add(Enemy(self.size, self.knifeAnimation, spawn))

	def collisions(self, group1, group2, kill1, kill2):
		collision = pygame.sprite.groupcollide(group1, group2, kill1, kill2)
		for unit in collision:
			for second_unit in collision[unit]:
				self.statistics.plusKill(unit.getDamage(second_unit.dealDamage()))

	def enemies_collision(self, enemies):
		for enemy in enemies:
			for second_enemy in enemies:
				if pygame.sprite.collide_rect(enemy, second_enemy):
					if (enemy == second_enemy):
						enemy.speed = 0.01
						continue
					enemy.speed = 0
				else:
					enemy.speed = 0.01

	def loop(self):
		pygame.mixer.Channel(0).set_volume(0.25)
		pygame.mixer.Channel(0).play(pygame.mixer.Sound('music.wav'), 99999)
		running = True
		paused = False
		while running:
			
			self.gameUpdate()

			for event in pygame.event.get():
				if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
					sys.exit()

				self.player.move()
				
				if pygame.mouse.get_pressed()[0]:
					self.new_time = pygame.time.get_ticks()
					if (self.new_time - self.old_time >= 200):
						pygame.mixer.music.load("shot.mp3")
						self.bullets.add(self.player.fire())
						pygame.mixer.music.set_volume(0.4)
						pygame.mixer.music.play()
						self.old_time = self.new_time

			if self.player.isAlive and not paused:
			
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
				self.hud.update(self.statistics, self.player)
			
			self.clock.tick(60)
			pygame.display.update()

def main():
	game = Game()
	game.loop()

main()