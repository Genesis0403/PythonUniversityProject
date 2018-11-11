import pygame as pg
import sys
from view.Window import Window
from entities.Entity import Entity
from entities.Bullet import Bullet


window = Window()
clock = pg.time.Clock()
pg.key.set_repeat(10, 10)
size = [100,100]
speed = 5
entity = Entity(size)
entities = pg.sprite.Group()
entities.add(entity)
bullets = pg.sprite.Group()
old_time = 0
new_time = pg.time.get_ticks()

while 1:
	
	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()
		if pg.key.get_pressed()[pg.K_w]:
			entity.move(0, -speed)
		if pg.key.get_pressed()[pg.K_s]:
			entity.move(0, speed)
		if pg.key.get_pressed()[pg.K_d]:
			entity.move(speed, 0)
		if pg.key.get_pressed()[pg.K_a]:
			entity.move(-speed, 0)
		if pg.mouse.get_pressed()[0]:
			old_time = new_time
			new_time = pg.time.get_ticks()
			if (new_time - old_time >= 50):
				bullets.add(entity.fire())
	
	window.update()
	entities.update()
	bullets.update()
	entities.draw(window.screen)
	bullets.draw(window.screen)
	clock.tick(60)
	pg.display.update()