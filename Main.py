import pygame as pg
import sys
import random
from view.Window import Window
from entities.Entity import Entity
from entities.Bullet import Bullet
from entities.Player import Player
from entities.Enemy import Enemy

window = Window()
clock = pg.time.Clock()
pg.key.set_repeat(40, 30)
size = [117,100]
player = Player(size, "entities/bb.png")

entities = pg.sprite.Group()
enemies = pg.sprite.Group()
bullets = pg.sprite.Group()

entities.add(player)
old_time = pg.time.get_ticks()
new_time = pg.time.get_ticks()

def gameUpdate(enemies):
	if len(enemies.sprites()) == 0:
		for amount in range(3):
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
			enemies.add(Enemy(size, "entities/aa.png", spawn))

while 1:
	
	gameUpdate(enemies)
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()
		
		player.move()
		
		if pg.mouse.get_pressed()[0]:
			new_time = pg.time.get_ticks()
			if (new_time - old_time >= 200):
				bullets.add(player.fire())
				old_time = new_time
	
	for unit in pg.sprite.groupcollide(enemies, bullets, False, True):
		unit.getDamage(30)

	for unit in pg.sprite.groupcollide(entities, enemies, False, False):
		unit.getDamage(30)

	for enemy in enemies:
		for second_enemy in enemies:
			if pg.sprite.collide_rect(enemy, second_enemy):
				if (enemy == second_enemy):
					enemy.speed = 0.01
					continue
				enemy.speed = 0
			else:
				enemy.speed = 0.01

	window.update()
	entities.update()
	enemies.update(player.position())
	bullets.update()

	entities.draw(window.screen)
	enemies.draw(window.screen)
	bullets.draw(window.screen)
	
	clock.tick(60)
	pg.display.update()