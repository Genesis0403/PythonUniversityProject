import pygame as pg
import sys
from view.Window import Window
from entities.Entity import Entity
from entities.Bullet import Bullet
from entities.Player import Player
from entities.Enemy import Enemy

window = Window()
clock = pg.time.Clock()
pg.key.set_repeat(10, 10)
size = [100,100]
speed = 5
player = Player(size, "entities/b.png")

entities = pg.sprite.Group()
enemies = pg.sprite.Group()
bullets = pg.sprite.Group()

entities.add(player)
enemies.add(Enemy(size, "entities/a.png"))
old_time = pg.time.get_ticks()
new_time = pg.time.get_ticks()

while 1:
	
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()
		if pg.key.get_pressed()[pg.K_w]:
			player.move(0, -speed)
		if pg.key.get_pressed()[pg.K_s]:
			player.move(0, speed)
		if pg.key.get_pressed()[pg.K_d]:
			player.move(speed, 0)
		if pg.key.get_pressed()[pg.K_a]:
			player.move(-speed, 0)
		if pg.mouse.get_pressed()[0]:
			new_time = pg.time.get_ticks()
			if (new_time - old_time >= 200):
				bullets.add(player.fire())
				old_time = new_time
	
	window.update()
	entities.update()
	enemies.update(player.position())
	bullets.update()

	entities.draw(window.screen)
	enemies.draw(window.screen)
	bullets.draw(window.screen)
	
	clock.tick(60)
	pg.display.update()